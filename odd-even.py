while True:
	try:
		value=int(input(""))
		break
	except:
		print("invalid")
		break
if(value%2==0):
	print("Even")
else:
	print("Odd")
