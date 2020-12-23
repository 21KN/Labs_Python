#2 Тема: Умовні оператори.
# Питання: Операції відношень. Логічні операції. Приоритет операцій. Логічний тип даних. Умовний оператор. Каскадне розгалуження. Тернарний умовний оператор.
# Завдання: ст. 42-44. № 2.9, 2.17, 2.18, 2.19, 2.23-2.26

# 2.9 Скласти програму перевірки належності точки площини (𝑥, 𝑦) до
# зафарбованої області
print("Введіть координати точки площини: ")
x = float (input("X = "))
y = float (input("Y = "))

print("Точка (",x,",",y,")",end="")

if y >= x and y >= -x and y <= 1 :
  print(" належить")
else :
  print(" не належить")

input("Натисніть Enter для закінчення")


print("Введіть координати точки площини: ")
x = float (input("X = "))
y = float (input("Y = "))

condition = y <= 1 and y >= -1 and x <= 1 and x >=-1

result = "належить" if condition else "не належить"
print("Точка (",x,",",y,")", result)

input("Натисніть Enter для закінчення")


print("Введіть координати точки площини: ")
x = float (input("X = "))
y = float (input("Y = "))

condition = y <= 1 and x <= 2 and y >= 0 and x >= 0

result = "належить" if condition else "не належить"
print("Точка (",x,",",y,")", result)

input("Натисніть Enter для закінчення")



print("Введіть координати точки площини: ")
x = float (input("x = "))
y = float (input("y = "))

condition = x*x + y*y <= 4 and y <= -x+2 and y >= x-2 and x >= 0

result = "належить" if condition else "не належить"
print("Точка (",x,",",y,")", result)

input("Натисніть Enter для закінчення")


print("Введіть координати точки площини" )
x = float (input(x = ))
y = float (input(y = ))

condition = not(x=0 and y=0) and ("xx + yy =4) and -2=x=2 and -2=y=2

result = "належить" if "condition" else "не належить"
print("Точка" ('',x,'','',y,), "result")

input("nНатисніть Enter для закінчення")


print("Введіть координати точки площини: ")
x = float (input("x = "))
y = float (input("y = "))

condition = x*x + y*y <= 4 and ( y <= abs(x)-2 or y >= -abs(x)+2 )

result = "належить" if condition else "не належить"
print("Точка (",x,",",y,")", result)

input("\nНатисніть Enter для закінчення")

# 2.17 Перевірити, чи існує трикутник із заданими сторонами 𝑎,𝑏,𝑐. Якщо так, то визначити, який він:
# a) гострокутний;
# b) прямокутний;
# c) тупокутний.


print("Введіть довжину кожної із сторін трикутника: ")
a = float (input("Сторона A = "))
b = float (input("Сторона B = "))
c = float (input("Сторона C = "))

exist = a+b>c and a+c>b and b+c>a
right = a*a+b==c*c or a*a+c*c==b*b or b*b+c*c==a*a
sharp = a*a+b*b>c*c and a*a+c*c>b*b and b*b+c*c>a*a
obtuse = a*a+b*b<c*c or a*a+c*c<b*b or b*b+c*c<a*a

result = "Трикутник зі сторонами "+str(a)+" , "+str(b)+" , "+str(c)


if exist:
  result += " існує і є "
  if right:
    result += " прямокутний "
  if sharp:
    result += " гострокутний "
  if obtuse:
    result += " тупокутний "
else:
  result += " не існує"
print(result)

input("\nНатисніть Enter для закінчення")

# 2.18 Визначити, скільки розв’язків має рівняння та розв'язати його:
# a) 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0;
# b) 𝑎𝑥4 + 𝑏𝑥2 + 𝑐 = 0.
class CheckRes:
    pass

# 2.19 Визначити, скільки розв’язків має система рівнянь і розв'язати її:
# a) {𝑎1𝑥+𝑏1𝑦+𝑐1 =0, 𝑎2𝑥+𝑏2𝑦+𝑐2 =0;
# b){|𝑥|+|𝑦|=1, 𝑎𝑥+𝑏𝑦+𝑐=0.
class CheckResT:
    pass

# 2.23 За літерою-цифрою 𝑑 визначити назву цієї цифри.
a = input("Введіть цифру: ")
a = int(a)
l = ["нуль", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять"]

if a==0:
  print(l[0])
elif a==1:
  print("Це цифра " + l[1])
elif a==2:
  print("Це цифра " + l[2])
elif a==3:
  print("Це цифра " + l[3])
elif a==4:
  print("Це цифра " + l[4])
elif a==5:
  print("Це цифра " + l[5])
elif a==6:
  print("Це цифра " + l[6])
elif a==7:
  print("Це цифра " + l[7])
elif a==8:
  print("Це цифра " + l[8])
elif a==9:
  print("Це цифра " + l[9])
elif a>9:
  print("Число більше одноцифрового")
elif a<0:
  print("Число мінусове")

input("Натисніть Enter для закінчення")

# 2.26 Задано тризначне натуральне число.
# Записати його словами, вважаючи, що це число означає деяку суму грошей
# (у гривнях або іншій валюти). Наприклад, для числа 256 треба записати "двісті п’ятдесят шість гривень".
class InTNum:
    pass


# 2.24
i = input("Введіть номер місяця: ")
i = int(i)

if i == 1 or i == 3 or i == 5 or i == 7 or i == 9 or i == 11:
  print("У цьому місяці 31 день")
elif i == 4 or i == 6 or i == 8 or i == 10 or i == 12:
  print("У цьому місяці 30 днів")
elif i == 2:
  print("У цьому місяці 28 днів")

input("Натисніть Enter для закінчення")

# 2.25
i = input("Введіть число: ")
i = int(i)

n1 = " грибів"
n2 = " гриб"
n3 = " гриба"

if i==0:
  print("Ми знайшли " + str(i) + n1 + " у лісі")
elif i%100>=10 and i%100<=20:
  print("Ми знайшли " + str(i) + n1 + " у лісі")
elif i%10==1:
  print("Ми знайшли " + str(i) + n2 + " у лісі")
elif i%10>=2 and i%10<=4:
  print("Ми знайшли " + str(i) + n3 + " у лісі")
else:
  print("Ми знайшли " + str(i) + n1 + " у лісі")

input("Натисніть Enter для закінчення")