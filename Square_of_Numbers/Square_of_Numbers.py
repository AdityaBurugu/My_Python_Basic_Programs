def Square(N):
    S = N
    Square_Numbers = []
    def Calculator(N):
        for i in range(1,N+1):
            Square_Numbers.append(i*i)
        print('Square Numbers = ',Square_Numbers)
    Calculator(S)
    Sum = sum(Square_Numbers)
    print('The Sum of Square_Numbers = ',Sum)
    print('Program Finished')
    print('Program Uploaded by Aditya Burugu')
Square(4)