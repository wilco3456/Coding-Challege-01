import csv
import sys

def process_shifts(path_to_csv):
    """

    :param path_to_csv: The path to the work_shift.csv
    :type string:
    :return: A dictionary with time as key (string) with format %H:%M
        (e.g. "18:00") and cost as value (Number)
    For example, it should be something like :
    {
        "17:00": 50,
        "22:00: 40,
    }
    In other words, for the hour beginning at 17:00, labour cost was
    50 pounds
    :rtype dict:
    """

    # Open work_shifts.csv into a dictionary
    with open(path_to_csv, mode='r') as csv_file:
        work_shifts = {}
        csv_reader = csv.DictReader(csv_file)

        i = 0   # Counter
        for record in csv_reader:
            work_shifts[i] = [record.get("start_time", "none"), record.get("pay_rate"), record.get("end_time"), record.get("break_notes")]
            i += 1

    #print(work_shifts)
    
    return work_shifts


def process_sales(path_to_csv):
    """

    :param path_to_csv: The path to the transactions.csv
    :type string:
    :return: A dictionary with time (string) with format %H:%M as key and
    sales as value (string),
    and corresponding value with format %H:%M (e.g. "18:00"),
    and type float)
    For example, it should be something like :
    {
        "17:00": 250,
        "22:00": 0,
    },
    This means, for the hour beginning at 17:00, the sales were 250 dollars
    and for the hour beginning at 22:00, the sales were 0.

    :rtype dict:
    """
    
    # Open transactions.csv into a dictionary
    with open(path_to_csv, mode='r') as csv_file:
        transactions = {}
        csv_reader = csv.DictReader(csv_file)

        i = 0
        for record in csv_reader:
            transactions[i] = [record.get("time", "none"),record.get("amount")]
            i += 1

    #print(transactions)
    
    return transactions

def compute_percentage(shifts, sales):
    """

    :param shifts:
    :type shifts: dict
    :param sales:
    :type sales: dict
    :return: A dictionary with time as key (string) with format %H:%M and
    percentage of labour cost per sales as value (float),
    If the sales are null, then return -cost instead of percentage
    For example, it should be something like :
    {
        "17:00": 20,
        "22:00": -40,
    }
    :rtype: dict
    """
    
    totals = {}

    # Calculates the amount of sales for each hour
    for key,val in sales.items():
        time_pair = val[0].split(":")   # Splits the time into hours and mins by (":")
        hour = time_pair[0]
        hour_str = str(hour) + ":00"
        
        if hour_str not in totals:
            totals[hour_str] = [1]      # Sets the dictionary counter
        else:
            totals[hour_str][0] += 1    # Increments the dictionary counter
    
    #print(totals)

    # Calculates the total cost of labour for the hour
    for key,val in totals.items():
        totals_time_pair = key.split(":")   # Splits the time into hours and mins by (":")
        totals_hour = totals_time_pair[0]

        for key0,val0 in shifts.items():
            start_time_pair = val0[0].split(":")
            start_hour = start_time_pair[0]
            
            end_time_pair = val0[2].split(":")
            end_hour = end_time_pair[0]

            # Checks if the sales time is within the labour hour boundaries
            if totals_hour >= start_hour and totals_hour <= end_hour:
                if len(val) == 1:
                    totals[key].append(val0[1])     # Sets the cost of labour for the hour
                else:
                    totals[key][1] = float(totals[key][1]) + float(val0[1])     # Increments the cost of labour for the hour
                
                #print(key)
                #print(val0)

    # Calculates the cost of labour as a percentage of sales
    for key,val in totals.items():
        # ("cost of labour for the hour") / ("the amount of sales for each hour")
        percentage_labour_sales = float(val[1]) / int(val[0])
        totals[key].append(percentage_labour_sales)

    #print(totals)

    #Print the table header in 12 space format
    s = '%-12s %-12s %-12s %-12s' % ("Hour", "Sales", "Labour", "%")
    print(s)

    for key,val in totals.items():
        s = '%-12s %-12s %-12s %-12s' % (key, val[0], val[1], val[2])
        print(s)
    print("")
    
    return totals

def best_and_worst_hour(percentages):
    """

    Args:
    percentages: output of compute_percentage
    Return: list of strings, the first element should be the best hour,
    the second (and last) element should be the worst hour. Hour are
    represented by string with format %H:%M
    e.g. ["18:00", "20:00"]

    """
    
    first_key = list(percentages.keys())[0]     # First key in the percentage dictionary
    best = percentages[first_key][2]
    worst = percentages[first_key][2]

    b_hour = first_key
    w_hour = first_key

    # Selects the lowest and highest costs of labour as a percentage of sales
    for key,val in percentages.items():
        if val[2] > best:
            best = val[2]
            b_hour = key
        if val[2] < worst:
            worst = val[2]
            w_hour = key        

    #print(b_hour)
    #print(w_hour)

    #Returns the first occuring Best Hour and the first occuring Worst Hour
    return [b_hour, w_hour]

def main(path_to_shifts, path_to_sales):
    shifts_processed = process_shifts(path_to_shifts)
    sales_processed = process_sales(path_to_sales)
    percentages = compute_percentage(shifts_processed, sales_processed)
    best_hour, worst_hour = best_and_worst_hour(percentages)
    return best_hour, worst_hour

if __name__ == '__main__':
    # You can change this to test your code, it will not be used
    path_to_sales = sys.argv[2]
    path_to_shifts = sys.argv[1]
    best_hour, worst_hour = main(path_to_shifts, path_to_sales)

    print("Best Hour: " + str(best_hour))
    print("Worst Hour: " + str(worst_hour))
