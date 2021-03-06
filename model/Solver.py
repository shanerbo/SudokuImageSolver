
from tkinter import *
from tkinter import messagebox
import numpy as np
import cv2
import pylab as pl
import numpy as np

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        
    def printGrid(self):
        for i in range(len(self.sudoku)):
            if i%3 == 0:
                print('.-----------------------.')
            for j in range(len((self.sudoku)[0])):
                if j%3 == 0:
                    print('|', end=' ')
                print(self.sudoku[i][j], end=' ')
                if j == 8:
                    print('|')
        print('.-----------------------.')
        
    def validCol(self, c, n):
        for i in range(len(self.sudoku)):
            if self.sudoku[i][c] == n:
                return False
        return True
    
    def validRow(self, r, n):
        for i in range(len(self.sudoku)):
            if self.sudoku[r][i] == n:
                return False
        return True
    
    def boxStartPoint(self, r, c):
        return (r//3)*3, (c//3)*3
    
    
    def validBox(self, r, c, n):
        boxRow, boxCol = self.boxStartPoint(r, c)
        for i in range(3):
            for j in range(3):
                if self.sudoku[boxRow+i][boxCol+j] == n:
                    return False
        return True
    
    def validEntry(self, r, c, n):
        if self.validCol(c, n) and self.validRow(r, n) and self.validBox(r, c, n):
            return True
        else:
            return False
        
    def findEntry(self, loc):
        for i in range(len(self.sudoku)):
            for j in range(len((self.sudoku)[0])):
                if self.sudoku[i][j] == 0:
                    loc[0] = i
                    loc[1] = j
                    return True
        return False

    def solver(self):
        loc = [0, 0]
        if not self.findEntry(loc):
            return True
        r = loc[0]
        c = loc[1]
        for i in range(1, 10):
            if self.validEntry(r, c, i):
                self.sudoku[r][c] = i
                if self.solver():
                    return True
                self.sudoku[r][c] = 0
        return False