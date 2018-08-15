choice =input('which shape do you wish to calculate for?\n(choose between triangle, square and trapezoid or cylinder to find its volume.)')
if choice =="triangle":
	#area of a triangle = (1/2)*base*height
	base = float(input("Enter length of the base of the circle"))
	height = float(input("Enter length of the height of the triangle"))
	area = ((0.5)*base*height)
elif choice ==  'trapezoid':
	
    #area of a trapezoid
    #trapezoid = (1/2)*(a+b)h

    side_a = float(input("Enter length of side a\n:"))
    side_b = float(input("Enter Length of side b\n:"))
    height = float(input("Enter the height of the trapezium"))
    area = (0.5 * ((side_a + side_b) * (height)))
    print("The area of the trapezium is",str(area) + "cm^2")
elif choice == 'square':
	
	print()
	print()
	#area of a square
	L = float(input("Enter the length of a side of the square\n:"))#ask for input
	square_area = (L**2)
	print("The are of the square is", str(round(square_area,2)) + "cm^2")
elif choice=='cylinder':
	#volume of a cylinder = pi*r**2*H

    radius = float(input("Enter the radius of the cylinder\n:"))
    height = float(input("Enter the height of the cylinder\n:"))
    volume = ((pi)*(radius**2)*(height))
    print("The volume of the cylinder is",str(area) + "cm^3")
print('thank you!')