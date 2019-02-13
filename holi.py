p = input()
if(p in ["Saturday","saturday","Sunday","sunday","SATURDAY","SUNDAY"]):
    print("yes")
elif(p in ["Monday","Tuesday","Wednesday","Thursday","Friday","monday","tuesday","wednesday","thursday","friday","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]):
    print("no")
else:
    print("Invalid Input")
