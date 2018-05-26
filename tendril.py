import math
import random

#with help from
#https://www.nodebox.net/code/index.php/Tendrils

class Tendril:

	def __init__(self, x, y, width=15):

		self.x = x
		self.y = y
		self.width = width
		self.angle = random.uniform(0,2*3.14158)  # random angle in radians.
		self.segments = []
		self.v = 0

	def create(self, distance=3.0, curl=0.01, step=0.02, nmbSegments=50):
		distance = random.uniform(distance/2, distance)
		nmbSegments = int(round(random.uniform(nmbSegments, nmbSegments*1.2)))

		for i in range(1, nmbSegments):
			self.x += math.cos(self.angle) * distance
			self.y += math.sin(self.angle) * distance
			self.v = 0
			self.v += random.uniform(-step, step)
			self.v *= 0.9 + curl * 0.1
			self.angle += self.v

			self.segments.append((self.x, self.y, self.angle))

	def draw(self, draw):

		n = len(self.segments)
		for i, (x, y, angle) in enumerate(self.segments):

				r = self.width
				#r = (1-float(i)/2*n) * self.width # size gradually decreases.
				draw.ellipse([(x,y),((x+r),(y+r))], fill=(0,0,0))