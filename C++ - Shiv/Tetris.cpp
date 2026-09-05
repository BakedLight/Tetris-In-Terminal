// STRUCTURE:
/*
---------------------------------------------------------------------
Thread 1 - Input check
this thread will be used to check input events when they occur and move the blocked horizontally to update the location
this thread is continuously gonna work regardless of thread 2's condition on whether it is paused or running
---------------------------------------------------------------------
Thread 2 - Vertical movement / Gravity
this thread will be used to move blocks down by one line each 0.3 seconds and 0.1 second when player intentionally wants blocks to fall faster
so this thread will be paused for the time (0.3 or 0.1 sec) and then update and get paused again
---------------------------------------------------------------------
Screen Updation or Frame Updation:
frame is going to be updated from top to bottom (i.e. the cursor will be moved to start of first line during each frame's drawing process)
both threads will update frames using different algorithms
thread 1: This will update each line just purely based on left/right movement or rotation of blocks
thread 2: this will update each line as just being the upper line brought down (simulating blocks moving down) based on varying speeds
---------------------------------------------------------------------
Collisions or collision detection:
idk how to do ts, still gotta figure this part out
---------------------------------------------------------------------
*/

#include <iostream>
#include <vector>
#include <windows.h>
#include <conio.h>
#include <thread>
#include <chrono>

using namespace std;

void print2DVector (vector<vector<int>> vec) {
    for (int i = 0; i < size(vec); i++) {
        for (int j = 0; j < size(vec[0]); j++) {
            cout << vec[i][j] << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> vectorTranspose (vector<vector<int>> block) {
    int rows = size(block[0]); // returns 3 in t block's case
    int columns = size (block);
    vector<vector<int>> transposedBlock(rows, vector<int>(columns, 0));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            transposedBlock[i][(columns-j-1)] = block[j][i];
        }
    }
    return transposedBlock;
}

void makeBox (int rows, int columns, int thickness) {
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

// void timedUpdation () {
//     while (true){
//         // cout << "Fall down" << endl;
//         // this_thread::sleep_for(chrono::milliseconds(500));
//     }
// }

// void instantUpdation () {
//     while(true) {

//         // Check if a key was pressed without blocking the execution
//         if (_kbhit()) {
//             char key = getch(); // Get the char immediately
//             if (key == 'K') {
//                 cout << "Left" << endl;
//             }
//             else if (key == 'M') {
//                 cout << "Right" << endl;
//             }
//             else if (key == 'P') {
//                 cout << "Down" << endl;
//             }
//             else if (key == 'H') {
//                 cout << "Up" << endl;
//             }
//         }
//     }
// }

int main() {

    vector<vector<int>> lBlock = {
        {1, 1, 1},
        {1, 0, 0}
    };

    vector<vector<int>> transported = vectorTranspose(lBlock);
    

    const int ROWS = 10, COLUMNS = 10, THICKNESS = 2;
    makeBox(ROWS, COLUMNS, THICKNESS);


    while(true) {

        // Check if a key was pressed without blocking the execution
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

    // if (thread1.joinable()) thread1.join();
    // if (thread2.joinable()) thread2.join();

    return 0;
}