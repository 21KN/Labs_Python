# 1.   Тема: Лінійні програми.

# Питання: Основні правила синтаксису. Види змінних величин. Типи даних. Коментарі.
# Тотожна інструкція. Присвоєння. Введення / виведення.
# Оператор підстановки %. Арифметичні операції. Бібліотека math. Комплексні числа.
# Завдання: ст. 27. № 1.2,  1.5, 1.7, 1.9, 1.24

import math
import cmath

i = 1j
pi = math.pi
z = cmath.exp(i * pi)

# 1.2 Дано натуральне тризначне число. Знайти суму цифр цього числа.
class ThreeDigitNumber:
    def Fold(self):

        n = input("Введите трехзначное число: ")
        n = int(n)

        d1 = n % 10
        d2 = n % 100 // 10
        d3 = n // 100

        print("Сумма цифр числа:", d1 + d2 + d3)


ThreeDigitNumber.Fold(self=0)

# 1.5 Обчислити значення многочлена для введеного з клавіатури комплексного числа 𝑧:
# a)𝑓(𝑧)=4𝑧4 +3𝑧3 +2𝑧2 +𝑧+1;
# b)𝑓(𝑧)=𝑧4 +2𝑧2 +1;

class ValueOfThePolynomial:
    pass

# 1.7 Вивести на екран текст:
# a) a a a
# b)
# a-------a
# aa |a| a a a-------a
# a
# де a – введена з клавіатури цифра.

class DisplayText:
    def printText(self):
        print('')



# 1.9 Дано натуральне тризначне число. Знайти:
# a) число одиниць, десятків і сотень цього числа;
# b) число, утворене при прочитанні заданого числа справа наліво.

class GivenANaturalThreeDigitNumberToFind:
    pass

