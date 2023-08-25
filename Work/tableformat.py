# tableformat.py

class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings. 
        """
        raise NotImplementedError()
    
    def row(self, rowdata):
        """
        Emit a single row of table data. 
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers), end=" ")
        print()
    
    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()

class CSVTableFormatter(TableFormatter):
    """
    Emit a table in CSV format
    """
    def headings(self, headers):
        print(",".join(headers))
    
    def row(self, rowdata):
        print(",".join(rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Emit a table in HTML format
    """
    def headings(self, headers):
        tagged_headers = "</th><th>".join(headers)
        print("<tr><th>" + tagged_headers + "</th></tr>")

    def row(self, rowdata):
        tagged_row = "</td><td>".join(rowdata)
        print("<tr><td>" + tagged_row + "</td></tr>")

def create_formatter(fmt):
    """
    Create a formatter based on a selected format
    """
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {fmt}")