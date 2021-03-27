import sys  
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""overall class to manage the game asserts and behavior"""
	def __init__(self):
		"""to create the app resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		## self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")

		# Create an instance to store game statistics .
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		
		self._create_fleet()
		## Set background colour
		## self.bg_color = (23,0,0)
	
	def _create_fleet(self):
		"""to create the fleet of aliens """
		# Make a alien
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height )
		number_rows = available_space_y // (2 * alien_height)
		## create a loop for alien group
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				# create alien and place it in a row 
				self._create_alien(alien_number, row_number)

	def _ship_hit(self):
		"""Respond to the ship being hit by an alien."""
		if self.stats.ships_left > 0:
			# DEcrement ships left.
			self.stats.ships_left -= 1

			# Get rid of any remaining aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()

			# Pause
			sleep(0.5)
		else:
			self.stats.game_active = False

	def _create_alien(self, alien_number, row_number): 
		"""to just refactor create fleet """
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number 
		alien.rect.x = alien.x 
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def run_game(self):
		""" to run all the resourses of the game created """
		while True:
			## Watch for the user keyboard responces 
			self._check_events()

			if self.stats.game_active: 
				self.ship.update()
				self._update_aliens()
				self._update_bullets()
			
			self._update_screen()
			self.bullets.update()
			

	def _update_bullets(self):

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0 :
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):

		collisions =pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
		## print(len(self.bullets))
		if not self.aliens:
			## destroy the existing bullets and create new fleet 
			self.bullets.empty()
			self._create_fleet()

	def _update_aliens(self):
		""" update the position of the alien in the fleet """
		self._check_fleet_edges()
		self.aliens.update()

		## when ship hits the alien 
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			# print("Ship hit!!! ")
			self._ship_hit()

		## Look for aliens hitting the bottom of the screen.
		self._check_aliens_bottom()

	def _check_aliens_bottom(self):
		"""check if the alien fleet reached bottom of screen"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
			# Treat this the same as if the ship got hit.
				self._ship_hit()
				break

	def _check_events(self):
		""" Resopond to the keyboard and mouse events """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)				
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)	

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge. """
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction. """
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _check_keydown_events(self,event):
		"""to check the true flags"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True 
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		"""to check the false events """
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
	
	def _fire_bullet(self):
		"""to control bullet movements """
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _update_screen(self):
		"""to update the screen """
		## Fill the background colour
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.aliens.draw(self.screen)

		# Make the most recently drawn screen 
		pygame.display.flip() 

if __name__ == '__main__':
	"Make a game instance , and run the game " 
	ai = AlienInvasion()
	ai.run_game() 
	
