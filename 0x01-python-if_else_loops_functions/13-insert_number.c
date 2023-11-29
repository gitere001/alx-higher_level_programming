#include "lists.h"
/**
 * insert_node - insert a new node
 * @head: head pointer
 * @number: number of node inserted
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *tmp = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head || ((*head)->n > number))
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			tmp = current;
			current = current->next;
		}
		tmp->next = new;
		new->next = current;
	}
	return (new);
}
