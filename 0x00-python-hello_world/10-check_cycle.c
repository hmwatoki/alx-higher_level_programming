#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to head of list
 * Return: 1 if cycle, 0 otherwise
*/
int check_cycle(listint_t *list)
{
listint_t *slw = list, *fst = list;
while (slw && fst && fst->next)
{
slw = slw->next;
fst = fst->next->next;
if (slw == fst)
{
return (1);
}
}
return (0);
}
