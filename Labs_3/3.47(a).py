# 3.47. Скласти програму для обчислення суми перших 𝑛 членів:
# a) послідовності Фібоначчі;

k = m = 1
element = input("Введіть номер елементу: ")
element = int(element)
for n in range(int(element-2)):
    tmp = k + m
    k = m
    m = tmp
print(str(element)+" елемент послідовності дорівнює " + str(m))

input("Натисніть Enter для завершення програми")