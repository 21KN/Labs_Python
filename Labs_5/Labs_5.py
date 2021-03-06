# Тема: Списки.
# Питання: Впорядковані колекції. Список. 3 способи створення списків. Індексація. Поелементна робота зі списком. Зрізи. Операції над списками. Введення списків з клавіатури. Обхід списку: ітеруванням, за індексами, за допомогою функції enumerate. Моделювання роботи з матрицями.
# Завдання: ст. 102. № 4.1 a)-c), 4.2 a) b), 4.12, 4.13.

# 4.1 Дано список натуральних чисел. Знайти кількість:
# a) парних компонент;
# b) компонент,що діляться на 3 або 5;
# c) нульових компонент;


num_a = 0
num_b = 0
num_c = 0
list = [5, 7 , 0, 1, 12, 7, 8, 3, 3]

for i in list:
    n = i
    while n > 0:
        n -= 2
    if n == 0:
        num_a += 1
    n = i
    while n > 0:
        n -= 3
    if n == 0:
        num_b += 1
    elif n == 5:
        num_b += 1
    n = i
    if n == 0:
      num_c += 1

print("Кількість парних компонентів: " + str(num_a))
print("Кількість компонентів, що діляться на 3 або 5: " + str(num_b))
print("Кількість нульових компонентів: " + str(num_c))

input("Натисніть Enter для завершення")


# 4.2. Дано список натуральних чисел. Використовуючи оператор створення
# списку, побудувати список, що містить:
# a) всіпарніелементизаданогосписку;
# b) всі елементи заданого списку, що є повними квадратами;


list = [i for i in range(10)]
list_a = []
for i in range(0,len(list),2):
  list_a.append(list[i])
list_b = [i**2 for i in list]
print("Список а: " + str(list_a))
print("Список б: " + str(list_b))

input("Натисніть Enter для завершення")


# 4.12. Дано два впорядкованих списки. Не використовуючи функцію
# сортування, об'єднати ці списки у один впорядкований список.


a = [1,2,3,4,5,6]
b = [7,8,9,10,11,12]
new_list = []
d = a + b
while d:
  new_list.append(d.pop(d.index(min(d))))
print(new_list)

input("Натисніть Enter для завершення")


# 4.13. Дано список, що складається з коефіцієнтів многочлена
# 𝑃𝑛(𝑥)=𝑎0 ∗𝑥𝑛 +𝑎1 ∗𝑥𝑛−1+...+𝑎𝑛−1 ∗𝑥+𝑎𝑛
# Обчислити:
# a) значення многочлена при заданому значенні х;
# b) похідноївідмногочленапризаданомузначенніх;
# c) інтеграла від много члена 𝑃𝑛 (𝑥) на заданому відрізку.


x = int(input("Ввеліть х: "))
n = int(input("Введіть n: "))
list = [i * x**n for i in range(n)]
print(list)

input("Натисніть Enter для завершення")
