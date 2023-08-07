#include "lists.h"
/**
 * check_cycle - checks whether a linked list has a cycle or not
 * @list: the linked list
 * Return: 1 if there is a cycle and 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
