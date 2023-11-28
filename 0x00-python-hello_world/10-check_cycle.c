#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the header of the linked list
 *
 * Return: 1 if there is a cycle, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow =  slow->next;
		fast = fast->next->next;
	}
	return (0);
}