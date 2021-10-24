import math
def shape_area():
    choice = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if choice == "1":
        radius = float(input())
        return math.pi * radius**2

    elif choice == "2":
         side_a = float(input())
         side_b = float(input())
         return side_a*side_b

    elif  choice == "3":
        side = float(input())
        return (side**2 * 3**0.5)/4
    else:
        return


