#include <iostream>
#include <windows.h>
#include <conio.h>
#include <thread>
#include <chrono>

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

void set_cursor(int x = 0 , int y = 0)
{
    HANDLE handle;
    COORD coordinates;
    handle = GetStdHandle(STD_OUTPUT_HANDLE);
    coordinates.X = x;
    coordinates.Y = y;
    SetConsoleCursorPosition ( handle , coordinates );
}

int main() {
    const int ROWS = 10, COLUMNS = 10, THICKNESS = 2;
    
    // makeBox(ROWS, COLUMNS, THICKNESS);

    // Update Loop
    while (true){

        // Check if a key was pressed without blocking the execution
        if (_kbhit()) {
            char key = getch(); // Get the char immediately
            if (key == 'K') {
                cout << "Left" << endl;
                set_cursor(0, 1);
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