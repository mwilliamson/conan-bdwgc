#include <stdio.h>

#include "gc.h"

int main() {
    int* data = GC_malloc(sizeof(int));
    *data = 42;

    printf("%d\n", *data);

    return 0;
}
