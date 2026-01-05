#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define WIDTH 5
#define MAX_SIZE (WIDTH * WIDTH)

int array[WIDTH][WIDTH];

int directions[][2] = {
    {0, 1},  // EST   (droite)
    {-1, 0}, // NORD  (haut)
    {0, -1}, // OUEST (gauche)
    {1, 0},  // SUD   (bas)
};

void fill_matrix(int t[WIDTH][WIDTH]) {
    int value = 1;
    int column = WIDTH / 2, line = WIDTH / 2;
    int direction_index = 0;
    int max_steps_in_direction = 1;
    int num_steps_done = 0;
    int num_change_direction = 2;

    while (1) {
        t[line][column] = value++;
        column += directions[direction_index][1];
        line += directions[direction_index][0];
        if (column < 0 || line < 0 || column >= WIDTH || line >= WIDTH)
            break;

        num_steps_done++;
        if (num_steps_done == max_steps_in_direction) {
            direction_index = (direction_index + 1) % 4;
            num_steps_done = 0;
            num_change_direction--;
            if (num_change_direction == 0) {
                max_steps_in_direction++;
                num_change_direction = 2;
            }
        }
    }
}

void print_matrix(int matrix[WIDTH][WIDTH]) {
    for (size_t i = 0; i < WIDTH; ++i) {
        for (size_t j = 0; j < WIDTH; ++j)
            printf("%4d ", matrix[i][j]);
        printf("\n");
    }
}

int main() {
    fill_matrix(array);
    print_matrix(array);
}
