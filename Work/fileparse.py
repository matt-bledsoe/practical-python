# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None):
    '''
    Parse a csv file into a list of records 
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        # Read the headers
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        
        records = []
        for row in rows:
            if not row: # Skip rows with no data
                continue

            # Select correct elements
            if select:
                row = [row[index] for index in indices]
            
            # Type conversion
            if types:
                row = [func(val) for func, val in zip(types, row)]
            record = dict(zip(headers, row))
            records.append(record)
        

    
    return records
