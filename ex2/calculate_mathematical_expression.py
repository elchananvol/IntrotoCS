def calculate_mathematical_expression(num1, num2, parameter):
    if parameter == "+":
        return (num1 + num2)
    elif parameter == "-":
        return (num1 - num2)
    elif parameter == "*":
        return (num1 * num2)
    elif parameter == "/" and num2 != 0:
        return (num1 / num2)
    else:
        return None




def calculate_from_string(math_problem):
    separation = math_problem.split()
    if separation[1] == "+":
        return (float (separation[0]) + float(separation[2]))
    elif separation[1] == "-":
        return (float (separation[0]) - float (separation[2]))
    elif separation[1] == "*":
        return (float (separation[0]) * float (separation[2]))
    elif separation[1] == "/" and (float(separation[2]) != 0):
        return (float (separation[0]) / float (separation[2]))
    else:
        return None
