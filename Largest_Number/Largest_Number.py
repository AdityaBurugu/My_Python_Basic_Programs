A = int(input('Firsr Number = '))
B = int(input('Second Number = '))
C = int(input('Third Number = '))
if(A > B and A> C):
    Largest = A
elif(B > A and B > C):
    Largest = B
else:
    Largest = C

print(Largest,'is the largest among the given data')