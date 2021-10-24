def print_to_n(n):
    if n < 1:
        return
    print_to_n(n-1)
    print(n)

def digit_sum(n):
    num_string= str(n)
    if len(num_string)== 0:
        return 0
    return int(num_string[-1]) + int(digit_sum(num_string[:-1]))

def is_prime(n):
    if n <= 1:
        return False
    if is_prime_helper(n, (int(n**0.5))):
        return True
    return False

def is_prime_helper(n, g):
    if g == 1:
        return True
    if n < 2 or n % g == 0:
        return False
    return is_prime_helper(n, g - 1)


def play_hanoi(hanoi,n,src,dest,temp):
    if n==1:
        hanoi.move(src,dest)
    else:
        play_hanoi(hanoi, n-1, src, temp, dest)
        play_hanoi(hanoi, 1, src, dest,temp)
        play_hanoi(hanoi, n-1, temp, dest, src)



def print_sequences(char_lst,n):
    print_sequences_helper(char_lst, "", n)

def print_sequences_helper(char_lst, option, n):
    if n==0:
        print(option)
        return
    for letter in range(len(char_lst)):
        a = str(char_lst[letter])
        option = option + a
        print_sequences_helper(char_lst, option, n - 1)
        option = option[:-1]

def print_no_repetition_sequences(char_lst,n):
    print_no_repetition_sequences_helper(char_lst,"", n)

def print_no_repetition_sequences_helper(char_lst, option, n):
    if n==0:
        print(option)
        return

    for index in range(len(char_lst)):
        the_letter = char_lst[index]
        a = str(the_letter)
        option = option + a
        char_lst.remove(the_letter)
        print_no_repetition_sequences_helper(char_lst, option, n-1)
        char_lst.insert(index,the_letter)
        option = option[:-1]


lst_to_print = []

def parentheses(n):
    parentheses_helper(["(", ")"], 0, n)
    return lst_to_print

def parentheses_helper(base_stone, indicator, n):
    x1,x2= "(",")"
    if len(base_stone) == n*2:
        list_to_str = "".join(i for i in base_stone)
        lst_to_print.append(list_to_str)
        return

    for i in range(indicator, len(base_stone)):
        base_stone.insert(i + 1, x2)
        base_stone.insert(i + 1, x1)
        parentheses_helper(base_stone, i + 1, n)
        base_stone.pop(i + 1)
        base_stone.pop(i + 1)

def flood_fill(image,start):
    if image[start[0]][start[1]]== "*":
        return
    image[start[0]][start[1]] = "*"
    flood_fill(image, (start[0],start[1]-1))
    flood_fill(image, (start[0], start[1] +1))
    flood_fill(image, (start[0]-1, start[1]))
    flood_fill(image, (start[0]+1, start[1]))