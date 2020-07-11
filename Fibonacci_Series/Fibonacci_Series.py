Number_of_Terms = int(input("Number_of_Terms = "))

# first two terms
N1 = 0
N2 = 1
count = 2
# check if the number of terms is valid
if Number_of_Terms <= 0:
   print("Please enter a positive integer")
elif Number_of_Terms == 1:
   print("Fibonacci sequence:")
   print(N1)
else:
   print("Fibonacci sequence:")
   print(N1,",",N2,end=', ')
   while count < Number_of_Terms:
       Nth = N1 + N2
       print(Nth,end=' , ')
       # update values
       N1,N2 = N2,Nth
       count += 1