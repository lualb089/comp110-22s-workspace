from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatenation operator"""
        # Set up a result list of strings (str) that is empty
        result: list[str] = []

        if isinstance(rhs, str):
            # Loop thru each item in self.items
            for item in self.items:
                # For each item, append the concatenation of item and rhs to result list
                result.append(item + rhs)
            # could also be....
            # result.items.append(item + rhs)
        else:
            # Assert that len of self.items is equal to lenght of rhs.items
            for i in range(0, len(self.items)):
                # Build up the result list by concat
                # each item in self.items with corresponding item in rhs.items
                result.append(self.items[i] + rhs.items[i])
        # Return a newly constructed StrArray whose items are result 
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
names: StrArray = first + " " + last + "!"

print(result)
print(names)
print(last + "!")