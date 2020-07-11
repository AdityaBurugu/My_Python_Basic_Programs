S = int(input('Enter the Range for which Square Numbers to be Found : '))
Square_Numbers = []
def Square(N):
    for i in range(1,N+1):
        Square_Numbers.append(i*i)
    print('Square Numbers = ',Square_Numbers)
Square(S)
Sum = sum(Square_Numbers)
print('The Sum of Square_Numbers = ',Sum)
print('Program Finished')
print('Program Uploaded by Aditya Burugu')