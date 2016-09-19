import arcade

sprite_scale = 1
screen_w=800
screen_h=600

mov_vel=5

class MyApp(arcade.Window):
	def __init__(self,w,h):
		super().__init__(w,h)
		self.allsprites=None
		self.coins=None
		self.score=0
		self.playersprite=None
		self.walls=None
		self.phys=None

	def setup(self):
		self.allsprites=arcade.SpriteList()
		self.walls=arcade.SpriteList()

		self.score=0
		self.playersprite=arcade.Sprite("images/alienBeige.png",sprite_scale)
		self.playersprite.center_x = 172
		self.playersprite.center_y = 300
		self.allsprites.append(self.playersprite)

		for x in range(172,650,35):
			wall = arcade.Sprite("images/grassBlock.png",sprite_scale)
			wall.center_x=x
			wall.center_y=180
			self.allsprites.append(wall)
			self.walls.append(wall)
		for y in range(273,500,35):
			wall=arcade.Sprite("images/grassBlock.png",sprite_scale)
			wall.center_x=465
			wall.center_y=y
			self.allsprites.append(wall)
			self.walls.append(wall)

		self.phys = arcade.PhysicsEngineSimple(self.playersprite,self.walls)

		arcade.set_background_color(arcade.color.AMAZON)

	def on_draw(self):
		arcade.start_render()
		self.allsprites.draw()
		output = "Score: {}".format(self.score)
		arcade.draw_text(output,10,10,arcade.color.WHITE,14)

	def on_key_press(self, key,modifiers):
		if key == arcade.key.UP:
			self.playersprite.change_y=mov_vel
		elif key == arcade.key.DOWN:
			self.playersprite.change_y=-mov_vel
		elif key == arcade.key.LEFT:
			self.playersprite.change_x=-mov_vel
		elif key == arcade.key.RIGHT:
			self.playersprite.change_x=mov_vel

	def on_key_release(self, key, modifiers):
		if key == arcade.key.UP:
			self.playersprite.change_y -=mov_vel
		elif key == arcade.key.DOWN:
			self.playersprite.change_y=0
		elif key == arcade.key.LEFT:
			self.playersprite.change_x = 0
		elif key == arcade.key.RIGHT:
			self.playersprite.change_x=0

	def animate(self,dt):
		self.phys.update()

window = MyApp(screen_w,screen_h)
window.setup()
arcade.run()