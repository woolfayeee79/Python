def is_triangle(x, y, z):
    if z > (x+y) or y > (x+z) or x > (y+z):
        print('No')
    else:
        print('Yes')
        

#write a function that prompts the user to imput three stick lenths,
# convers them to integers, and uses is_triangle to check whether sticks with
# the given lengths can form a triangle.

def triangle():
    x = int(input("Please enter the length of the 1st stick: \n"))
    y = int(input("Please enter the length of the 2nd stick: \n"))
    z = int(input("Please enter the length of the 3nd stick: \n"))
    is_triangle(x, y, z)

triangle()











