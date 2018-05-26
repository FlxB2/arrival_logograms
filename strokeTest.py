import math
import random
from random import randint
import PIL
from PIL import Image, ImageDraw, ImageFilter

def arc(image, bbox, start, end, fill, width=1.0, segments=10):

    draw = ImageDraw.Draw(image)

    """
    Hack that looks similar to PIL's draw.arc(), but can specify a line width.
    """
    # radians
    start *= math.pi / 180
    end *= math.pi / 180

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

    prev = [0,0,0,0]

    widthMax = width

    for i in range(segments):
    	var = width+randint(-widthMax,widthMax)
    	fn = lambda x: var if var > 0 else 0
    	width = fn(var)

        # angle centre
        a = start + (i+0.5) * da

        # x,y centre
        x = cx + math.cos(a) * rx
        y = cy + math.sin(a) * ry

        # derivatives
        dx = -math.sin(a) * rx / (rx+ry)
        dy = math.cos(a) * ry / (rx+ry)

        eRad = width
       # start =(x-dx*l,y-dy*l)
        draw.ellipse([x-dx*l-eRad,y-dy*l-eRad,x-dx*l+eRad,y-dy*l+eRad], fill=(255,0,0,0))

        if(prev != [0,0,0,0]):
        	#top line
        	draw.line([prev[0],prev[1],x-dx*l-eRad,y-dy*l-eRad], fill=(255,255,0,0), width=2)
        	#bottom
        	draw.line([x-dx*l+eRad,y-dy*l+eRad,prev[2],prev[3]], fill=(255,255,0,0), width=2)

        prev = [x-dx*l-eRad,y-dy*l-eRad,x-dx*l+eRad,y-dy*l+eRad]


        #middle line
        draw.line([(x-dx*l,y-dy*l), (x+dx*l, y+dy*l)], fill=fill, width=1)

    return image


seed = input("seed? ")
random.seed(seed)
size = 4000
image = Image.new("RGB", (size,size), "white")
rad = size/2 - size/10

arc(image, (size/2-rad, size/2-rad, size/2+rad, size/2+rad), 0, 200, fill=(0,0,0), width=5).show()



