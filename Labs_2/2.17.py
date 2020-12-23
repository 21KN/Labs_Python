# 2.17. Перевірити, чи існує трикутник із заданими сторонами 𝑎, 𝑏, 𝑐.
# Якщо так, то визначити, який він:


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