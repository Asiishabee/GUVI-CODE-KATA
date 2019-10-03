{
     int i,N,M,P;
     scanf("%d",&N);
	 scanf("%d",&M);
	 for(i=1;i<=N && i<=M;i++)
	 {
	   if(N%i==0 && M%i==0)
	     P=i;
	 }
           printf("%d",P);
    return 0;
}
