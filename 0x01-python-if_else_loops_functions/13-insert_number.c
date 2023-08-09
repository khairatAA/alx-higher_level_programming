#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - adds a new node to the sorted list
 * @head: the first node
 * @number: value to be added
 * Return: the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node =  NULL;
	listint_t *temp = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < new_node->n)
		{
			temp = temp->next;
		}
		new_node->next = temp->next;
		temp->next = new_node;
	}
	return (new_node);
}
