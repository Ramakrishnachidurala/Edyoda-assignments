#define empty dictionary

dict={}

#ASCII values of alphabets starts from a=97 and end on z=122

#SO define for loop with in range(97,123) as last value in for loop range not considered so values till 123 only printed i.e till z

for i in range(97,123):
    
	dict[chr(i)]=i

print(dict)    
