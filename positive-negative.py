while True:
	try:
		a=input("")
		val=int(a)
		break
	except:
		print("the num is not a int")
		break
if(val>0):
	print("Positive")
elif(val==0):
	print("zero")
else:
	print("Negative")
