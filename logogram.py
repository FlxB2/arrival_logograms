import random
import sys
from random import randint
import math
import PIL
from PIL import Image, ImageDraw, ImageFilter
from tendril import Tendril
from circularStroke import CircularStroke

#inital startpoint 
#https://mathematica.stackexchange.com/questions/137156/where-is-abbott-how-to-make-logograms-from-the-film-arrival

def disks (draw, center, rad, nmbDisks, minAngleExtent, maxAngleExtent, size=25, tendril=False):
	radVarDisk = random.uniform(size/4, size);

	for i in range(1,nmbDisks):
		angle = random.uniform(minAngleExtent, maxAngleExtent)

		varCenter = 35

		xVar = center[0] + random.uniform(-varCenter,varCenter)
		yVar = center[1] + random.uniform(-varCenter,varCenter)

		x0 = xVar + rad * math.cos(angle)
		y0 = yVar + rad * math.sin(angle)

		x1 = x0 + random.uniform(0, radVarDisk)
		y1 = y0 + random.uniform(0, radVarDisk)

		draw.ellipse([(x0,y0),(x1,y1)], fill=(0,0,0))
		tendrilVar = tendril and random.uniform(0,4) > 3.141
		if tendrilVar:
			for i in range(0,1):
				#trendrilOnBlob(draw, (x0,y0), 50, 25)
				tendril = Tendril(x0,y0,10)
				tendrilSize = randint(35,50)
				tendril.create(5.0, 10.0 ,0.1, tendrilSize)
				tendril.draw(draw)


def logogram(seed, imgSize, varThickness, varCenter, nmbCirc, varRad):

	image = Image.new("RGB", imgSize, "white")
	x = image.width/2
	y = x
	draw = ImageDraw.Draw(image)
	rad = imgSize[0]/3

	#logogram_circle(draw, nmbCirc, (x,y), varCenter, varThickness, rad, varRad)
	stroke = CircularStroke(nmbCirc, (x,y), varCenter, varThickness, rad, varRad)
	angle = randint(0,360)
	v = randint(0, 90)
	stroke.draw(draw, angle, v)

	nmbDisks = 70
	minAngleExtent = random.uniform(0,2*3.141)
	maxAngleExtent = minAngleExtent+0.4
	nmbCluster = randint(1,4)
	for i in range(0,nmbCluster):
		minAngleExtent = random.uniform(0,2*3.141)
		maxAngleExtent = minAngleExtent+0.4
		disks(draw, (x,y), rad, nmbDisks, minAngleExtent, maxAngleExtent, size=100, tendril=True)
		middleAngle = (maxAngleExtent - (-1*(minAngleExtent-maxAngleExtent)/2)) * (180/3.141)
		stroke.drawCircleBlob(draw, middleAngle, 60, 50, 20, 2)

	disks(draw, (x,y), rad, 70, 0, 2*3.141, size=25)

	#image = image.filter(ImageFilter.MaxFilter(1))
	image = image.filter(ImageFilter.BLUR)
	image = image.filter(ImageFilter.BLUR)



	#threshold
	thresholdValue = 200
	image = image.convert('L')
	fn = lambda x : 255 if x > thresholdValue else 0
	image = image.convert('L').point(fn, mode='1')


	image.thumbnail((2048,2048))

	return image

def generatePNGs(nmbPics):
	for i in range(0,nmbPics):
		seed = random.uniform(0, i) * 1000;
		string = "samples/" + str(i)+"hepta.png"
		logogram(seed, (2048,2048), 10, 10, 100, (1,1)).save(string, "PNG")


if(len(sys.argv[1:]) == 1):
	seed = float(sys.argv[1])
else: 
	seed = randint(0,10000)
random.seed(seed)
logogram(seed, (2048,2048), 10, 10, 100, (1,1)).show()
#generatePNGs(20)


