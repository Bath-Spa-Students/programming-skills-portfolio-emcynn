#formula for area of a triangle 
def area_triangle(base, height):
    return 0.5 * base * height
     
#inputting the values of base and height 
base = float(input("Input the base of the triangle:"))
height = float(input("Input the height of the triangle:"))

#printing the answer 
print("The area of the triangle is", area_triangle(base, height))