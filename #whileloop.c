#include<stdio.h>
#include<conio.h>
 void main()
{
int n,s,sum=0;
clrscr();
printf("Enter the value of n");
scanf("%d",&n);
while(n!=0)
{
 s=n%10;
 n=n/10;
 sum=sum+s;
}
printf("%d\n",sum);
getch();
}
