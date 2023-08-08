#include "lists.h"

/**
 * check_cycle - checks if a linked list is a cycle
 * @list: pointer to the next node
 * Return: returns 1 on if a cycle is found or 0 if a cycle is not found
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && slow && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
