#############################################################

# LOGIN : volberstan

# ID NUMBER : 206136749

# WRITER : elchanan volbersten

##############################################################


def input_list():
    lst = []
    x = 0
    sum = 0
    while x  != "":
        x = input()
        if x != "":
            lst.append(int(x))
            sum += int(x)
    lst.append(sum)
    return lst



def inner_product(vec_1, vec_2):
    result = 0
    if len(vec_1) != len(vec_2):
        return
    else:
        for i in range(0, len(vec_1)):
             q= vec_1[i] * vec_2[i]
             result += q
        return result


def sequence_monotonicity(sequence):
    q1 = q2= q3 =q4 =1
    if  1>= len(sequence):
        return [True,True,True,True]
    else:
        for i in range(0, len(sequence) - 1):
            if sequence[i] <= sequence[i + 1] and q1 != False:
                q1= True
            else:
                q1= False
            if sequence[i] < sequence[i + 1] and q2 != False:
                q2 = True
            else:
                q2 = False
            if sequence[i] >= sequence[i + 1] and q3 != False:
                q3 = True
            else:
                q3 = False
            if sequence[i] > sequence[i + 1] and q4 != False:
                q4 = True
            else:
                q4 = False
    return [q1,q2,q3,q4]



def monotonicity_inverse(def_bool):
    if def_bool == sequence_monotonicity([1,2,3,4]):
        return [1, 2, 3, 4]
    elif def_bool == sequence_monotonicity([1,3,3,4]):
        return [1, 3, 3, 4]
    elif def_bool == sequence_monotonicity([4,3,2,1]):
        return [4,3,2,1]
    elif def_bool == sequence_monotonicity([4, 2, 2, 1]):
        return [4, 2, 2, 1]
    elif def_bool == sequence_monotonicity([4, 2, 3, 1]):
        return [4, 2, 3, 1]
    elif def_bool == sequence_monotonicity([4, 4, 4, 4]):
        return [4, 4, 4, 4]
    else:
        return

def primes_for_asafi(n):
    divisor = 2
    check_mun = 3
    counter = 1
    lst= [2]
    while counter < n:
        while divisor < check_mun:
            if check_mun % divisor != 0:
                 divisor += 1
            else:
                check_mun += 1
                divisor = 2
        counter += 1
        lst.append(check_mun)
        check_mun += 1
        divisor = 2
    return lst


def sum_of_vectors(vec_lst):
    lst=[]
    h=0
    if vec_lst != []:
        for i in range(len(vec_lst[0])):
            for j in range(len(vec_lst)):
                 x= vec_lst[j][i]
                 h += x
            lst.append(h)
            h = 0
    else:
        return

    return lst


def num_of_orthogonal(vectors):

    counter = 0
    num_of_orthogonal_lists= 0
    
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if j != i:
                result = 0
                for t in range(len(vectors[0])):
                        counter = vectors[i][t] * vectors[j][t]
                        result += counter
                if result == 0:
                     num_of_orthogonal_lists +=1
            else:
                j +=1


    return int(num_of_orthogonal_lists/2)