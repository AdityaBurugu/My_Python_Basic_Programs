print('Product of Elements in a list')
def Prod_Lst(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
list1 = [1, 2, 3]
Output = Prod_Lst(list1)
print('Product of List :',Output)
print('*************************')
print('Program Finished')