#method 1
#using for loop by adding new element before the current element

def revstring(s):
	a=""
	for i in s:
		a=i+a
	print(a)
revstring("1234abcd")



"""method 2
using slicing

def revstring(s):
	print(a[::-1])
a="1234abcd"
revstring(a)

"""
