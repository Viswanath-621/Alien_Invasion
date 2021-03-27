class Settings:
	"""the settings to control the game resourses"""
	def __init__(self):
		"""Initialize the game settings"""
		# Screen settings 
		self.screen_width = 1280
		self.screen_height = 720
		self.bg_color = (255,190,51)

		## Ship settings
		self.ship_speed = 10.5
		self.ship_limit = 3

		## Bullet settings
		
		self.bullet_speed = 5.9
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (212,175,55)

		## alien settings
		self.alien_speed = 1
		self.fleet_drop_speed = 1
		# fleet_direction of 1 represents right , -1 represents left 
		self.fleet_direction = 1