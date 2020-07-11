A=int(input('Enter the Minimum Range: '))
B=int(input('Enter the Maxnimum Range: '))
n1=0
n2=1
n = n1 + n2
Fibo_Sequence=[]
if(A == 0 ) :
    Fibo_Sequence.append(n1)
    Fibo_Sequence.append(n2)
    Fibo_Sequence.append(n)
elif(A == 1 ) :
    Fibo_Sequence.append(n2)
    Fibo_Sequence.append(n)
while 1:
    n1,n2 = n2,n
    n = n1 + n2
    if(n > B):
        break
    elif(n >= A):
        Fibo_Sequence.append(n)
print('Fibonacci Sequence:',Fibo_Sequence)