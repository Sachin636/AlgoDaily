# 1329. Sort the Matrix Diagonally [Medium]

https://leetcode.com/problems/sort-the-matrix-diagonally/

<br>

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

<br>

## My Solution

Just store the indices of the diagonals in the list.

And call sort method on each stored list of indices

## Note : If you improve the sorting algorithm runtime will improve.
