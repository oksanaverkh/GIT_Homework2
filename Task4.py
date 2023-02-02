# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
import random
os.system('cls')

def list_creation(num, limit):
    new_list = []
    for _ in range(num+1):
        new_list.append(random.randint(0, 100))
    print('List of coefficients:', new_list)
    return new_list

def check():
    k = int(input('Enter degree K: '))
    while not 0<=k<=100:
        print('Wrong value, try again')
        k = int(input('Enter degree K: '))
    return int(k)

def main():
    k = check()    
    coef_list = list_creation(k, 100)
    with open('polynomial.txt', 'w') as data:
        for i in range(k+1):
            if coef_list[i]==0:
                continue
            elif coef_list[i]==1:
                data.write(f' x^{k-i} +')
            elif (k-i)==1:
                data.write(f' {coef_list[i]*1}x +')
            elif (k-i)==0:
                data.write(f' {coef_list[i]*1}')
            else:
                data.write(f' {coef_list[i]}x^{k-i} +')
        data.write(' = 0')

if __name__ == "__main__":
    main()