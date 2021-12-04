
"""Python's map() is a built-in function that allows you to process and transform all the items in an iterable 
   without using an explicit for loop, a technique commonly known as mapping. 
   map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable."""

a=lambda i :i*i

lis=[4,5,2,9]
print("List of Squares of lis is: ")
print(list(map(a,lis)))
