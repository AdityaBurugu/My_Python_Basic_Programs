#Learning the Concepts of Lists
#Creating a List
Numbers = [54,848,9483,23,478]
print('Numbers = ',Numbers)
#Accessing Values in the created list
#Accessing only One value in the above Created List
print('Value available at index [3] is',Numbers[3])
#Accessing Multiple values in the above Created List
#Accessing Multiples values in a Range in the above Created List
print('The values from index [1] to index [4] are',Numbers[1:4])
#Accessing Multiple values in a  Range untill the last element in the above Created List
print('The values from index [1] to [the last element of this list] are',Numbers[1:])
#Accessing Multiple values in a  Range from starting value to the given indexing value in the above Created List
print('The values from index [0] to index [4] are',Numbers[:4])
#Accessing a value in a Reverse[Negative] Order in the above Created List
print('Value available at index [-2] is',Numbers[-2])
#Now let's create a list using String as an element in that list
Names = ['Aditya','Akhil','Navya','Nani','Rakesh','Parvathi','Yashvi']
print('Names = ',Names)
#Let's Create List containing Multiple Data Types
Data = [1.5,3,'Aditya']
print('Data = ',Data)
#Let's try to create a List in a List
List = [Numbers , Names]
print('The combined list of Numbers and Names = ',List)
#Let's try to add another element to the Numbers List
#Let's try to add another element to the Numbers List at the last
Numbers.append(22)
print('The list after appending 22 in Numbers list :',Numbers)
#Let's try to add another element to the Numbers List in between
Numbers.insert(3,10)
print('The list after inserting 10 at indexing value 3 in Numbers list :',Numbers)
#Let's try to remove an element in the Numbers List
Numbers.remove(478)
print('The list after removing 478 from Numbers list :',Numbers)
#Let's try to Remove element from Numbers List based on it's Indexing Number
Numbers.pop(2)
print('The list after removing element at indexing value 2 in Numbers list :',Numbers)
#Let' see what's gone be my output if I didn't mention te Indexing value [Last element in my list is removed]
Numbers.pop()
print('The list after removing element at the last indexing value in Numbers list :',Numbers)
#Let's try to remove Multiple values in Numbers list
del Numbers[2:]
print('The list after removing elements from indexing value[2] to the last indexing value in Numbers list :',Numbers)
#Let' try to add multiples values to the Number list
Numbers.extend([27,30,55,66])
print('The list after adding multiple elements at the last indexing value in Numbers list :',Numbers)
#Let' try to find yhe Minimum value in Numbers List
print('The Minimum value in Numbers List = ',min(Numbers))
#Let' try to find yhe Maximum value in Numbers List
print('The Maximum value in Numbers List = ',max(Numbers))
#let's try to find out the sum of Numbers List
print('The Sum of Numbers List = ',sum(Numbers))
#Let's try to sort out the Numbers List
Numbers.sort()
print('Ascending Order =',Numbers)
#let's try to replace a Indexing value in Number List[Updating the List]
Numbers[3]=66
print('The New Value Available at index [3] in Numbers List :',Numbers)
#let's try to find out the number of elements in Number List
print('The No.of Elements in Numbers List =',len(Numbers))
#Let's try to Merge Up two lists
print('The List after Merging Up =',[1,2,3,4] + [5,6,7,8])
#let's try to print the same list Multiple times
print('4 times Hi =',['HI'] * 4)
#Let's try to find out how many times an element is being repeated in Numbers Lists
print('The Number of Times the Number has repeated =',Numbers.count(66))
#Let's clear a list
A = [1,2,3,'Aditya',55]
A.clear()
print('The Output after clearing List A =',A)
#Let's copy a list to another list
B = Numbers.copy()
print('The List after copying Numbers List to B =',B)
#Let's try to find out the indexing value of a element in Numbers List
print('The indexing value of 848 =',Numbers.index(848))
#Let's try to reverse the Numbers List
Numbers.reverse()
print('The New List after reversing the elements :',Numbers)
#Getting hash value of a String
print(hash('87287'))
print('Program Completed')
print('Thank You')
print('Program Upload by Aditya Burugu')