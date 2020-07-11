def Factorial(N):
    Factorial=1
    for i in range(2,N+1):
        Factorial = Factorial*i
    return Factorial

while 1 :
    x = int(input('Enter the Number : '))
    Fact = Factorial(x)
    print('Factorial of ', x, ':', Fact)

    Choice = input('Do U Want to Continue : ')
    if(Choice == 'Y' or Choice == 'y' ):
        continue
    elif(Choice == 'N' or Choice == 'n' ):
        break
    elif(Choice != 'Y' or Choice != 'y' or Choice != 'N' or Choice != 'n' ):
        print('please give input Y or y or N or n for further process')
    Choice = input('Do U Want To Continue : ')
    if (Choice == 'Y' or Choice == 'y'):
        continue
    elif (Choice == 'N' or Choice == 'n'):
        break
    elif (Choice != 'Y' or Choice != 'y' or Choice != 'N' or Choice != 'n'):
        print('Please Give Input Y or y or N or n for further process')
    print("Invalid Input")
    break
print('Program Finished')
print('Program Uploaded by Aditya Burugu')