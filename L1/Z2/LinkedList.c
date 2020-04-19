#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct ListElement
{
    int data;
    struct ListElement * next;
} ListElement_type;

void show(ListElement_type *front);
void find(ListElement_type *front, int position);
void merge(ListElement_type **head, ListElement_type **head1);
int size(ListElement_type *front);
void pushFront(ListElement_type **front, int number);
void pushBack(ListElement_type **front, int number);
void pushPosition(ListElement_type **front, int number, int position);
void deleteFront(ListElement_type **front);
void deleteBack(ListElement_type **front);
void deletePosition(ListElement_type **front, int position);

void pushFront(ListElement_type **front, int number)
{
    ListElement_type *current;
    current = (ListElement_type *) malloc(sizeof(ListElement_type));
    current -> data = number;
    current -> next = (*front);
    *front = current;
}

void pushBack(ListElement_type **front, int number)
{
    if(*front == NULL)
    {
        *front = (ListElement_type*) malloc(sizeof(ListElement_type));
        (*front) -> data = number;
        (*front) -> next = NULL;
    }
    else
    {
        ListElement_type *current=*front;
        while (current -> next != NULL)
        {
            current = current->next;
        }
        current -> next = (ListElement_type*) malloc(sizeof(ListElement_type));
        current -> next -> data = number;
        current -> next -> next = NULL;
    }
}

void pushPosition(ListElement_type **front, int number, int position)
{
    if(position == 0)
    {
        pushFront(front, number);
    }
    else
    {
        if(position == size(*front))
        {
            pushBack(front, number);
        }
        else
        {
            ListElement_type *current=*front;
            ListElement_type *tmp;
            int i = 0;
            while (current -> next != NULL && i < position-1)
            {
                current = current -> next;
                i++;
            }
            tmp = current -> next;
            current -> next = (ListElement_type*) malloc(sizeof(ListElement_type));
            current -> next -> data = number;
            current -> next -> next = tmp;
        }
    }
}

void deleteFront(ListElement_type **front)
{
    ListElement_type *tmp = NULL;
    if (*front != NULL)
    {
        tmp = (*front) -> next;
        free(*front);
        *front = tmp;
    }
}

void deleteBack(ListElement_type **front)
{
    if((*front) -> next == NULL)
    {
        *front = NULL;
    }
    else
    {
        ListElement_type *current = *front;
        while (current -> next -> next != NULL)
        {
            current = current -> next;
        }
        free(current -> next);
        current -> next = NULL;
    }
}


void deletePosition(ListElement_type **front, int position)
{
    if(position == 0)
    {
        deleteFront(front);
    }
    else
    {
        ListElement_type *current = *front;
        ListElement_type *tmp;
        int i=0;
        while (current -> next != NULL && i < position-1)
        {
            current=current -> next;
            i++;
        }
        tmp = current -> next;
        current -> next = tmp -> next;
        free(tmp);
    }
}

void show(ListElement_type *front)
{
    if(front == NULL)
    {
        printf("List is empty");
    }
    else
    {
        ListElement_type *current = front;
        while (current != NULL)
        {
            printf("%i\n", current -> data);
            current = current -> next;
        }
    }
}

void find(ListElement_type *front, int position)
{
    ListElement_type *current = front;
    int i = 0;
    while(current -> next != NULL && i < position - 1)
    {
        current = current -> next;
        i++;
    }
    printf("%i\n", current -> next -> data);
}

void merge(ListElement_type **head, ListElement_type **head1)
{
    ListElement_type *current = *head1;
    ListElement_type *next;
    while (current != NULL)
    {
        pushBack(head, current -> data);
        next = current -> next;
        free(current);
        current = next;
    }
    *head1 = NULL;
}

int size(ListElement_type *front)
{
    int counter = 0;
    if(front == NULL)
    {
        return counter;
    }
    else
    {
        ListElement_type *current = front;
        while (current != NULL)
        {
            counter++;
            current = current -> next;
        }
    }
    return counter;
}

int main()
{
    ListElement_type *head;
    head = NULL;

    ListElement_type *head1;
    head1 = NULL;

    for (int i = 0; i < 1000; i++)
    {
        pushBack(&head, rand() % 100);
        pushBack(&head1, rand() % 100);
    }

    merge(&head, &head1);
    find(head, 9);
    pushFront(&head, 54);
    pushPosition(&head, 58, 0);
    pushFront(&head, 91);
    deleteBack(&head);
    deletePosition(&head, 27);
    deleteFront(&head);
    show(head);

    printf("\n");
    clock_t start = clock();
    find(head, 20);
    clock_t finish = clock();

    double time = 0.0;
    time += (double) (finish - start) / CLOCKS_PER_SEC;
    printf("Time spent to reach the position(20): %f\n", time);

    clock_t start1 = clock();
    find(head, 999);
    clock_t finish1 = clock();
    time += (double) (finish1 - start1) / CLOCKS_PER_SEC;
    printf("Time spent to reach the position(999): %f\n", time);
}