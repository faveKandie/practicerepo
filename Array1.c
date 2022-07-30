#include <stdio.h>
#include <string.h>
//an example on array//

int main(void)
{
	int SIZE = 10;
	int array[10] = {'0', '1', '2', 
	'3', '4', '5', '6', 
	'7', '8', '9',};
	int i;
	int j;
	int array2[11] = {'0', '1', '-2', 
	'-9', '-20', '-35', '-54', 
	'-77', '-96', '-135', '\0'};
	int k;
	int size = 10;
	char ARRAY[22];
	
	printf("size of array is : %d\n", sizeof(array));
	for (i = 0, j = 0, k = 0; i < SIZE, j < SIZE, k < size; i++, j++, k++)
	{
		array2[k] =  3 * k - 2 * k * k;
		printf("array[%d] = +%d \t array2[%d] = %d\n", i, j, k, array2[k]);
	}
	
	return(0);
}