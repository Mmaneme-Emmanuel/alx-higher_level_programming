#include "lists.h"
/**
*check_cycle - Write a function in C that checks if a singly linked list has a cycle
*@list:pointer to the list to be checked
*Return:return 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
listint_t *fast_count, *slow_count;

fast_count = list;
slow_count = list;


while(slow_count != NULL && fast_count != NULL && fast_count->next != NULL)
{
	slow_count = slow_count->next;
	fast_count = fast_count->next->next;
	if (slow_count == fast_count)
	{
return (1);
	}
}
return (0);
}
