

a=list(range(0,500))
b=0
c=0

print("Working with FOR")
for x in range(0,len(a)):
	b=b+a[x]
print("Sum of a="+ str(b))

b=0
print("Case WHILE")
while(c<len(a)):
	b=b+a[c]
	c=c+1
print("Sum of a="+ str(b))



def sumList(list):
	b=0
	if len(list)==1:
		return list[0]
	else:
		return b + list[0] + sumList(list[1:len(list)])
	print("Sum of a="+ str(b))


print("Case RECURSION \n Sum of a=" + str(sumList(a)))
