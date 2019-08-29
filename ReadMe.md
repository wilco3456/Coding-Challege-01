# Coding Challenge

## Explanation
The most and least profitable hour of the day for a given restaurant must be found when looking at labour cost.  
Two csvs will be provided, one describing the shifts, and one describing the hourly sales.

### LABOUR DATA
A shift will include the pay-rate (per hour), the start and end time, and a text field where the manager will enter break info. This may vary depending on the individual manager.

For example:
<pre>
{  
    'break_notes': '15-18',  
    'start_time': '10:00',  
    'end_time': '23:00',  
    'pay_rate': 10.0  
}  
</pre>

The data given shows a shift started at 10AM and ended at 11PM. However, the break_notes "15-18" indicates that the staff member took a 3 hour break in the middle of the day (when they would not be paid). The employee was paid £10 per hour.

### SALES DATA
This shows you a set of transactions:

For example: 
<pre>
{  
    'time' : '10:31',  
    'amount' : 50.32  
} 
</pre>

The different metrics for the different hours must be computed, such as the total sales during this hour, the cost of labour for this hour, and the cost of labour as a percentage of sales.

For example:
<pre>
Hour	Sales   Labour  %  
7:00	100     30      30%  
8:00	300     60      20%  
</pre>

Lastly, the hour which was the best and the worst in terms of labour cost as a percentage of sales must be output.

## Platform Recommendation:
* This program has been run on Windows 10.0.15063 build 15063 and Mac OS X, developed using Python version 3.7, Other systems have not been tested, and it is advised to have caution with untested OS.

## To Start:
* Open a command line window and navigate to the folder holding the program's *.py* file.
* Then type: python coding_challege.py work_shifts.csv transactions.csv, which should run the program.

## Example Runtime
<pre>
C\...\coding_challenge_py>python coding_challege.py work_shifts.csv transactions.csv

Hour         Sales        Labour       %
19:00        2            66.0         33.0
14:00        2            74.0         37.0
17:00        1            64.0         64.0
12:00        3            74.0         24.6666666667
21:00        1            66.0         66.0
15:00        1            74.0         74.0
10:00        2            50.0         25.0
13:00        2            74.0         37.0
18:00        3            76.0         25.3333333333
16:00        1            74.0         74.0
11:00        2            60.0         30.0

Best Hour: 15:00
Worst Hour: 12:00
</pre>
