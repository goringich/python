lst = [int(item) for item in input().split()]
lst2 = [item for item in input().split()]
edNol = int(input())

sum = []
lstN = 0
ot = 0

for i in range(len(lst)):
    if lst2[i] == "-":
        lstN -= 2**lst[i]
    else:
        lstN += 2**lst[i]

arr = []
while lstN > 0:     
    arr.append(lstN%2)
    lstN = lstN//2

arr.reverse()
for i in range(len(arr)):
    if arr[i] == edNol:
        ot+=1
    else:
        pass
print(ot)
        
#6042 614 5 4 1 0
# + - + + - -

