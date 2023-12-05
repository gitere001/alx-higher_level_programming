#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* reverse_listint - Function to reverse a linked list in place
* @head: Pointer to the head of the list
* Return: Pointer to the new head of the reversed list
*/
listint_t *reverse_listint(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
* is_palindrome - Function to check if singly linked list is palindrome
* @head: Pointer to the head of the list
* Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = *head;
	listint_t *second_half, *reversed_second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second_half = slow;
	reversed_second_half = reverse_listint(second_half);

	while (reversed_second_half != NULL)
	{
		if ((*head)->n != reversed_second_half->n)
			return (0);

		*head = (*head)->next;
		reversed_second_half = reversed_second_half->next;
	}

	prev_slow->next = reverse_listint(second_half);

	return (1);
}
