/*
 * File: 10-checks_cycle.c
 * Author: Daniel John
 */

#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - A function in C that checks if
 *		a singly linked list has a cycle in it.
 * @list: Linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cat, *mouse;

	if (list == NULL || list->next == NULL)
		return (0);

	cat = list->next;
	mouse = list->next->next;

	while (cat && mouse && mouse->next)
	{
		if (cat == mouse)
			return (1);

		cat = cat->next;
		mouse = mouse->next->next;
	}
	return (0);
}
