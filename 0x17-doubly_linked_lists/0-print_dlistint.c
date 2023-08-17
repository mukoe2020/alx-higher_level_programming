#include "lists.h"

/**
 * print_dlistint - prints all elements in a linked list
 * @h: head of linked list
 * Return: number of nodes in the linked list
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t countnodes = 0;

	while (h != NULL)
	{
		countnodes++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (countnodes);
}
