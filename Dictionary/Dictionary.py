####Let's learn the Concept of Dictionaries
#Create a Dictionary
Data = {1:'Aditya',2:'Nani',3:'Akhil'}
print('Data :',Data)
#Accessin Values in Dictionary
print('Output :',Data[3])
#Accessin Values in Dictionary using Built-in-Functions
print('Output :',Data.get(1))
#Assigning values to keys which are not mentioned in the above Dictionary
print('Output :',Data.get(4,'Navya'))
#Let's try to Create Dictionary with the help of lists
Names = ['Aditya','Navya','Naveen','Akhil','Ganesh']
Likes = ['Python Programming','Learn New Things','Ride Bikes','Play Cricket','To Have Fun ']
Favorite = dict(zip(Names,Likes))
print('Favorite :',Favorite)
#Accessing values from above created Favorite Dictionary
print('Favorite :',Favorite['Navya'])
#Let's try to add new values to Favorite Dictionary
Favorite['Abhi']='Seeing Videos'
print('Favorite :',Favorite)
#Let's try to Delete a Value from Dictionary
del Favorite['Aditya']
print('Favorite :',Favorite)
#Create a List in a Dictionary and Dictiory in a Dictionary
Prog = {'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print('Prog :',Prog)
#Accessing Values in Prog Dictionary
print('Output :',Prog['JS'])
print('Output :',Prog['Java'])
print('Output :',Prog['Python'])
#Accessing Values in Prog {'Python'}
print('Output :',Prog['Python'][0])
print('Program Completed')
print("Thank You")
print('Program Uploaded by Aditya')