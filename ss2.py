a = int(input("Введите значение  10СС: "))
ss = int(input("Введите СС, в которую хотите перевести число: "))

last = []
a = int(a)


def check(num1):
    if num1 < 10:
        list.append(str(num1))
    else:
        num1 = chr(num1 + 55)
        print(num1)
        list.append(num1)

def lasting(ar):
    ar.reverse()
    ar = "".join(ar)
    print(ar)


if a <= ss and a < 10:
    last += str(a)
else:
    b = a // ss
    num1 = a % ss
    
    if ss <= 10:
        last.append(str(num1))
        while b >= ss:
            num1 = b % ss
            b //= ss
            last.append(str(num1))
        else:
            last.append(str(b))
            lasting(last)
    else:
        list = []
        check(num1)
        while b >= ss:
            if b < 10:
                num1 = b % ss
                b //= ss
                list.append(str(num1))
            else:
                num1 = b % ss
                b //= ss
                check(num1)
        else:
            if b < 10:
                list.append(str(b))
            else:
                pass
            lasting(list)