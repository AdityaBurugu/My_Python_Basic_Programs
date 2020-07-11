C = int(input('Enter the Range for which Cube Numbers to be Found : '))
Cube_Numbers = []
def Cube(O):
    for j in range(1,O+1):
        Cube_Numbers.append(j*j*j)
    print('Cube Numbers = ',Cube_Numbers)
Cube(C)
Sum_= sum(Cube_Numbers)
print('The Sum of Cube_Numbers = ',Sum_)
print('Program Finished')
print('Program Uploaded by Aditya Burugu')