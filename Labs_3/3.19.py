# 3.19. Створити програму, яка з’ясовує, чи входить задана цифра до
# запису заданого натурального числа.

a = int(input("Введіть число: "))
b = int(input("Введіть цифру: "))
for i in str(a):
    if i == str(b):
        print("Цифра входить до заданого числа")

input("Натисніть Enter для завершення")