from follow import follow
import report
import tableformat
import csv

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0, 1, 4]] for row in rows)
    rows = ([func(val) for func, val in zip([str, float, float], row)] for row in rows)
    rows = (dict(zip(["name", "price", "change"], row)) for row in rows)
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile) 
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio)
    table_format = tableformat.create_formatter(fmt)
    table_format.headings(["Name", "Price", "Change"])
    for row in rows:
        table_format.row([f"{row['name']}", f"{row['price']}", 
                          f"{row['change']}"])

def main(argv):
    ticker(argv[1], argv[2], argv[3])

# if __name__ == "__main__":
    # import sys
    # main(sys.argv)
