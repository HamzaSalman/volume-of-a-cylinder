# Created by: Hamza Salman
# Created for: ICS3U
# Created on: November 2016
# this program calculates the volume of a cylinder.

import math

print 'enter the radius'
radius_input = raw_input()

print 'enter the height'
height_input = raw_input()

def volume(radius, height):
    #this uses radius and height to calculate volume
    
    volume_of_cylinder = math.pi * (float(radius) ** 2)  * float(height)
    
    return volume_of_cylinder

try:
    print('the volume of the cylinder is: ' + str(round(volume(radius_input, height_input), 2)))

except:
    print('please input your number')
