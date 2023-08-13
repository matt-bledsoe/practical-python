# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    '''
    Parse a csv file into a list of records 
    '''
    # Can't select without headers
    if select and ~has_headers:
        raise RuntimeError("Cannot select columns without headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
         
        if has_headers:
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
            
            # If there are headers create a dict, else make a tuple
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    
    return records
