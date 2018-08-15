#CODE FOR AREA OF A SECTOR
from math import pi
radius = float(input("Enter the radius of the sector\n:"))
print()
angle = int(input("Enter the angle of the sector\n:"))
print()
area = (angle/360)* (pi * (radius **2))
print("The area of the sector is ",str(round(area,2)) + "cm^2")
