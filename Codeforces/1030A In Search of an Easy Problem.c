#include <stdio.h>
int main()
{
    int a, c = 0;
    scanf("%d",&a);
    int A[a];
    for(int i = 0; i < a; i++)
	{
		scanf("%d",&A[i]);
        if(A[i] == 1)
			c++;
    }
    if(c== 0)
		printf("EASY");
    else
		printf("HARD");
}
