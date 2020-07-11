x=int(input('Enter the value: '))
L=int(input('Enter the Minimum Range: '))
U=int(input('Enter the Maximum Range: '))
Multiples = []
for i in range(L,U+1):
    if(i % x ==0):
        Multiples.append(i)
print(Multiples)