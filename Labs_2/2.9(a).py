﻿# 2.9(a) Скласти програму перевірки належності точки площини (𝑥, 𝑦) до
# зафарбованої області (рис. 2.1.)

print("Введіть координати точки площини: ")
x = float (input("X = "))
y = float (input("Y = "))

print("Точка (",x,",",y,")",end="")

if y >= x and y >= -x and y <= 1 :
  print(" належить")
else :
  print(" не належить")

input("Натисніть Enter для закінчення")  
