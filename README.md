# Project2 description given by Instructor:

Water Utility Companies charge different amounts per gallon depending on the  consumption. The customers will save money if they save water – that is good additional motivation! A  simplified method that a company would use to calculate the billed amount will be implemented in this  project assignment.

Problem definition:
1. Design and implement a program to compute and display information for a utility company that
supplies water to its customers. For a specified customer, the program will compute and display 
the amount of money that the customer will be billed for water usage during the current billing 
period.
2. The program will prompt the user to enter three values (in the following order):
a. The customer's code (a character) using a string ‘Enter customer code (R, C, or I):’ 
Use variable name customer_code to store the code.
b. The customer's beginning meter reading (a positive integer value) using a string ‘Enter 
beginning reading (between 0 and 999999999):’
Use variable name start_reading to store the beginning meter value. 
 
c. The customer's ending meter reading (a positive integer value) using a string ‘Enter ending 
reading (between 0 and 999999999):’
Use variable name end_reading to store the ending meter value. 
3. Validate
a. The program is required to check the customer’s code immediately after the user 
provides the input value. Recognize upper case only letters for customer codes (“R”, “C”, 
ECS 174 
Copyright © 2022 Susan Tabbaa Nachawati, Ph.D. & Jelena Trajkovic, Ph.D. 
and “I”). Any letter that is not defined as a code, input is considered an invalid input. If 
the code is not acceptable, print 'Invalid input (customer code)' and finish the program. 
Do not ask for other inputs.
a. If the customer's code is correct, the user should proceed to input both the start and end 
readings. The program is required to check the user-supplied start and end reading 
immediately after both input values are read. Validate that both values are within the 
range [0, 999999999]. Any value outside this range is considered invalid. If any of the 
values for the readings are invalid, print ' Invalid input (beginning or ending reading value 
is out of the range)' and finish the program. Do not ask the user to try again or perform 
any computation.
4. The program will first compute the gallons of water used by the customer during the current 
billing period. Use a variable named used_gallons to store the value for computed water 
usage.
5. The meter's dial has nine digits and records tenths of a gallon: therefore eight leftmost digits 
represent gallons, and the rightmost digit represents a tenth of a gallon. 
For example, the beginning reading 444400003 represents 44440000.3 gallons, and the ending 
444400135 represents 44440013.5. Consequently, 444400135 - 444400003 = 132 represents 13.2 
gallons of water used during the billing period. Alternatively, you can compute the used water as 
44440013.5 - 44440000.3 = 13.2. 
6. Next, the program will compute the amount of money that the customer will be billed, based on 
the customer's code and water usage, using the information below. Use a variable named 
to_bill to store the value for the computed billing amount.
 Code 'R' (residential):
 $5.00 plus $0.0005 per gallon used
 Code 'C' (commercial):
 $1000.00 for 4 million gallons or less, and $0.00025 for each additional gallon used
 Code 'I' (industrial):
$1000.00 if usage does not exceed 4 million gallons, 
$2000.00 if usage exceeds 4 million gallons but does not exceed 10 million gallons, and 
$2000.00 plus $0.00025 for each additional gallon that exceeds 10 million gallons.
7. For each run, the program will display a summary with the following information:
 a. The customer's code, using the string ‘Customer code: ‘ (and one space after this string) 
followed by the code that the customer provided
for example ‘Customer code: R’
 b. The customer's beginning meter reading, using the string 'Beginning reading value in gallons 
and tenths of gallon' (and one space after this string) followed by the reading formatted as gallons and 
tenths of a gallon
for example ‘Beginning reading value in gallons and tenths of gallon 123.0’
ECS 174 

 c. The customer's ending meter reading, using sing the string 'Ending reading value in gallons and 
tenths of gallon' (and one space after this string) followed by the reading formatted as gallons and tenths 
of a gallon
for example ‘Ending reading value in gallons and tenths of gallon 223.5’ 
NOTE for b. & c. For both variables start_reading and end_reading, please keep the 
original value in the variable, but print as gallons and tenths of a gallon. 
 d. The gallons of water used by the customer, using a string ‘Gallons of water used:’ (and one 
space after this string) followed by computed water used formatted as gallons and tenths of a gallon
for example ‘Gallons of water used: 100.5‘ 
 
 e. The amount of money billed to the customer ‘Amount billed:’ (and one space after this string) 
followed by the billed amount with $ sing before the amount and two digits to the right of the decimal 
point
for example ‘Amount billed: $5.05’ 
Please Note:
Since the meter’s dial only has nine digits, the reading at the end of the billing period may be less than 
the reading at the beginning of the billing period. This kind of meter is called a “wrap-around counter,“ 
as it restarts counting from 0 once the max value is reached.
Example: the end meter reading is less than the beginning meter reading.
If we have a beginning meter reading of 999999994 and an ending meter reading of 000000005:
When adding one to the MAX possible reading of the meter we get:
 999999999
+ 1
---------------------
1000000000  (MAX + 1)
The leading (leftmost) 1 is an overflow because we have space to represent only 9 digits on the meter (not 
10 digits as it is needed here0.
To compute how much was used in this case, start by subtracting the beginning meter reading from (MAX 
+ 1): 
 1000000000
- 999999994 
--------------------
 0000000006  this is how much we spent till the meter became 000000000
Now, we need to add this to the end meter reading value:
 000000006 
+ 000000005
-----------------------
 000000011
The total is 000000011, but remember that the rightmost digit is 1/10the of the gallon, so the water 
consumption is 1.6 gallons.
Steps: 
0. You are doing pair programming. Both teammates will share the responsibility of designing the solution, 
implementing (coding, debugging, and testing), and writing the report. One partner will write or type 
while the other is observing and commenting. The partners need to keep discussing how to solve each 
step of the problem. After about 2-3 minutes, the partners will switch roles. And keep switching until the 
project is done and the report is written.
1. Outline what are the inputs and output(s) of your code on paper (for the report).
2. Write down how will you compute the outputs using the inputs.
3. PrairieLearn will give a max number of points if you get the solutions right the first time. It pays off that 
you start your development in IDLE/Pycharm/online compiler. To implement any of the projects, create a 
file in the development environment. 
a) Start by implementing reading value for one input variable using input() function. Print the 
value of that variable. Test and correct any bugs. Remove the print of the variable when you are sure the 
input works. 
b) Validate the input for the first variable (see Problem definition 3. Validate)
c ) Repeat the process for all input variables
d) Compute the value(s) of the output and print the values on-screen using the print() function. 
At this point, you can just put each variable in a separate row – you are checking for the correctness of 
the computation. No need to format the input now.
e) Observe the format of the desired output. Modify the print statements such that your output 
matches desired output. Remember to match the whitespace. 
f) To allow for automatic grading use the variable names as provided in this document and the 
editor in PL. If any discrepancy, notify the instructor. 
Note: Nonfunctional requirements will help other programmers or you (if you were to read the code a 
year after it’s been written), understand what the intention and the steps were for each part of the code. 
Nonfunctional requirements for this code are :
• Add comments to your code.
• If variable names are not specified, use meaningful variable names, that adhere to the good 
coding practices (as reviewed in lectures).
4. Test your code using the sample run inputs.
5. Think about other test cases: be creative! Can you test all the cases that a user can input (why or why 
not)? How do you select significant test cases? Add at least 5 more test cases on your own.
