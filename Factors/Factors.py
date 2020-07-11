x = int(input('Enter the value: '))
Factors = []
for i in range(1,x+1):
    if (x % i == 0):
        Factors.append(i)
print(Factors)