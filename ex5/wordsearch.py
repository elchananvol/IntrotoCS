import sys
import os



def right(lsts):
    lstsToreturn =[]
    for lst in range(len(lsts)):
        a = "".join(i for i in lsts[lst])
        lstsToreturn.append(a)
    return lstsToreturn
#print(right(lsts))

def reverse(lsts):
    reversed_lsts=[]
    for lst in range(len(lsts)):
        reversed_lsts.append(lsts[lst][::-1])
    return reversed_lsts
#print(reverse(right(lsts)))

def down(lsts):
    new=[]
    for i in range(len(lsts[0])):
        a = "".join(lsts[j][i] for j in range(len(lsts)))
        new.append(a)
    return new
#print(down(lsts))

#print(reverse(down(lsts)))
def one_list(lsts):
    b = []
    for lst in range(len(lsts)):
        for i in lsts[lst]:
            b.append(i)
    return b


def diagonal_right(lsts):
    lst = one_list(lsts)
    index_list = list(i for i in range(len(lsts[0])))
    for i in range(1,len(lsts)):
        if len(lsts[0]) != 0:
            index_list.append(i*len(lsts[0]))
    #print(index_list)

    stop_list= list((i*len(lsts[0])-1) for i in range(1,len(lsts)))

    diagonal_right_lst=[]
    for i in index_list:
        indicator = i
        loop_list = [lst[indicator]]
        while indicator < (len(lst)-len(lsts[0]) - 1) and not indicator in stop_list:
            indicator = len(lsts[0]) + 1 + indicator
            loop_list.append(lst[indicator])
        diagonal_right_lst.append(loop_list)
    diagonal_right_lst = right(diagonal_right_lst)
    return diagonal_right_lst

def diagonal_left(lsts):
    f = reverse(lsts)

    f= diagonal_right(f)
    return f


def find_word(lst, word):
    times = 0
    for i in lst:
        for t in range(len(i)):
            if i.find(word, t) == t:
                times += 1
    return word, times


def find_words_in_matrix(word_list,matrix,directions):
    #print(len(matrix))
    if len(matrix)== 0:
        return []
    d = down(matrix)
    u = reverse(d)
    r = right(matrix)
    l = reverse(r)
    y = diagonal_right(matrix)
    z = diagonal_left(matrix)
    w = reverse(z)
    x = reverse(y)
    dict_direction = {"d": d,"u": u, "r":r, "l":l, "y":y, "z":z, "w":w, "x":x}
    reshima = []
    check_list =[]
    for letter in directions:
        if (not letter in check_list):
            check_list.append(letter)
            reshima += dict_direction[letter]
    reshima_sofit = []
    for word in word_list:
        conclusion = find_word(reshima, word)
        if conclusion[-1] != 0:
            reshima_sofit.append(conclusion)
    return reshima_sofit
#from datetime import datetime
#start= datetime.now()
#asd= ["raw","red","blue","move","gum","son","shoe","she","dog","PoP","ai","P"]
#print(find_words_in_matrix(asd,[["P"]],"durlwxyz"))
#end = datetime.now()
#print(f"the time is {end-start}")

def main():
    args= sys.argv[1:]
    if check_input_args(args) is None:
        word_list = read_wordlist_file(args[0])
        matrix = read_matrix_file(args[1])
        results = find_words_in_matrix(word_list,matrix,args[3])
        #print (results)
        write_output_file(results,args[2])

def check_input_args(args):
    if len(args) != 4:
        return "the command inserted in wrong way"
    a = os.path.isfile(args[0])
    b = os.path.isfile(args[1])
    if not a:
        return "word file doesn't exist"
    if not b :
        return "matrix file doesn't exist"
    for i in range(len(args[3])):
        directions_list = "udrlwxyz"
        if not args[3][i] in directions_list:
            return "there letter in the directions that not permitted"

def read_wordlist_file(filename):
    f = open(filename, "r")
    word_list = list(i[:-1] for i in f)
    f.close()
    return word_list

def read_matrix_file(filename):
    f = open(filename, "r")
    matrix_lst = list(i[:-1].split(",") for i in f)
    f.close()
    return matrix_lst

def write_output_file(results,output_filename):
    f = open(output_filename, "w")
    if len(results) != 0:
        f.write(results[0][0] + "," + str(results[0][1]))
        for i in results[1:]:
            f.write('\n' + i[0] + "," + str(i[1]))
    f.close()


if __name__ == '__main__':
    main()


