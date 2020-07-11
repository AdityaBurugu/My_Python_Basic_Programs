#Sum and Average of Odd Numbers and Sum and Average of Even Numbers.
L=int(input('Enter the Minimum Range: '))
U=int(input('Enter the Maximum Range: '))
Even_sum=0
Even_numbers=0
Odd_sum=0
Odd_numbers=0
for i in range(L,U+1):
    if(i%2==0):
        Even_sum+=i
        Even_numbers+=1
    elif(i%2!=0):
        Odd_sum+=i
        Odd_numbers+=1
print(Even_sum,'is the sum of Even Numbers from',L,'to',U)
print(Odd_sum,'is the sum of Odd numbers from',L,'to',U)
print('There are',Even_numbers,'between',L,'and',U)
print('There are',Odd_numbers,'Between',L,'and',U)
Average_Even=Even_sum/Even_numbers
Average_Odd=Odd_sum/Odd_numbers
print(Average_Even,'is the Average of Even Numbers from',L,'to',U)
print(Average_Odd,'is the Average of Odd numbers from',L,'to',U)
print('Hi Aditya Your Program execution is Completed')
print('Thank You')