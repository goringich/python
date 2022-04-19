import string

a = int(input("Введите число: "))
ss = int(input("Введите СС, в которую хотите перевести число: "))

b = a // ss #первое деление
num1 = a % ss #первый остаток

alf = list(string.ascii_uppercase) #алфавит, длина 26

def bukv(num):
    for l in range (0, len(alf)-1):
        if int(num) - 10 == l:
            numN = alf[l]
            return numN
        else:
            pass
        
        
if num1 >= 10 and num1 < ss:
    num1 = bukv(num1)
    print("bukva", num1)
    last = str(num1) #первый остаток в строке
    
else:
    print(b)
    last = str(num1) #первый остаток в строке


while b >= ss:
    print("b > ss")
    
    for i in range(1,100):
        if b >= ss:
            num = b % ss
            if num >= 10:
                num = bukv(num)
            b //= ss
            last += str(num)
#         elif b >= 10 and b < ss:
#             num = bukv(b)
#             print("буква последняя", num)
#             last += str(num)
#             
        if b >= 10 and b < ss:
            num = bukv(b)
            print("буква последняя", num)
            last += str(num)

        else:
            last += str(b)
            
            
        b //= ss
else:
    print("b <= ss", b)
    if b >= 10 and b < ss:
        num = bukv(b)
        print("буква последняя", num)
        last += str(num)
    else:
        last += str(b)

    
#переворачиваем
last = last[::-1]
ar = list(last)
for i in range(len(ar)):
    if ar[0] == "0":
        ar.pop(0)
last = ''.join(ar)
    
print(last)
