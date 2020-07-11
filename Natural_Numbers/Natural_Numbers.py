N = int(input("Enter a number: "))
if N < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(N > 0):
       sum += N
       N -= 1
   print("The sum of",'Natural Numbers =',sum)