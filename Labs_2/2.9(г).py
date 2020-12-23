# 2.9(г) Скласти програму перевірки належності точки площини (𝑥, 𝑦) до
# зафарбованої області (рис. 2.1.)

print("Введіть координати точки площини: ")
x = float (input("x = "))
y = float (input("y = "))

condition = x*x + y*y <= 4 and y <= -x+2 and y >= x-2 and x >= 0

result = "належить" if condition else "не належить"
print("Точка (",x,",",y,")", result)

input("Натисніть Enter для закінчення") 