from random import randint


N=20 # Колл-во чисел
countot=0 #Счётчик положительных чисел
countpol=0 # Счётчик отрицательных чисел



n=[randint(-100,100) for i in range (N)]
print(n)

print("Максимальное число: ",max(n))
print("Минимальное число: ",min(n))

print('кол-во положительных чисел:', sum(b > 0 for b in n))
print('кол-во отрицательных чисел:', sum(b < 0 for b in n))
print('кол-во нулей:', sum(b == 0 for b in n))
