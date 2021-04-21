#1 задание 
a = 1
b = 2
c = a + b
print(c)

d = int(input("Введите число: "))
print(d)
e = str(input("Введите слово: "))
print(e)


#2 задание 

a = int(input("Введите время в секундах: "))
hours = a // 3600
minutes = (a - hours * 3600) // 60
seconds = a - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

#3 задание

n = int(input("Введите число: "))
sum = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(sum)

#4 задание

a = int(input("Введите целое положительное число "))
max = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max:
        max = a % 10
    elif a > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

#5 задание

a = float(input("Введите выручку фирмы "))
b = float(input("Введите издержки фирмы "))
if a > b:
    print(f"Фирма отработала с прибылью. Рентабельность выручки: {a / b}")
    c = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника: {a / c}")
elif a == b:
    print("Фирма отработала в ноль")
else:
    print("Фирма отработала в убыток")

#6 задание

a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        c = a + 0.1 * a
        result_days += 1
        result_km = result_km + (c - a)
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)