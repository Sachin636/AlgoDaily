# 990. Satisfiability of Equality Equations

Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.


# Example

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

Input: ["a==b","b!=c","c==a"]
Output: false

Input: ["a==b","b==c","a==c"]
Output: true


# Solution

First Union all the equation containing `==`

Then check all the equations with `!=`.

If there is a contradiction return False.

else return True.