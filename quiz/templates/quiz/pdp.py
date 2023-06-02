a = str(input("Enter the number: "))

sumNum = 0
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        print(f"{i}, juftson: {str(a[i])}")
        sumNum += int(a[i])
print(sumNum)        