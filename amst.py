val=int(input())
z=list(map(int,str(val)))
y=list(map(lambda x:x**3,z))
if(sum(y)==val):
	print("yes")
else:
	print("no")
