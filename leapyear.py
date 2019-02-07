while True:
	try:
		year=int(input())
		break
	except:
		print("invalid")
		break
if (year%4==0 and year%4!=0 or year%400==0):
	print("yes")
else:
	print("no")
