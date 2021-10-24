# i chose (in the first case) to see what happens when the third number is the largest
# and in the second case to check what happens if involve zero and negative number
def largest_and_smallest(num1,num2,num3):
    if num1 >= num2 and num2 > num3:
         return num1,num3
    elif num1 >= num2 and num1>=num3 and num3 >= num2:
         return num1, num2
    elif num2 >= num1 and num1 >= num3:
         return num2,num3
    elif num2 >= num1 and num3 >= num1 and num2 >= num3:
         return num2, num1
    elif num3 >= num1 and num2 >= num1:
         return num3,num1
    elif num3 >= num2 and num1 >= num2:
         return num3, num2


def check_largest_and_smallest():
    if largest_and_smallest(17,1,6) == (17, 1) \
            and largest_and_smallest(1,17,6) == (17, 1) \
            and largest_and_smallest(1,1,2) == (2, 1) \
            and largest_and_smallest(1, 5, 15) == (15, 1) \
            and largest_and_smallest(1, 0, -7) == (1, -7):
        return True
    else:
         return False
