a=int(input("Enter n number:"))
n=1
sum=0
while a>=1:
	while n%2==0:
		sum+=n
		a-=1
		n+=1
	else:
		n+=1
print("Sum of first ",n//2-1," even natural numbers is ",sum)