#include<stdio.h>
#include<string.h>
int main()
{
char a[50],p; 
int len,i;

scanf("%s",a);
len=strlen(a);
if(len%2==0)
{
for(i=0;i<len;i+=2)
{
p=a[i];
a[i]=a[i+1];
a[i+1]=p;

}
printf("%s",a);
}
else
{
for(i=0;i<(len-1);i+=2)
{
p=a[i];
a[i]=a[i+1];
a[i+1]=p;

}
printf("%s",a);
}
return 0;
}
