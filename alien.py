import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
	""" to have the alien on the screen """
	def __init__(self, ai_game):
		"""to initialize the alien """
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		## Load the image
		self.image = pygame.image.load('C:\\Users\\Yugandhari Bodapati\\Desktop\\python_work\\game_development\\alien_ship.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	
	def check_edges(self):
		"""to check whether the alien is hit or not """
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0 :
			return True

	def update(self):
		"""Move the alien right or left. """
		self.x += (self.settings.alien_speed* self.settings.fleet_direction)
		self.rect.x = self.x