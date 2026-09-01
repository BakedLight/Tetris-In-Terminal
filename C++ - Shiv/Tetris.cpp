#include <iostream>
using namespace std;

void makeBox(int rows, int columns, int thickness) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < thickness; j++) {
            cout << "#";
        }
        for (int k = 0; k <  columns; k++) {
            cout << " ";
        }
        for (int l = 0; l < thickness; l++) {
            cout << "#";
        }
        cout << endl;
    }
    for (int j = 0; j < thickness/2; j++) {
        for (int k = 0; k < columns + (2*thickness); k++) {
            cout << "#";
        }
        cout << endl;
    }
}

int main() {
    const int ROWS = 20, COLUMNS = 10, THICKNESS = 2;
    makeBox(ROWS, COLUMNS, THICKNESS);

    return 0;
}