#include <stdio.h>

main()
{
	char str[80];
	int i, delt = 'a' - 'A';

	printf("you entered a string less than 80 characters:\n");
	gets( str );
	
	for (i = 0; str[i]; i++){
		if ((str[i] >= 'a') && (str[i] <= 'z'))
			str[i] -= delt; /* convert to upper case */
	}
	printf("The entered string is (in uppercase):\n", str);
	
	return 0;
}
