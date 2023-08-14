#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next_half = NULL;
	int isPalindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (isPalindrome);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next_half = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next_half;
	}
	if (fast != NULL)
		slow = slow->next;
	while (slow != NULL)
	{
		if (prev->n != slow->n)
		{
			isPalindrome = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}

	return (isPalindrome);
}
