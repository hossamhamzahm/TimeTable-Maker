# TimeTable-Maker

*TimeTable-Maker* is a console program that uses backtracking algorithm to generate all possible timetables for the specified courses. 
<br>
On startup, the program reads a large CSV file that contains the university schedule then it asks the user to enter the wanted courses. Finally, it starts backtracking to generate all possible timetables from the entered courses.



>**Disclaimer** This program was written before but with very bad complexity O(N^6) where n is the number of courses. I refactored the algorithm to use backtracking instead of many nested for loops which results in a better complexity O(!6). 
