
import os
import math
from wave_helper import *

def read_file(file):
    lineList = [line.rstrip('\n') for line in open(file)]
    lst_to_return = []
    for lst in range(len(lineList)):
        for i in lineList[lst]:
            if i != " ":
                lst_to_return.append(i)
    return lst_to_return

def second_choise(data_list,frame_rate):
    second_choice = 0
    while second_choice != "7":
        print("options: \n1. reverse the audio. \n2. faster. \n3. slower. \n4. boost volume.\n5. lower volume.\n6. low pass filter.\n7. exit")
        second_choice = input("enter ur choice:")

        if second_choice == "1":
            data_list.reverse()
            msg = "the order is reversed now"
        elif second_choice == "2":
            data_list = data_list[::2]
            msg = "the record is faster now"
        elif second_choice == "3":
            new_lst = []
            for i in range(0, len(data_list) - 1):
                a = [int((data_list[i][0] + (data_list[i + 1][0])) / 2),
                     ((data_list[i][1] + (data_list[i + 1][1])) / 2)]
                new_lst.append(data_list[i])
                new_lst.append(a)
            new_lst.append(data_list[-1])
            data_list = new_lst
            msg = "the audio is slowler right now"
        elif second_choice == "4":
            for i in range(len(data_list)):
                data_list[i] = [int(data_list[i][0] * 1.2), int(data_list[i][1] * 1.2)]
                if data_list[i][0] > 32767:
                    data_list[i][0] = 32767
                if data_list[i][1] > 32767:
                    data_list[i][1] = 32767
                if data_list[i][0] < -32768:
                    data_list[i][0] = -32768
                if data_list[i][1] < -32768:
                    data_list[i][1] = -32768
            msg = "the volume is stronger right now"
        elif second_choice == "5":
            for i in range(len(data_list)):
                data_list[i] = [int(data_list[i][0] / 1.2), int(data_list[i][1] / 1.2)]
            msg = "the volume is lower right now"
        elif second_choice == "6":
            lst_to_return = []
            for i in range(0, len(data_list)):
                if i == 0 or i == len(data_list) - 1:
                    a = [data_list[0], data_list[1]]
                    if i == (len(data_list) - 1):
                        a = [data_list[-2], data_list[-1]]
                    b = int((a[0][0] + a[1][0]) / 2)
                    lst_to_return.append([b,b])
                else:
                    a = [data_list[i - 1], data_list[i], data_list[i + 1]]
                    b = [int((a[0][0] + a[1][0] + a[2][0]) / 3), int((a[0][0] + a[1][0] + a[2][0]) / 3)]
                    lst_to_return.append(b)
            data_list = lst_to_return
            msg = "audio is muffled right now"
        elif not second_choice in ["1","2","3","4","5","6","7"]:
            msg = "the letter u enetred is invalid"
        elif second_choice == "7":
            file_name_to_save= input("enter file name to save:")
            save_wave(frame_rate, data_list, file_name_to_save)
            msg = "the file saved"
        print(msg)



def main():
    choice =  0
    print("wellcome to global system ltd...")
    while choice != "3":
        print("u have three options \n1. change wav file \n2. compose melody into wav file\n3. exit")
        choice = input("enter ur choice:")
        if choice == "1":
            file_name = input("enter file name:")
            check = load_wave(file_name)
            while check == -1:
                print("the file u entered is not existed.. try again until you succeed or die")
                file_name = input("enter file name:")
                check = load_wave(file_name)
            frame_rate, data_list = load_wave(file_name)
            second_choise(data_list,frame_rate)



        elif choice =="2":
            file_name = input("enter instruction file name:")
            input_comp = read_file(file_name)
            while input_comp == -1:
                print("the file name u entered is not existed.. try again until you succeed or die")
                file_name = input("enter instruction file name:")
                input_comp = read_file(file_name)


            dict_cordes = {"A": 440, "B": 494, "C": 523, "D": 587, "E": 659, "F": 698, "G": 784, "Q": 0}
            lst_to_return = []
            for i in range(len(input_comp)):
                if (i + 1) % 2 == 0 or len(input_comp) == 1:
                    continue
                else:
                    SAMPLE_RATE = 2000
                    MAX_VOLUME = 32767
                    samples_per_cycle = 1
                    if input_comp[i] != "Q":
                        samples_per_cycle = SAMPLE_RATE / dict_cordes[input_comp[i]]
                    for j in range(int(input_comp[i + 1]) * 125):
                        value = int(MAX_VOLUME * math.sin(math.pi * 2 * j / samples_per_cycle))
                        if input_comp[i] == "Q":
                            value = 0
                        lst_to_return.append([value, value])
            second_choise(lst_to_return,2000)

        elif choice not in ["1","2","3"]:
            print("the letter u enetred is invalid")
    print("goodbye")




if __name__=="__main__":
    main()


















#frame_rate = [[1, 2], [3, 4]]
#print(frame_rate.reverse())