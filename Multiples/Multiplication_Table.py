def Multiplication_Table(Number,LowerLimit = 0, UpperLimit = 10):
   N = Number
   L = LowerLimit
   U = UpperLimit
   if type(N)==int:
      for i in range(L,U+1):
         print(N,'x',i,'=',N*i)
      print('Program Completed')
      print('Program Uploaded bu Aditya Burugu')
   else:
      print("Invalid Input")
Multiplication_Table(-7)