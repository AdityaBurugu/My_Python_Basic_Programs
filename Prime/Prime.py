print('Finding Prime Numbers and Sum of Prime Numbers in a given Range')
L = int(input('Enter the Minimum Range: '))
U = int(input('Enter the Maximum Range: '))
Prime = []
for N in range(L,U+1):
    Factors = 0
    for Divisor in range(1,N+1):
        if (N % Divisor == 0):
            Factors+=1
    if(Factors == 2):
        print(N,'is a prime number')
        Prime.append(N)
print('The sum of Prime Numbers Between {:d} to {:d} is {:d}'.format(L,U,sum(Prime)))
print('Program Finished')
print('Thank You')