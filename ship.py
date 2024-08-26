import pygame
from pathlib import Path

class Ship:
	"""to add the rocket image """
	def __init__(self,ai_game):
		"""Initialize the ship and set the position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		  
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship image and get its rect 
		self.image = pygame.image.load(Path() / 'rocket.png')
		self.rect = self.image.get_rect()

		self.image2 = pygame.image.load(Path() / 'space.jpg')
		self.rect2 = self.image2.get_rect()
		
		# Start each new ship at the bottem of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		self.rect2 = self.screen_rect
		
		# Store a decimal value for the ship's settings
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement Flag
		self.moving_right = False 
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		""" To Have ship movement based on flag """
		if self.moving_right and self.rect.right < self.screen_rect.right :
			self.x += self.settings.ship_speed 			
		if self.moving_left and self.rect.left > 0 :
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom  :
			self.y += self.settings.ship_speed

		
		# Update rect object from self.x
		self.rect.x = self.x
		self.rect.y = self.y

	def center_ship(self):
		"""Center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image2, self.rect2)
		self.screen.blit(self.image, self.rect)
		