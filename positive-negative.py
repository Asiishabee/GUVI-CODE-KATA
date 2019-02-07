while True:
	try:
		a=inpu
		val=int(a)
		break
	except:
		print("the num is not a int")
		break
if(val>0):
	print("positive")
elif(val==0):
	print("zero")
else:
	print("negative")
