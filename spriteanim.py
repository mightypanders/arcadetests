import arcade

screen_w = 800
screen_h = 600

mov_speed = 3


class MyApp(arcade.Window):
	def __init__(self, w, h):
		super().__init__(w, h)
		self.allsprites = arcade.SpriteList()

		self.player = arcade.AnimatedWalkingSprite(4.0)
		file = "images/SBM2-Bomberman.gif"

		stand_left_right = [[52, 00, 16, 28]]
		self.player.stand_right_textures = arcade.load_textures(file, stand_left_right, False)
		self.player.stand_left_textures = arcade.load_textures(file, stand_left_right, True)

		stand_up = [[00, 00, 18, 28]]
		self.player.stand_up_textures = arcade.load_textures(file, stand_up, False)

		stand_down = [[105, 00, 18, 28]]
		self.player.stand_down_textures = arcade.load_textures(file, stand_down, False)

		walk_sprites = [[52, 00, 16, 28],
		                [72, 00, 16, 28],
		                [52, 00, 16, 28],
		                [89, 00, 16, 28]]
		self.player.walk_right_textures = \
			arcade.load_textures(file, walk_sprites, False)
		self.player.walk_left_textures = \
			arcade.load_textures(file, walk_sprites, True)

		walk_sprites = [[00, 00, 18, 28],
		                [18, 00, 18, 28],
		                [00, 00, 18, 28],
		                [36, 00, 18, 28]]
		self.player.walk_up_walk_textures = arcade.load_textures(file, walk_sprites, False)

		walk_sprites = [[105, 00, 18, 28],
		                [123, 00, 18, 28],
		                [105, 00, 18, 28],
		                [141, 00, 18, 28]]
		self.player.walk_down_textures = arcade.load_textures(file, walk_sprites, False)

		self.player.texture_change_distance = 50
		self.player.center_y = screen_h / 2
		self.player.center_x = screen_w / 2

		self.allsprites.append(self.player)
		arcade.set_background_color(arcade.color.AMAZON)

	def on_draw(self):
		arcade.start_render()
		self.allsprites.draw()

	def on_key_press(self, key, modifiers):
		"""
		Called whenever a key is pressed.
		"""
		if key == arcade.key.UP:
			self.player.change_y += mov_speed
		elif key == arcade.key.DOWN:
			self.player.change_y -= mov_speed
		elif key == arcade.key.LEFT:
			self.player.change_x -= mov_speed
		elif key == arcade.key.RIGHT:
			self.player.change_x += mov_speed

	def on_key_release(self, key, modifiers):
		"""
		Called whenever a key is released
		"""
		if key == arcade.key.UP:
			self.player.change_y -= mov_speed
		elif key == arcade.key.DOWN:
			self.player.change_y += mov_speed
		elif key == arcade.key.LEFT:
			self.player.change_x += mov_speed
		elif key == arcade.key.RIGHT:
			self.player.change_x -= mov_speed

	def animate(self, dt):
		self.allsprites.update()
		self.allsprites.update_animation()


def main():
	MyApp(screen_w, screen_h)
	arcade.run()


if __name__ == '__main__':
	main()
