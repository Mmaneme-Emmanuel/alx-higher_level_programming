#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the listint_t list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *prev_slow = NULL, *mid_node = NULL;
int result = 1;

if (*head == NULL || (*head)->next == NULL)
	return (1);

while (fast != NULL && fast->next != NULL)
{
	fast = fast->next->next;
	prev_slow = slow;
	slow = slow->next;
}

if (fast != NULL)
{
	mid_node = slow;
	slow = slow->next;
}

prev_slow->next = NULL;
reverse_list(&slow);

result = compare_lists(*head, slow);

reverse_list(&slow);

if (mid_node != NULL)
{
	prev_slow->next = mid_node;
	mid_node->next = slow;
}
else
{
	prev_slow->next = slow;
}

return (result);
}

/**
 * reverse_list - reverses a linked list.
 * @head: pointer to the head of the list.
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists.
 * @head1: pointer to the head of the first list.
 * @head2: pointer to the head of the second list.
 * Return: 1 if the lists are equal, 0 otherwise.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}
	return (head1 == NULL && head2 == NULL);
}
