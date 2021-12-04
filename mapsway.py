
"""Python's map() is a built-in function that allows you to process and transform all the items in an iterable 
   without using an explicit for loop, a technique commonly known as mapping. 
   map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable."""

a=lambda i :i*3

lis=[1, 2, 3, 4, 5, 6, 7]

print(list(map(a,lis)))