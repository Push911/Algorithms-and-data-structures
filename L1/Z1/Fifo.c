#include <stdbool.h>
#include <stdio.h>

#define MAX 1000
#define ERROR 1000000000

int  p = 0, k = 0, tab[MAX];

bool toEnd(int element)
{
    if(k == MAX)
        return 0;
    tab[k++] = element;
    return 1;
}

int firstElement()
{
    if(p == k)
        return ERROR;
    return tab[p];
}

int lastElement()
{
    if(p == k)
        return ERROR;
    return tab[k-1];
}
int main()
{
    int fe = firstElement();
    int le = lastElement();

    if(!toEnd(12) || !toEnd(22) || !toEnd(32))
    {
        printf("Queue is full");
    }

    if(fe != ERROR)
    {
        printf("First element in queue: %d", fe);
    }
    else if(le != ERROR)
    {
        printf("Last element in queue: %d", le);
    }
    else
    {
        printf("Error");
    }
}