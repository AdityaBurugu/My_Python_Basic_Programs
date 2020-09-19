#Sum and Average of Odd Numbers and Sum and Average of Even Numbers.
def Odd_Even(LowerLimit,UpperLimit):
    L = LowerLimit
    U = UpperLimit
    Even_Numbers = []
    Odd_Numbers = []
    Even_sum = 0
    Even_numbers = 0
    Odd_sum = 0
    Odd_numbers = 0
    for i in range(L, U + 1):
        if (i % 2 == 0):
            Even_Numbers.append(i)
            Even_sum += i
            Even_numbers += 1
        elif (i % 2 != 0):
            Odd_Numbers.append(i)
            Odd_sum += i
            Odd_numbers += 1
    print(Even_sum, 'is the sum of Even Numbers from', L, 'to', U)
    print(Odd_sum, 'is the sum of Odd numbers from', L, 'to', U)
    print('There are', Even_numbers, 'Even Numbers from', L, 'to', U)
    print("Even Numbers from", L, 'to', U, 'are', Even_Numbers)
    print('There are', Odd_numbers, 'Odd Numbers from', L, 'to', U)
    print("Odd Numbers from", L, 'to', U, 'are', Odd_Numbers)
    Average_Even = Even_sum / Even_numbers
    Average_Odd = Odd_sum / Odd_numbers
    print(Average_Even, 'is the Average of Even Numbers from', L, 'to', U)
    print(Average_Odd, 'is the Average of Odd numbers from', L, 'to', U)
    print('Hi Aditya Your Program execution is Completed')
    print('Thank You')
Odd_Even(3,8)