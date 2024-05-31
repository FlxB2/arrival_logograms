from random import randint
import random
import sys

from logogram import logogram

if(len(sys.argv[1:]) == 1):
	seed = float(sys.argv[1])
else: 
	seed = randint(0,10000)
random.seed(seed)
logogram((2048,2048), 10, 10, 100, (1,1)).show()