#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    int n = 10;

    ptr = (int *)malloc(n * sizeof(int));

    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Use the allocated memory
    for (int i = 0; i < n; i++) {
        ptr[i] = i;
    }

    return 0;
}
