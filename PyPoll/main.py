# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:17:51 2019

@author: Maverick Sanchez
"""

import os, csv

def read_file():
    dict_holder = {}
    csv_path = os.path.join ("Resources","election_data.csv")    
    with open(csv_path, newline='', encoding="utf-8") as csv_file:
        next(csv.reader(csv_file)) #Skip the header/Move cursor
        for row in csv.reader(csv_file):
            dict_holder[row[0]] = [row[1], row[2]]
        return dict_holder


   
def write_file():
    output_path = os.path.join( "election_data_summary.csv")
    
    with open(output_path, "w", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(['Election Results'])
        csv_writer.writerow(['-------------------------'])
        csv_writer.writerow([f'Total Votes: {total_cast} '])
        csv_writer.writerow(['-------------------------'])
        for k, v in results.items():   
            csv_writer.writerow([f'{k} : {float((v/total_cast))*100:.3f}% ({v})'])
        csv_writer.writerow(['-------------------------']),
        csv_writer.writerow([f'Winner: {max(results, key=results.get)}'])
        csv_writer.writerow(['-------------------------'])
    

if __name__ == '__main__':
    election_data_dict = read_file()
    results = {}
    
    total_cast = len(set(election_data_dict.keys()))
    
    counter = 0
    for k, v in election_data_dict.items():    
        if v[1] not in results:
            results[v[1]] = 1 #initial entry, so 1
        else:
            counter = int(results.get(v[1])) + 1
            results[v[1]] = counter
            counter = 0

    results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
    
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {total_cast} ')
    print(f'-------------------------')
    for k, v in results.items():   
        print(f'{k} : {float((v/total_cast))*100:.3f}% ({v})')    
    print(f'-------------------------')
    print(f'Winner: {max(results, key=results.get)}')
    print(f'-------------------------')
    print('Writing to file...')    
    write_file()
    print('Program completed.') 
