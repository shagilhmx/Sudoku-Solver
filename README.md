## -> [A VIDEO SHOWING HOW THE PROGRAM EXACTLY WORKS](https://drive.google.com/file/d/1hQUiYHpJQpClfQFXCh4waUWeijJky7jv/view?usp=sharing) <-

# Real-Time-Webcam-Sudoku-Solver

## Table of contents
* [What is Real Time Webcam Sudoku Solver?](#What-is-Real-Time-Webcam-Sudoku-Solver?)
* [Code requirements](#Code-requirements)
* [Installation](#Installation)
* [Usage](#Usage)
* [How does it work?](#How-does-it-work?)

## What is Real Time Webcam Sudoku Solver?
This is a program written in Python that connects with your webcam and tries to solve the [sudoku](https://en.wikipedia.org/wiki/Sudoku). 
I was inspired by [this project](https://github.com/MateuszKozlowski1124/Real-Time-Webcam-Sudoku-Solver)

## Code requirements
Python 3.8 with following modules installed:
* NumPy 1.18 
* TensorFlow 2.3 
* Keras 2.4
* Matplotlib 3.3 (if you want to train a model that recognizes digits by your own)
* OpenCV 4.4

## Installation
Simply download the project as a compressed folder or clone it.
To check for yourself how the program works you don't have to train your CNN model. 
Already trained is saved in Models folder. 
Using Terminal/Command Prompt navigate to the correct directory and run main_file.py using the following command: python main_file.py

## Usage
After running main_file.py you should see a window that shows live feed from your webcam.
Now place a sudoku in the webcam's field of view.
And that's all. In the window should appear a solution.
If the solution doesn't appear, or the program doesn't even locate the sudoku, try to move it closer/further to the webcam. If it doesn't help, you may need to improve the lighting quality.

## How does it work?
Short explanation - algorithm:
* read a frame from a webcam
* convert that frame into grayscale
* binarize that frame
* find all external contours
* get the biggest quadrangle from that contours
* apply warp transform (bird eye view) on the biggest quadrangle
* split that quadrangle into 81 small boxes
* check which boxes contain digits
* extract digits from boxes that aren't empty
* prepare that digits for a CNN model
* while not solved and iterations of the loop <= 4:
	* rotate the digits by (90 * current iteration) degrees
	* classify the digits using a CNN model
	* if an average probability is too low go to the next iteration of the loop
	* compare the digits with a previous solution
	* if the digits are part of the previous solution then we don't need to solve the sudoku again - break the loop
	* try to solve the sudoku
	* if solved correctly break the loop
* return a copy of the frame (with a solution if any were found)