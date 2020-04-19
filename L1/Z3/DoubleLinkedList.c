#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct ListElement
{
    int data;
    struct ListElement * previous;
    struct ListElement * nextElement;
} Element;

void show(Element *front);
void merge(Element **frontList1, Element **frontList2);
void find(Element *front, int position);
void delete(Element **front);
void deletePosition(Element **front, int position);
int size(Element *front);
void push(Element **front, int data);
void pushPosition(Element **front, int data, int position);



void push(Element **front, int data)
{
    if(*front == NULL)
    {
        *front = (Element*) malloc(sizeof(Element));
        (*front) -> data = data;
        (*front) -> previous = (*front);
        (*front) -> nextElement = (*front);
    }
    else
    {
        Element *current = *front;
        while (current -> nextElement != *front)
        {
            current = current -> nextElement;
        }
        current -> nextElement = (Element*) malloc(sizeof(Element));
        current -> nextElement -> data = data;
        current -> nextElement -> previous = current;
        current -> nextElement -> nextElement = (*front);
        (*front) -> previous = current -> nextElement;
    }
}

void pushPosition(Element **front, int data, int position)
{
    if(position == 0)
    {
        Element *current;
        Element *tmp;
        tmp = (*front) -> previous;
        current = (Element*) malloc(sizeof(Element));
        current -> data = data;
        current -> nextElement = (*front);
        current -> previous = tmp;
        tmp -> nextElement = current;
        (*front) -> previous = current;
        (*front) = current;
    }
    else if(position == size(*front))
    {
        push(front, data);
    }
    else
    {
        Element *current;
        Element *tmp;

        int i = 0;
        while (current -> nextElement != NULL && i < position - 1)
        {
            current = current -> nextElement;
            i++;
        }

        tmp = current -> nextElement;
        current -> nextElement = (Element*) malloc(sizeof(Element));
        current -> nextElement -> data = data;
        current -> nextElement -> previous = current;
        tmp -> previous = current -> nextElement;
        current -> nextElement -> nextElement = tmp;
    }
}

void delete(Element **front)
{

    if((*front) -> nextElement == (*front))
    {
        *front = NULL;
    }
    else
    {
        Element *current = *front;
        while (current -> nextElement -> nextElement != (*front))
        {
            current = current -> nextElement;
        }
        free(current -> nextElement);
        current -> nextElement = (*front);
        (*front) -> previous = current;
    }
}

void deletePosition(Element **front, int position)
{
    if(position == 0)
    {
        Element *tmp;
        tmp = (*front) -> nextElement;
        tmp -> previous = (*front) -> previous;
        (*front) -> previous -> nextElement = tmp;
        free(*front);
        *front = tmp;
    }
    if(position == size(*front))
    {
        delete(front);
    }
    else
    {
        Element *current = *front;
        Element *tmp;
        int i = 0;
        while (current -> nextElement != (*front) && i < position - 1)
        {
            current = current -> nextElement;
            i++;
        }
        tmp = current -> nextElement;
        current -> nextElement = tmp -> nextElement;
        current -> nextElement -> previous = current;
        free(tmp);
    }
}

void show(Element *front)
{
    if(front == NULL)
    {
        printf("List is empty");
    }
    else
    {
        Element *current = front;
        do {
            printf("%i\n", current -> data);
            current = current -> nextElement;
        }while (current != front);
    }
}

void find(Element *front, int position)
{
    Element *current = front;
    if(position < size(front) / 2)
    {
        int i = 0;
        while (current->nextElement != front && i < position - 1)
        {
            current = current -> nextElement;
            i++;
        }
        current = current -> nextElement;
        printf("%i", current -> data);
    }
    else
    {
        int i = size(front);
        while (current -> previous != NULL && i > position + 1)
        {
            current = current -> previous;
            i--;
        }
        current = current -> previous;
        printf("%i", current -> data);
    }
}

void merge(Element **frontList1, Element **frontList2)
{
    Element *current = *frontList2;
    Element *nextElement;

    while (current -> nextElement != (*frontList2))
    {
        push(frontList1, current -> data);
        nextElement = current -> nextElement;
        free(current);
        current = nextElement;
    }

    if (current -> nextElement == (*frontList2))
    {
        push(frontList1, current -> data);
        free(current);
    }
    *frontList2 = NULL;
}

int size(Element *front)
{
    int amount = 0;
    if(front == NULL)
    {
        return amount;
    }
    else
    {
        Element *current = front;
        do
        {
            amount++;
            current = current -> nextElement;
        }while (current != front);
    }
    return amount;
}

int main()
{
    Element *frontList1;
    frontList1 = NULL;

    Element *frontList2;
    frontList2 = NULL;

    for(int i = 0; i < 1000; i++)
    {
        push(&frontList1, rand() % 100);
        push(&frontList2, rand() % 100);
    }

    pushPosition(&frontList1, 35, 0);
    deletePosition(&frontList1, 120);
    deletePosition(&frontList1, 546);
    printf("\n");
    show(frontList2);
    merge(&frontList1, &frontList2);
    show(frontList1);

    clock_t begin = clock();
    printf("\nElement 45 is: ");
    find(frontList1, 45);
    clock_t end = clock();

    double time;
    time = (double) (end - begin) / CLOCKS_PER_SEC;
    printf("\nTime spent to reach the position(45): %f\n", time);

    clock_t begin1 = clock();
    printf("\nElement 982 is: ");
    find(frontList1, 982);
    clock_t end1 = clock();

    time = (double) (end1 - begin1) / CLOCKS_PER_SEC;
    printf("\nTime spent to reach the position(982): %f\n", time);
}