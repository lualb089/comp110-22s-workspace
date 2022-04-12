"""Dictionary related utility functions."""

__author__ = "730480432"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in table:
        new_list: list[str] = []
        i: int = 0
        if rows >= len(table[column]):
            return table

        while i < rows:
            new_list.append(table[column][i])
            i += 1
        result[column] = new_list

    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for value in names:
        result[value] = table[value]
    
    return result


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for key in first_table:
        result[key] = first_table[key]
    
    for key in second_table:
        if key in result:
            result[key] += second_table[key]
        else:
            result[key] = second_table[key]
    
    return result


def count(table: list[str]) -> dict[str, int]:
    "Given a list, will produce a dict that is unique to it."
    result: dict[str, int] = {}

    for value in table:
        if value in result:
            result[value] += 1
        
        else:
            result[value] = 1
    
    return result


def helper(table: list[dict[str, str]], column_name: str) -> list[dict[str, str]]:
    """Lopp through all students data in list and keep needed data."""
    result: list[dict[str, str]] = []

    for student in table:
        if int(student[column_name]) >= 5:
            result.append(student)
    
    return result 
