#include<stdio.h>
#include<conio.h>
void main()
{
 char a[1000],b[1000];
 int i,z=10;
 clrscr();
 printf("\n Enter string\n");
 gets(a);
 for(i=0;a[i]!='\0';i++)
 {
 	
  printf("%c",a[i]);
  if(i==z)
  {
     printf("\n");
     z+=10;
    }
 }
 getch();
}
