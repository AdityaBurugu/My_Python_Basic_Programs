def Prime(LowerLimit,UpperLimit):
    L = LowerLimit
    U = UpperLimit
    Prime = []
    if LowerLimit<UpperLimit and LowerLimit>0 and UpperLimit>0:
        print('Finding Prime Numbers and Sum of Prime Numbers in a given Range')
        for N in range(L, U + 1):
            Factors = 0
            for Divisor in range(1, N + 1):
                if (N % Divisor == 0):
                    Factors += 1
            if (Factors == 2):
                print(N, 'is a prime number')
                Prime.append(N)
        print('The sum of Prime Numbers Between {:d} to {:d} is {:d}'.format(L, U, sum(Prime)))
        print('Program Finished')
        print('Thank You')
    elif LowerLimit>=UpperLimit:
        print("Lower Limit Should be less than Upper Limit")
    elif LowerLimit<0 and UpperLimit<0:
        print("Invalid Lower & Upper Limit Input")
    elif LowerLimit<0:
        print("Invalid Lower Limit Input")
    elif UpperLimit<0:
        print("Invalid Upper Limit Input")
Prime(10,100)