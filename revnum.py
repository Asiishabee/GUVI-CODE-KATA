val=int(input())
reverse=0
while(val>0):
    dig=val%10
    reverse=(reverse*10)+dig
    val=val//10
print(reverse)
