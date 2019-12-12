# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:06:26 2019
@author: Maverick Sanchez
"""

import os, csv

def read_file():
    csv_path = os.path.join ("Resources","budget_data.csv")    
    with open(csv_path, newline='', encoding="utf-8") as csv_file:
        next(csv.reader(csv_file)) #Skip the header/Move cursor
        return dict(csv.reader(csv_file)) #Return dictionary of key - values


def delta_average():
    previous = 0
    diff = 0
    average_running = {}
    for k, v in csv_reader_dict_main.items():
        if previous != 0: 
            diff =  float(v) - previous
            average_running[k] = diff
        previous = float(v)
        
    return average_running
    
def write_file():
    output_path = os.path.join( "budget_summary.csv")
    
    with open(output_path, "w", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
    
        csv_writer.writerows([
                            ["Financial Analysis", ""],
                            ["Total Months: ", total_months],
                            ["Total: ", f'${total_amount}'],
                            ["Average  Change: ", f'${delta:.2f}'],
                            ["Greatest Increase in Profits: ", f'{max_increase_year[0]} (${int(max_increase)})' ],
                            ["Greatest Decrease in Profits: ", f'{min_increase_year[0]} (${int(min_increase)})'],
                            ["----------------------------", ""]
                            ])
    

# Main function call, I did it modular approach
if __name__ == "__main__":
    csv_reader_dict_main = read_file()
    value_computations = {}
    total_months = len(set(csv_reader_dict_main.keys())) # Count unique keys (Dates) using Set
    total_amount = sum([int(a) for a in csv_reader_dict_main.values()]) # Sum of all values (budget amount)
    value_computations = delta_average()
    delta = sum([float(a) for a in value_computations.values()])/(len(value_computations))
    max_increase = max(value_computations.values())
    max_increase_year = [k for k,v in value_computations.items() if v == max_increase]
    min_increase = min(value_computations.values())
    min_increase_year = [k for k,v in value_computations.items() if v == min_increase]
    
    print('Financial Analysis')
    print('----------------------------\n')
    print(f'Total Months: {total_months}') 
    print(f'Total: ${total_amount}')
    print(f'Average  Change: ${delta:.2f}')
    print(f'Greatest Increase in Profits: {max_increase_year[0]} (${int(max_increase)}) ')
    print(f'Greatest Decrease in Profits: {min_increase_year[0]} (${int(min_increase)})')
    print(f'\n----------------------------')
    print('Writing to file...') 
    
    
    write_file()
    
    print('Program completed.') 
