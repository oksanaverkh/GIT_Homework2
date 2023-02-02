# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os
import random
os.system('cls')

def check():
    d = int(input('Enter d: '))
    while not 1<=d<=10:
        print('Wrong value, try again')
        d = int(input('Enter d: '))
    return int(d)

def main():    
    accuracy = check()
    d = 10**(-accuracy)
    print(f'd = %.{accuracy}f'%d)
    print(f'10 / 3 = {round(10/3,accuracy)}')


if __name__ == "__main__":
    main()