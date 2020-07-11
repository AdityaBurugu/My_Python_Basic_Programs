def Celsius_to_Fahrenheit(x):
    print(x, 'Celsius =', (x * 1.8) + 32 // 1, 'Fahrenheit')

while 1 :
    x = float(input('Celsius = '))
    Celsius_to_Fahrenheit(x)
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