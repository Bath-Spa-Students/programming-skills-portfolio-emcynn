#Practice Exercise 5
#You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

#Given list
list1 = [5, 10, 15, 20, 25, 50, 20]

#Find the index of the first occurrence of 20
index_20 = list1.index(20)

#Replace it with 200
list1[index_20] = 200

#Display the updated list
print("Updated list:", list1)