hello = "mammam sux"
goodbye = "hey mammam is not so bad"
weeeee = "LOL"
vowels = ['a','e','i','o','u']
print(hello[1])
# prints the second character of the string hello 

for i in range(10):
	print(i)
# prints one number per line from 0 to 9 inclusive

for i in range(len(hello)):
	print(hello[i])
#prints one letter per line of the string hello
for i in range(5):
	print (vowels[i])


print(len(hello))
# len gives the length of the string 

print(len(vowels))




print (hello)

for i in range(len(hello)):
	if(hello[i] in vowels):
		print (hello[i])

def timesTwo(n):
	return n*2
	
print(timesTwo(18.5))





def vowPrint(R):
	vowels = ['a','e','i','o','u']
	for i in range(len(R)):
		if(R[i] in vowels):
			print (R[i])


vowPrint(hello)

vowPrint(goodbye)

print (weeeee)
