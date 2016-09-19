import arcade

screen_w = 800
screen_h = 600

mov_speed = 3


class MyApp(arcade.Window):
	def __init__(self, w, h):
		super().__init__(w, h)
		self.allsprites = arcade.SpriteList()

		self.player = arcade.AnimatedWalkingSprite(4.0)
		filename = "images/SBM2-Bomberman.gif"

		stand_loc_list = [[52, 0, 16, 28]]
		self.player.stand_right_textures = arcade.load_textures(filename,
		                                                        stand_loc_list,
		                                                        False)
		self.player.stand_left_textures = arcade.load_textures(filename,
		                                                       stand_loc_list,
		                                                       True)
		walk_loc_list = [[52, 0, 16, 28],
		                 [72, 0, 16, 28],
		                 [52, 0, 16, 28],
		                 [89, 0, 16, 28]]
		self.player.walk_right_textures = \
			arcade.load_textures(filename, walk_loc_list, False)
		self.player.walk_left_textures = \
			arcade.load_textures(filename, walk_loc_list, True)

		walk_loc_list = [[0, 0, 18, 28],
		                 [18, 0, 18, 28],
		                 [0, 0, 18, 28],
		                 [36, 0, 18, 28]]
		self.player.walk_up_walk_textures = arcade.load_textures(filename,
		                                                         walk_loc_list,
		                                                         False)
		walk_loc_list = [[105, 0, 18, 28],
		                 [123, 0, 18, 28],
		                 [105, 0, 18, 28],
		                 [141, 0, 18, 28]]
		self.player.walk_down_textures = arcade.load_textures(filename,
		                                                      walk_loc_list,
		                                                      False)

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
		Called whenever the mouse moves.
		"""
		if key == arcade.key.UP:
			self.player.change_y = mov_speed
		elif key == arcade.key.DOWN:
			self.player.change_y = -mov_speed
		elif key == arcade.key.LEFT:
			self.player.change_x = -mov_speed
		elif key == arcade.key.RIGHT:
			self.player.change_x = mov_speed

	def on_key_release(self, key, modifiers):
		"""
		Called when the user presses a mouse button.
		"""
		if key == arcade.key.UP or key == arcade.key.DOWN:
			self.player.change_y = 0
		elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
			self.player.change_x = 0

	def animate(self, dt):
		self.allsprites.update()
		self.allsprites.update_animation()


def main():
	MyApp(screen_w, screen_h)
	arcade.run()


if __name__ == '__main__':
	main()
