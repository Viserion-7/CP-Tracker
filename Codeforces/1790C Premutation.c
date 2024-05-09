#include <stdio.h>

int main() {
    int t, n, x[100][100];
    int i, j, a, b;
    
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            for (j = 1; j < n; j++) {
                scanf("%d", &x[i][j]);
            }
        }

        if (x[0][1] == x[1][1])
            a = x[0][1];
        else
            a = x[2][1];

        for (i = 0; x[i][1] == a; i++);

        printf("%d", a);
        for (j = 1; j < n; j++)
            printf(" %d", x[i][j]);
        
        printf("\n");
    }

    return 0;
}
