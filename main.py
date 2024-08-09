import turtle
from turtle import *
import time
import random
from functions import *
#Begin intro
time.sleep(0.01)
readfile('intro.txt')
#Weapon selection
weaponpick()
#Leaving town to pick first destination
readfile('leave.txt')
#Loop until game ends
travel()

