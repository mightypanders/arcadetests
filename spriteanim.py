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
# Bomb Background 192,192,192 Make transparent TODO

bomb_sprite = get_bomb_textures()

class MyApp(arcade.Window):
	def __init__(self, w, h):
		super().__init__(w, h)
		self.allsprites = arcade.SpriteList()

		self.player = SpritePlayer(scale=10, playernumber=1, color=arcade.color.PINK)

		self.allsprites.append(self.player)

		arcade.set_background_color(arcade.color.AMAZON)

	def on_draw(self):
		arcade.start_render()

		self.allsprites.draw()
		self.player.bomb_list.draw()

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
		bomb = arcade.AnimatedTimeSprite(2, 0, 0, self.player.position[0], self.player.position[1])

	def animate(self, dt):
		self.player.bomb_list.update()
		self.allsprites.update()
		self.player.bomb_list.update_animation()
		self.allsprites.update_animation()


def main():
	MyApp(screen_w, screen_h)
	arcade.run()


class SpritePlayer(arcade.AnimatedWalkingSprite):
	def __init__(self, scale, playernumber, color):
		super().__init__(scale=scale)
		self.PlayerNo = playernumber
		self.color = color
		self.bomb_list = arcade.SpriteList()

		file = "images/SBM2-Bomberman.gif"

		stand_left_right = [[52, 00, 16, 28]]
		self.stand_right_textures = arcade.load_textures(file, stand_left_right, False)
		self.stand_left_textures = arcade.load_textures(file, stand_left_right, True)

		stand_up = [[00, 00, 18, 28]]
		self.stand_up_textures = arcade.load_textures(file, stand_up, False)

		stand_down = [[105, 00, 18, 28]]
		self.stand_down_textures = arcade.load_textures(file, stand_down, False)

		walk_sprites = [[52, 00, 16, 28],
		                [72, 00, 16, 28],
		                [52, 00, 16, 28],
		                [89, 00, 16, 28]]
		self.walk_right_textures = \
			arcade.load_textures(file, walk_sprites, False)
		self.walk_left_textures = \
			arcade.load_textures(file, walk_sprites, True)

		walk_sprites = [[00, 00, 18, 28],
		                [18, 00, 18, 28],
		                [00, 00, 18, 28],
		                [36, 00, 18, 28]]
		self.walk_up_walk_textures = arcade.load_textures(file, walk_sprites, False)

		walk_sprites = [[105, 00, 18, 28],
		                [123, 00, 18, 28],
		                [105, 00, 18, 28],
		                [141, 00, 18, 28]]
		self.walk_down_textures = arcade.load_textures(file, walk_sprites, False)

		self.texture_change_distance = 50
		self.center_y = screen_h / 2
		self.center_x = screen_w / 2

	def putbomb(self):
		bomb = SpriteBomb(self)
		self.bomb_list.append(bomb)

	def getKeyDownEvent(self,key):
		if key == arcade.key.UP:
			self.change_y += mov_speed
		elif key == arcade.key.DOWN:
			self.change_y -= mov_speed
		elif key == arcade.key.LEFT:
			self.change_x -= mov_speed
		elif key == arcade.key.RIGHT:
			self.change_x += mov_speed
		elif key == arcade.key.SPACE:
			self.putbomb()

	def getKeyUpEvent(self,key):
		if key == arcade.key.UP:
			self.change_y -= mov_speed
		elif key == arcade.key.DOWN:
			self.change_y += mov_speed
		elif key == arcade.key.LEFT:
			self.change_x += mov_speed
		elif key == arcade.key.RIGHT:
			self.change_x -= mov_speed


class SpriteBomb(arcade.AnimatedTimeSprite):
	def __init__(self, player):
		super().__init__()
		self.player = player
		self.timeplaced = datetime.now()

		self.textures = bomb_sprite
		self.transparent=False
		self.set_position(player.center_x, player.center_y)

	def update(self):
		super(SpriteBomb, self).update()
		if datetime.now().second-self.timeplaced.second>=3:
			self.kill()


if __name__ == '__main__':
	main()
