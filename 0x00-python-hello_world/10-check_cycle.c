#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linnked lists.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list;

	if (!list)
		return (0);

	while (first && last && last->next)
	{
		first = first->next;
		last = last->next->next;

		if (first == last)
			return (1);
	}
	return (0);
}
