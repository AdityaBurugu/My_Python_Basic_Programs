def Multiples(Number,LowerLimit = 0,UpperLimit = 100):
    x = Number
    L=LowerLimit
    U=UpperLimit
    Multiples = []
    if type(x)==int:
        for i in range(L,U+1):
            if type(x)== int and x>=0:
                if(i % x ==0):
                    Multiples.append(i)
            else:
                if (type(x)==int and i % x == 0):
                    Multiples.append(-(i))
        print(Multiples)
    else:
        print("Invalid Input")
Multiples(2)