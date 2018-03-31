#include <cstdio>
#include <cstdlib>
#include <iostream>

#define SIZE 9

unsigned int board[SIZE][SIZE];

void loadBoard() {
	FILE* fp = std::fopen("board.txt", "r");
	if (!fp) {
		std::perror("File opening failed");
	}

	int c; // note: int, not char, required to handle EOF (-1)
	uint8_t row = 0, col = 0;

    while ((c = std::fgetc(fp)) != EOF) {
    	int num = c - '0';

    	if (num > 0 && num <= 9) {
    		board[row][col++] = num;
    	} else if (c == '.') {
    		board[row][col++] = 0;
    	} else if (c == '\n') {
    		if (col == SIZE) {
    			++row;
    			col = 0;
    		} else {
    			std::cout << "Found a newline while col was " << (unsigned int)col << "...\n";
    			std::cout << "Going to skip incrementing row/col.\n";
    		}
    	}
    }
    for (uint8_t i = 0U; i < SIZE; ++i) {
    	for (uint8_t j = 0U; j < SIZE; ++j) {
    		std::cout << board[i][j] << ' ';
    	}
    	std::cout << '\n';
    }
}

bool isValidRowInsert(uint8_t row, uint8_t num) {
	for (uint8_t col = 0U; col < SIZE; ++col) {
		if (board[row][col] == num) {
			// already exists
			return false;
		}
	}
	return true;
}

bool isValidColumnInsert(uint8_t col, uint8_t num) {
	for (uint8_t row = 0U; row < SIZE; ++row) {
		if (board[row][col] == num) {
			// already exists
			return false;
		}
	}
	return true;
}

bool isValidSquareInsert(uint8_t row, uint8_t col, uint8_t num) {
	for (uint8_t i = (row / 3) * 3; i < ((row+3) / 3) * 3; ++i) {
		for (uint8_t j = (col / 3) * 3; j < ((col+3) / 3) * 3; ++j) {
			if (board[i][j] == num) {
				// already exists
				return false;
			}
		}
	}
	return true;
}

bool isValidMove(uint8_t row, uint8_t col, uint8_t num) {
	return isValidRowInsert(row, num) &&
		isValidColumnInsert(col, num) &&
		isValidSquareInsert(row, col, num);
}


int main() {
	loadBoard();
	// bool done = false;

	// while (!done) {
	// 	done = true;

	// 	for (uint8_t row = 0; row < SIZE; ++row) {
	// 		for (uint8_t col = 0; col < SIZE; ++col) {
	// 			if (board[row][col] == 0) {

	// 			}
	// 		}
	// 	}
	// }
	std::cout << (isValidMove(0,0,1) ? "true" : "false") << '\n';
}


