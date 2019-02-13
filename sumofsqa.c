#include<stdio.h>
int main()
{
int n,m,r,s;
scanf("%d",&n);
m=n%10;
r=n/10;
s=(m*m)+(r*r);
printf("%d",s);
return 0;
}
