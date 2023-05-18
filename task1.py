# Задача 26: Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiation(a, b) -> int:
    if b == 0:
        return 1
    elif b % 2 == 0:
        return exponentiation(a * a, b // 2)
    else:
        return a * exponentiation(a, b - 1)
    

a = int(input('Введите первое число > '))
b = int(input('Введите второе число > '))

print(f"{a} в степени {b} равно {exponentiation(a, b)}")