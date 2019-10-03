#include <stdio.h>
int main(void) 
{
  int N,M,P;
    scanf("%d",&N);
    scanf("%d",&M);
    P=N+M;
    if(P%2==0)
      printf("even");
    else
    printf("odd");
    return 0;
}
