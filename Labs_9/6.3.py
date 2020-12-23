# 6.8. Задано рядок, що складається з латинських (українських) літер. 
# Надрукувати всі літери, що
# a) входять до рядка по одному разу;
# b) входять до рядка не менше двох раз;
# c) не входять до рядка.

alphabet = "abcdefghijklmnopqrstuvwxyz"
string = "abcddeeffgh"
list_a = []
list_b = []
list_c = []
count = 0
for i in string:
    for j in string:
        if i == j:
            count += 1
    if count == 1:
        list_a.append(i)
    if count >= 2:
        list_b.append(i)
    count = 0

for alpha in alphabet:
    if alpha not in string:
        list_c.append(alpha)


print(list_a)
print(list_b)
print(list_c)

input("Натисніть Enter для завершення")    