import math

up = int(input("Enter the Up Coordinate:"))
x1, y1 = 0, up



down = int(input("Enter the Down Coordinate:"))
x2, y2 = 0, down



left = int(input("Enter the Left Coordinate:"))
x3, y3 = left, 0



right = int(input("Enter the Right Coordinate:"))
x4, y4 = right, 0



r1, r2 = 0, 0



r1, r2 = (x1-r1), (y1-r2)
r1, r2 = (x2-r1), (y2-r2)
r1, r2 = (x3-r1), (y3-r2)
r1, r2 = (x4-r1), (y4-r2)



print("Coordinates after all steps :" + str(r1), str(r2))



print("The distance from original Point :" +
      str(round(math.sqrt(r1**2 + r2**2))))

