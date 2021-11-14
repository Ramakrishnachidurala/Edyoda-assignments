#Taking tuples in list
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#defining empty list and taking last element of every tuple  and sorting it

lis=[]
for k in a:
    lis.append(k[1])
lis.sort() 

#defining empty list2 and inserting tuples based on index values of lis   

lis2=[]
for i in range(len(lis)):
    for j in  range(len(a)):
        if lis[i]==a[j][1]:
            num=lis.index(lis[i])
            lis2.insert(num,a[j])
print(lis2)

#method2 using functions
"""#define function endelement return last element of every tuple

def endelement(a):
	return a[-1]

#Define another function sorttuple with the previous function as the key and sort the list
def sorttuple(tuples):
	return sorted(tuples, key=endelement)

a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sorttuple(a))"""
