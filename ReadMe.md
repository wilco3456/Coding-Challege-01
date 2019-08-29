# Coding Challenge

## Explanation
The most and least profitable hour of the day for a given restaurant must be found when looking at labour cost.  
Two csvs will be provided, one describing the shifts, and one describing the hourly sales.

### LABOUR DATA
A shift will include the pay-rate (per hour), the start and end time, and a text field where the manager will enter break info. This may vary depending on the individual manager.

For example:  
{  
    'break_notes': '15-18',  
    'start_time': '10:00',  
    'end_time': '23:00',  
    'pay_rate': 10.0  
}  
The data given shows a shift started at 10AM and ended at 11PM. However, the break_notes "15-18" indicates that the staff member took a 3 hour break in the middle of the day (when they would not be paid). The employee was paid £10 per hour.


### SALES DATA
This shows you a set of transactions:

For example:  
[  
    {  
        'time' : '10:31',  
        'amount' : 50.32  
    }  
]  
The different metrics for the different hours must be computed, such as the total sales during this hour, the cost of labour for this hour, and the cost of labour as a percentage of sales.

For example:

Hour	Sales	Labour	%  
7:00	100	    30	    30%  
8:00	300	    60	    20%  
Lastly, the hour which was the best and the worst in terms of labour cost as a percentage of sales must be output.
