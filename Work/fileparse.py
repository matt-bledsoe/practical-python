# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file, select=None, types=None, has_headers=True, delimiter=",",
              silence_errors=False):
    '''
    Parse a csv file into a list of records 
    '''
    # Can't select without headers
    if select and not has_headers:
        raise RuntimeError("Cannot select columns without headers")
    
    rows = csv.reader(file, delimiter=delimiter)
        
    headers = next(rows) if has_headers else []
    
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for nrow, row in enumerate(rows, 1):
        if not row: # Skip rows with no data
            continue
        # Select correct elements
        if select:
            row = [row[index] for index in indices]
        # Type conversion
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_errors:
                    continue
                else:
                    print(f"Row {nrow}: Couldn't convert {row}")
                    print(f"Row {nrow}: {e}")
        
        # If there are headers create a dict, else make a tuple
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    
    return records
