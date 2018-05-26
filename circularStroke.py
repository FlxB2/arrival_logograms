import random
import math
import PIL
from random import randint
from PIL import ImageDraw

class CircularStroke:

	def __init__(self, nmb, center, centerVar, thicknessVar, rad, radVar):

		self.nmb = nmb
		self.center = center
		self.centerVar = centerVar
		self.thicknessVar = thicknessVar
		self.rad = rad
		self.radVar = radVar

	"""
	thanks to https://gist.github.com/skion/9259926
	Hack that looks similar to PIL's draw.arc(), but can specify a line width.
	"""
	def arc(self, draw, bbox, start, end, fill, width=1.0, segments=100):

		# radians
		start *= math.pi / 180.0
		end *= math.pi / 180.0

		# angle step
		da = (end - start) / segments

		# shift end points with half a segment angle
		start -= da / 2
		end -= da / 2

		# ellips radii
		rx = (bbox[2] - bbox[0]) / 2
		ry = (bbox[3] - bbox[1]) / 2

		# box centre
		cx = bbox[0] + rx
		cy = bbox[1] + ry

		# segment length
		l = (rx+ry) * da / 2.0

		widthMax = width

		for i in range(segments):
			width = randint(-widthMax,widthMax)

			# angle centre
			a = start + (i+0.5) * da

			# x,y centre
			x = cx + math.cos(a) * rx
			y = cy + math.sin(a) * ry

			# derivatives
			dx = -math.sin(a) * rx / (rx+ry)
			dy = math.cos(a) * ry / (rx+ry)

			draw.line([(x-dx*l,y-dy*l), (x+dx*l, y+dy*l)], fill=fill, width=width)

	def draw(self, draw, angle, gapWidth):
		for i in range(1, self.nmb):
			xVar = self.center[0] + random.uniform(-self.centerVar,self.centerVar)
			yVar = self.center[1] + random.uniform(-self.centerVar,self.centerVar)

			thickness = self.thicknessVar
			randomRad = self.rad * random.uniform(self.radVar[0], self.radVar[1])

			#TODO
			holeAngle = angle
			v =  gapWidth

			randomAngleStart = random.uniform(v+holeAngle,180+holeAngle-v)
			randomAngleEnd = random.uniform(randomAngleStart,360+holeAngle-v)

			self.arc(draw, (xVar-randomRad, yVar-randomRad, xVar+randomRad, yVar+randomRad), 
			randomAngleStart, randomAngleEnd, fill=(0,0,0), width=thickness)

	def drawCircleBlob(self, draw, angle, blobLength, blobWidth, nmbCircles, centerVarBlob):
		for i in range(1, nmbCircles):
			xVar = self.center[0] + random.uniform(-centerVarBlob/2, centerVarBlob)
			yVar = self.center[1] + random.uniform(-centerVarBlob/2, centerVarBlob)

			thickness = int(round(self.thicknessVar * random.uniform(0,4)))

			randomRad = self.rad + random.uniform(-blobWidth, blobWidth)

			randomAngleStart = angle + random.uniform(0, blobLength/2)
			randomAngleEnd = angle - random.uniform(0, blobLength/2)

			#print randomAngleStart
			#print randomAngleEnd

			self.arc(draw, (xVar-randomRad, yVar-randomRad, xVar+randomRad, yVar+randomRad), 
			randomAngleStart, randomAngleEnd, fill=(0,0,0), width=thickness)
