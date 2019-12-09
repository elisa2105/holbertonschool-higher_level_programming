#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: list
 * Return: 0 if there is no cycle 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *ptr1 = list;
listint_t *ptr2 = list;
if (list == NULL)
return (0);
while (ptr1->next != NULL && ptr1->next->next != NULL && ptr2->next != NULL)
{
ptr1 = ptr1->next->next;
ptr2 = ptr2->next;
if (ptr1 == ptr2)
return (1);
}
return (0);
}
