print("to check given num is positive or negative")
while True:
	try:
		a=input("enter num")
		val=int(a)
		break
	except:
		print("the num is not a int")
		break
if(val>0):
	print("the num is positive")
elif(val==0):
	print("the num is zero")
else:
	print("the num is negative")
