a = int(input("Введите число: "))

sum=0

lenA = len(str(a))

for i in range(1,lenA+1):
    num = 10**i
    num2 = 10**(i-1)
    aN = (a%num - a%num2) / (num2)

    sum+=aN
    
    if i == lenA:
        print("Длина числа", a, "равна:", lenA)
        print("Сумма всех цифр числа", a, "равна:", sum)