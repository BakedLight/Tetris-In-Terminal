#include <iostream>
#include <windows.h>
#include <conio.h>
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

void gotoRow(int targetRow) {
    HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO info;
    GetConsoleScreenBufferInfo(h, &info);
    SetConsoleCursorPosition(h, { 0, (SHORT)targetRow });
}   

int main() {
    const int ROWS = 10, COLUMNS = 10, THICKNESS = 2;
    // makeBox(ROWS, COLUMNS, THICKNESS);

    // Update Loop
    while (true){
        // Check if a key was pressed without blocking
        if (_kbhit()) {
            char key = getch(); // Get the char immediately
            if (key == 'K') {
                cout << "Left" << endl;
            }
            else if (key == 'M') {
                cout << "Right" << endl;
            }
            else if (key == 'P') {
                cout << "Down" << endl;
            }
            else if (key == 'H') {
                cout << "Up" << endl;
            }
        }

        // Other code here

    }

    return 0;
}