# Sudoku-BackTracking
## Use Back Tracking to solve Sudoku.
### Why?
  I was asked to implement a sudoku game in a interview. Back then, I had no idea abouy what sudoku is and how to make a routine to solve sudoku. But I believe that solving sudoku is really worth to try.
### How?
  We can assign numbers to empty cells, before assigning numbers, we need to check if the number is valid to assign. We need to check if the number is nor present in current row, column and 3x3 square([sudoku rule](http://www.counton.org/sudoku/rules-of-sudoku.php)). If the number is good, we recursively to check if this assignment will lead to correct result. One thing needs to be mentioned that each sudoku may have mutilple solutions.
 ### Big-O?
  O(n^m) where n is size of sudoku (i.e.in classic sudoku game, n is 9), m is blank cells. Also solving sudoku is NP-Hard problem.
 ### How to test it?
  I create a simple UI for this program using Tkinter. 0's for empty cells, you can type any sudoku question into that grid. After entering all data, you can just hit solve button, it will generate a solution for you sudoku question.
 ### Any improvment?
  Using dancing links with algorithm X to solve sudoku will be more faster than backtracking. Also it is hard to generate a sudoku question. Solving is easy, generating is hard. You need create a full sudoku grid, and check if it is valid.
  
#### TODO:
  Make an iOS app that can solve sudoku game.
  1. app can generate questions.(if it is hard to generate, we can store question on cloud)
  2. app can solve problems.
  3. app can cast image into grid(OCR) so that user do not need to maually type in problem.