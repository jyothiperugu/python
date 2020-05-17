#include <stdio.h>
int main()
{
 int num = 0, remainder = 0;

 // while -1 not entered...
 while(num != -1)
 {
 // prompt user for input
 printf("Enter an integer (-1 to stop): ");
 // read and store input, then modulus by 2
 scanf_s("%d", &num, sizeof(int));
 // ready to stop if -1 else...
 if(num != -1)
 {
 remainder = num % 2;
 // test for even/odd. If the modulus yields 0, it is even
if(remainder == 0)
 printf("%d is an even number.\n", num);
 else
 printf("%d is an odd number.\n", num);
 }
 }
 // -1 was entered
 printf("%d is an odd number.\n", num);
 printf("You ask to stop! Thank you.\n");
 return 0;
}
