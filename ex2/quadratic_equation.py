def quadratic_equation(a,b,c):
    if a != 0:
        x1 = (-b + (b**2 - 4*a*c )**0.5) / (2*a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


        if x1 != x2 and type(x1) == float and type(x2) == float:
            return x1, x2
            print(x1,x2)
        elif type(x1) != float  and type(x2) == float:
            return None,x2
        elif type(x1) == float and type(x2) != float:
            return x1, None
        elif x1==x2:
            return x1, None
        else:
            return None, None

    else:
        return None , None

def quadratic_equation_user_input():
    equation = input("Insert coefficients a, b, and c: ")
    a,b,c = equation.split(" ")
    a= float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        print("The parameter 'a' may not equal 0")
    else:
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        if x1 != x2 and type(x1) == float and type(x2) == float:
            print("The equation has 2 solutions:", x1,"and",x2)
        elif type(x1) != float  or type(x2) != float:
            print("The equation has no solutions")

        elif x1==x2:
            print("The equation has 1 solution:", x1)
    # else:
    #     return False

