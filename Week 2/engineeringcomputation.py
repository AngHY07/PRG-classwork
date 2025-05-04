#Ang Hao Yi 10273989D
import math

radiuscylinder = float(input('Kindly enter the radius of the cylinder in m '))
heightcylinder = float(input('Kindly enter the height of cylinder in m'))

volumeofcylinder = math.pi*(radiuscylinder**2)*heightcylinder

radiussphere = float (input('Kindly enter the radius of the sphere in m'))

surfaceAreaSphere = 4*math.pi*radiussphere**2

mass1 = float(input('Kindly enter mass of object 1 in kg '))
mass2= float(input('Kindlt enter mass of object 2 in kg'))
distance = float(input('Kindly enter the distance between the two object in m '))

g = 6.6743*(10**-11)

forceOfGravity = (g*mass1*mass2) / distance**2


print(f'Volume of the cylinder: {volumeofcylinder:.2f} cubic meters')
print(f'Surface area of the sphere: {surfaceAreaSphere:.2f} square meters')
print(f'Force of gravity between the objects: {forceOfGravity:.2e} Newtons')

