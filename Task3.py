# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
import random
import math
os.system('cls')

def list_creation(n, limit):
    new_list = []
    for _ in range(n):
        new_list.append(random.randint(-limit, limit))
    return new_list

def unique_list(new_list):
        non_repeat_list = []
        for i in range(len(new_list)):
            if new_list.count(new_list[i])==1:
                non_repeat_list.append(new_list[i])
        return non_repeat_list

def main():    
    n = abs(int(input('Enter list length: ')))
    limit = abs(int(input('Enter list limit value: ')))
    my_list = list_creation(n, limit)
    print(my_list)
    print(unique_list(my_list))

if __name__ == "__main__":
    main()

# import random

# def get_arr(num):              
#     my_L = []
#     for i in range(num):
#         my_L.append(random.randint(1,10))
#     return my_L

# def del_el (in_L):
#     temp = []
#     i = 0
#     while i < len(in_L)-1:
#         if in_L[i] in in_L[i+1:]:
#             temp.append(in_L[i])
#         i=i+1
#     return (list(set(in_L) - set(temp)))

# def main():
#     number = int(input('введите размер списка '))
#     arr = get_arr(number)
#     print(arr) 
#     print(del_el(arr))
     

# if __name__ == "__main__":
# 	main()
