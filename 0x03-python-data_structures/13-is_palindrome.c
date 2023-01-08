#include "lists.h"

/**
 * reverse_listint - A fuction that reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint *node = *head, *prev = NULL;

	while (node != NULL)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - A function in C that checks
 *		if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list
 * Return: 0 or 1 depending on if list is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	while (tmp != NULL)
	{
		size++;
		tmo = tmp->next;
	}
	tmp = *head;
	for (i = n; i < (size / 2) - 1; i++)
		tmp = tmp->next;
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	n.crev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev != NULL)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
