def Simple_Interest(P,T,R):
    print('Principle : Rs.',P)
    print('Time Period : ',T,'Years')
    print('Interest Rate :',R,'%')
    SI = (P*T*R)/100
    print('Simple_Interest : Rs.',SI)

while 1 :
    x = float(input('Enter the Principal : '))
    y = float(input('Enter the Time Period : '))
    z = float(input('Enter the Rate of Interest: '))
    Simple_Interest(x, y, z)
    Choice = input('Do U Want to Continue : ')

    if(Choice == 'Y' or Choice == 'y' ):

        continue
    elif(Choice == 'N' or Choice == 'n' ):
        break
    elif(Choice != 'Y' or Choice != 'y' or Choice != 'N' or Choice != 'n' ):
        print('Please give input Y or y or N or n for further process')
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