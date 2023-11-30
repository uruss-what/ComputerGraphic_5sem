#include <iostream>
#include <cmath>

using namespace std;
// Функция для вычисления приближенного корня первой частной производной по x
double FirstDerivativeX(double** arr, int rows, int columns, int x, int y) {
    if (x == 0) {
        return (arr[y][x + 1] - arr[y][x]) / 1.0;
    }
    else if (x == columns - 1) {
        return (arr[y][x] - arr[y][x - 1]) / 1.0;
    }
    else {
        return (arr[y][x + 1] - arr[y][x - 1]) / 2.0;
    }
}

// Функция для вычисления приближенного корня первой частной производной по y
double FirstDerivativeY(double** arr, int rows, int columns, int x, int y) {
    if (y == 0) {
        return (arr[y + 1][x] - arr[y][x]) / 1.0;
    }
    else if (y == rows - 1) {
        return (arr[y][x] - arr[y - 1][x]) / 1.0;
    }
    else {
        return (arr[y + 1][x] - arr[y - 1][x]) / 2.0;
    }
}

// Функция для вычисления приближенного корня второй частной производной по x
double SecondDerivativeX(double** arr, int rows, int columns, int x, int y) {
    if (x == 0) {
        return (arr[y][x + 2] - 2 * arr[y][x + 1] + arr[y][x]) / 1.0;
    }
    else if (x == columns - 1) {
        return (arr[y][x] - 2 * arr[y][x - 1] + arr[y][x - 2]) / 1.0;
    }
    else {
        return (arr[y][x + 1] - 2 * arr[y][x] + arr[y][x - 1]) / 1.0;
    }
}

// Функция для вычисления приближенного корня второй частной производной по y
double SecondDerivativeY(double** arr, int rows, int columns, int x, int y) {
    if (y == 0) {
        return (arr[y + 2][x] - 2 * arr[y + 1][x] + arr[y][x]) / 1.0;
    }
    else if (y == rows - 1) {
        return (arr[y][x] - 2 * arr[y - 1][x] + arr[y - 2][x]) / 1.0;
    }
    else {
        return (arr[y + 1][x] - 2 * arr[y][x] + arr[y - 1][x]) / 1.0;
    }
}

int main() {
    setlocale(LC_ALL,"Russian");
    const int rows = 5;  // Количество строк в массиве
    const int columns = 5;  // Количество столбцов в массиве

    // Инициализация двумерного массива
    double** arr = new double* [rows];
    for (int i = 0; i < rows; i++) {
        arr[i] = new double[columns];
    }

    // Заполнение массива значениями
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            arr[i][j] = sin(i) + cos(j);
        }
    }

    // Поиск максимального и минимального значения приближенной первой частной производной по x
    double maxFirstPartialDerivativeX = FirstDerivativeX(arr, rows, columns, 0, 0);
    double minFirstPartialDerivativeX = FirstDerivativeX(arr, rows, columns, 0, 0);

    // Поиск максимального и минимального значения приближенной первой частной производной по y
    double maxFirstPartialDerivativeY = FirstDerivativeY(arr, rows, columns, 0, 0);
    double minFirstPartialDerivativeY = FirstDerivativeY(arr, rows, columns, 0, 0);

    // Поиск максимального и минимального значения приближенной второй частной производной по x
    double maxSecondPartialDerivativeX = SecondDerivativeX(arr, rows, columns, 0, 0);
    double minSecondPartialDerivativeX = SecondDerivativeX(arr, rows, columns, 0, 0);

    // Поиск максимального и минимального значения приближенной второй частной производной по y
    double maxSecondPartialDerivativeY = SecondDerivativeY(arr, rows, columns, 0, 0);
    double minSecondPartialDerivativeY = SecondDerivativeY(arr, rows, columns, 0, 0);



    //Максимумы и минимумы первой производной по x и y
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {

            if (maxFirstPartialDerivativeX < FirstDerivativeX(arr, rows, columns, j, i)) {
                maxFirstPartialDerivativeX = FirstDerivativeX(arr, rows, columns, j, i);
            }

            if (minFirstPartialDerivativeX > FirstDerivativeX(arr, rows, columns, j, i)) {
                minFirstPartialDerivativeX = FirstDerivativeX(arr, rows, columns, j, i);
            }

            if (maxFirstPartialDerivativeY < FirstDerivativeY(arr, rows, columns, j, i)) {
                maxFirstPartialDerivativeY = FirstDerivativeY(arr, rows, columns, j, i);
            }

            if (minFirstPartialDerivativeY > FirstDerivativeY(arr, rows, columns, j, i)) {
                minFirstPartialDerivativeY = FirstDerivativeY(arr, rows, columns, j, i);
            }

        }
    }

    //Максимумы и минимумы второй производной по x и y
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {

            if (maxSecondPartialDerivativeX < SecondDerivativeX(arr, rows, columns, j, i)) {
                maxSecondPartialDerivativeX = SecondDerivativeX(arr, rows, columns, j, i);
            }

            if (minSecondPartialDerivativeX > SecondDerivativeX(arr, rows, columns, j, i)) {
                minSecondPartialDerivativeX = SecondDerivativeX(arr, rows, columns, j, i);
            }

            if (maxFirstPartialDerivativeY < SecondDerivativeY(arr, rows, columns, j, i)) {
                maxFirstPartialDerivativeY = SecondDerivativeY(arr, rows, columns, j, i);
            }

            if (minSecondPartialDerivativeY > SecondDerivativeY(arr, rows, columns, j, i)) {
                minSecondPartialDerivativeY = SecondDerivativeY(arr, rows, columns, j, i);
            }

        }
    }

    cout << "Функция sin(y) + cos(x)\nМаксимумы первой производной по \nx = " << maxFirstPartialDerivativeX << " \ny =  " << maxFirstPartialDerivativeY;
    cout << "\nМинимумы первой производной по \nx = " << minFirstPartialDerivativeX << " \ny =  " << minFirstPartialDerivativeY;
    cout << "\nМаксимумы второй производной по \nx = " << minSecondPartialDerivativeX << " \ny =  " << minSecondPartialDerivativeY;
    cout << "\nМинимумы второй производной по \nx = " << minSecondPartialDerivativeX << " \ny =  " << minSecondPartialDerivativeY;

}
