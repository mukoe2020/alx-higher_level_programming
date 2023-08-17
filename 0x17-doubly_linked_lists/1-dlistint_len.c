#include "lists.h"

/**
 * dlistint_len - used to count number of elements in the linked list
 * @h: head of the linked list
 * Return: number of elements
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t countnodes = 0;

	while (h != NULL)
	{
		countnodes++;
		h = h->next;
	}
	return (countnodes);
}
