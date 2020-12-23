# 2.9(ґ) Скласти програму перевірки належності точки площини (𝑥, 𝑦) до
# зафарбованої області (рис. 2.1.)

print("Введіть координати точки площини: ")
x = float (input("x = "))
y = float (input("y = "))

condition = x*x + y*y <= 4 and ( y <= abs(x)-2 or y >= -abs(x)+2 )

result = "належить" if condition else "не належить"
print("Точка (",x,",",y,")", result)

input("\nНатисніть Enter для закінчення") 