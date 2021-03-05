17. Letter Combinations of a Phone Number [Medium]

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

<br>

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

<br>

## Examples

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

<br>

#My Approach

Get a single digit and get all combinations

and if there are remaining digits

recurse and add all the cominations to previos combinations

Space and Time complexity is:

O(3 ^ N and 4 ^ N)
