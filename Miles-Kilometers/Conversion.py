def miles_to_km(x):
    print(x,'Miles =',x*1.6//1,'km')
while 1 :
    x = float(input('Miles = '))
    miles_to_km(x)
    Choice = input('Do U Want to Continue : ')
    if (Choice == 'Y' or Choice == 'y'):
        continue
    elif (Choice == 'N' or Choice == 'n'):
        break
    elif (Choice != 'Y' or Choice != 'y' or Choice != 'N' or Choice != 'n'):
        print('please give input y or y or n or n for further process')
    Choice = input('Do U Want To Continue : ')
    if (Choice == 'Y' or Choice == 'y'):
        continue
    elif (Choice == 'N' or Choice == 'n'):
        break
    elif (Choice != 'Y' or Choice != 'y' or Choice != 'N' or Choice != 'n'):
        print('please give input y or y or n or n for further process')
    print("Invalid Input")
    break