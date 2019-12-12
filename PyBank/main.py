# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:06:26 2019

@author: Maverick Sanchez
"""

import os, csv

#csv_path = os.path.join("../Resources/accounting.csv")
csv_path = os.path.join ("Resources","budget_data.csv")

with open(csv_path, newline='', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #print(csv_reader)
    csv_header = next(csv_reader)
    print(csv_header)
    #for row in csv_reader:
        #print(row)
