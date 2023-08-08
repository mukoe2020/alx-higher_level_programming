#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node into a sorted listint_t list
 * @head: pointer to pointer to the first node of the list
 * @number: integer to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next && number > current->next->n)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}

