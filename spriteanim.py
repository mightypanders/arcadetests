from datetime import datetime

import arcade
import arcade.color

screen_w = 800
screen_h = 600

mov_speed = 3


def get_bomb_textures():
	file = "images/14bomberman.PNG"
	loc = [[50, 255, 16, 17],
	       [33, 255, 16, 17],
	       [18, 255, 16, 17],
	       [33, 255, 16, 17]]
	return arcade.load_textures(file, loc, False)


#  TODO Bomb Background 192,192,192 Make transparent

bomb_sprite = get_bomb_textures()


class MyApp(arcade.Window):
	def __init__(self, w, h):
		super().__init__(w, h)
		self.allsprites = arcade.SpriteList()
		self.player = SpritePlayer(scale=2, playernumber=1, color=arcade.color.PINK)
		self.allsprites.append(self.player)
		arcade.set_background_color(arcade.color.AMAZON)

	def on_draw(self):
		arcade.start_render()
		self.player.bomb_list.draw()
		self.allsprites.draw()

	def on_key_press(self, key, modifiers):
		"""
		Called whenever a key is pressed.
		"""
		self.player.getKeyDownEvent(key)

	def on_key_release(self, key, modifiers):
		"""
		Called whenever a key is released
		"""
		self.player.getKeyUpEvent(key)

	def placeBomb(self):
		bomb = arcade.AnimatedTimeSprite(1, 0, 0, self.player.position[0],
		                                   self.player.position[1])

	def animate(self, dt):
		self.player.bomb_list.update()
		self.allsprites.update()
		self.player.bomb_list.update_animation()
		self.allsprites.update_animation()


class SpritePlayer(arcade.AnimatedWalkingSprite):
	def __init__(self, scale, playernumber, color):
		super().__init__(scale=scale)
		self.PlayerNo = playernumber
		self.color = color
		self.bomb_list = arcade.SpriteList()
		self.assingTextures()
		self.walkleftkey = arcade.key.LEFT
		self.walkrightkey = arcade.key.RIGHT
		self.walkupkey = arcade.key.UP
		self.walkdownkey = arcade.key.DOWN
		self.bombkey = arcade.key.SPACE

		self.texture_change_distance = 20
		self.center_y = screen_h / 2
		self.center_x = screen_w / 2

	def putbomb(self):
		bomb = SpriteBomb(self)
		self.bomb_list.append(bomb)

	def getKeyDownEvent(self, key):
		if key == self.walkupkey:
			self.change_y += mov_speed
		elif key == self.walkdownkey:
			self.change_y -= mov_speed
		elif key == self.walkleftkey:
			self.change_x -= mov_speed
		elif key == self.walkrightkey:
			self.change_x += mov_speed
		elif key == self.bombkey:
			self.putbomb()

	def getKeyUpEvent(self, key):
		if key == self.walkupkey:
			self.change_y -= mov_speed
		elif key == self.walkdownkey:
			self.change_y += mov_speed
		elif key == self.walkleftkey:
			self.change_x += mov_speed
		elif key == self.walkrightkey:
			self.change_x -= mov_speed
		self.start_walk = True

	def assingTextures(self):
		file = "images/SBM2-Bomberman.gif"

		stand_left_right = [[52, 2, 16, 28]]
		self.stand_right_textures = arcade.load_textures(file, stand_left_right, False)
		self.stand_left_textures = arcade.load_textures(file, stand_left_right, True)

		stand_up = [[1, 2, 16, 28]]
		self.stand_up_textures = arcade.load_textures(file, stand_up, False)

		stand_down = [[106, 2, 16, 28]]
		self.stand_down_textures = arcade.load_textures(file, stand_down, False)

		walk_sprites = [[52, 2, 16, 28],
		                [70, 2, 16, 28],
		                [52, 2, 16, 28],
		                [88, 2, 16, 28]]
		self.walk_right_textures = \
			arcade.load_textures(file, walk_sprites, False)
		self.walk_left_textures = \
			arcade.load_textures(file, walk_sprites, True)

		walk_sprites = [[1, 2, 16, 28],
		                [18, 2, 16, 28],
		                [1, 2, 16, 28],
		                [35, 2, 16, 28]]
		self.walk_up_textures = arcade.load_textures(file, walk_sprites, False)

		walk_sprites = [[106, 2, 16, 28],
		                [123, 2, 16, 28],
		                [106, 2, 16, 28],
		                [140, 2, 16, 28]]
		self.walk_down_textures = arcade.load_textures(file, walk_sprites, False)


class SpriteBomb(arcade.AnimatedTimeSprite):
	def __init__(self, player):
		super().__init__(scale=2)
		self.player = player
		self.timeplaced = datetime.now()
		self.textures = bomb_sprite
		self.transparent = True
		self.set_position(player.center_x, player.center_y)
		self.texture_change_frames = 30

	def update(self):
		super(SpriteBomb, self).update()
		if datetime.now().second - self.timeplaced.second >= 3:
			self.kill()


def main():
	app = MyApp(screen_w, screen_h)
	arcade.run()


if __name__ == '__main__':
	main()
