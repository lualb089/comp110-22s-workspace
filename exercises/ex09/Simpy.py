"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730480432"


class Simpy:
    """A utility class that is helpful for working with sequences of numerical data, just like what you would expect to see in a column of a data table."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Its purpose is to initialize the `values` attribute of the newly constructed `Simpy` object to the argument passed in."""
        self.values = values

    def __str__(self) -> str:
        """Takes no arguments and returns a `str`."""
        return f"Simpy({self.values})"

    def fill(self, values: float, fill_in: int) -> None:
        """Its purpose is to _fill_ a `Simpy`'s `values` with a specific number of repeating values."""
        self.values = []
        for i in range(fill_in):
            self.values.append(values)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Its purpose is to fill in the `values` attribute with range of values, like the `range` built-in function, but in terms of `float`s."""
        self.values = []
        assert step != 0.0

        while abs(stop) > abs(start):
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Compute the sum of a list."""
        numbers: float = 0.0
        numbers = sum(self.values)

        return numbers
        
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add the ability to use the _addition operator_ (`+`) in conjunction with `Simpy` objects and floats."""
        end: list[float] = []

        if isinstance(rhs, float):
            for value in self.values:
                end.append(value + rhs)
        
        else:
            assert len(rhs.values) == len(self.values)

        if isinstance(rhs, Simpy):
            for value in range(0, len(self.values)):
                end.append(self.values[value] + rhs.values[value])

        return Simpy(end)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add the ability to use the _power operator_ (`**`) in conjunction with `Simpy` objects and floats."""
        end: list[float] = []

        if isinstance(rhs, float):
            for value in self.values:
                end.append(value ** rhs)
        
        else:
            assert len(rhs.values) == len(self.values)

        if isinstance(rhs, Simpy):
            for value in range(0, len(self.values)):
                end.append(self.values[value] ** rhs.values[value])

        return Simpy(end)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add the ability to produce a _mask_, or a `list[bool]`, based on the equality of each item in the `values` attribute with some other `Simpy` object or a `float` value."""
        end: list[bool] = []

        if isinstance(rhs, float):
            for value in self.values:
                end.append(value == rhs)
        
        else:
            assert len(rhs.values) == len(self.values)

        if isinstance(rhs, Simpy):
            for value in range(0, len(self.values)):
                end.append(self.values[value] == rhs.values[value])

        return end

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add the ability to produce a _mask_, or a `list[bool]`, based on the greater than relationship between each item in the `values` attribute with some other `Simpy` object or a `float` value."""
        end: list[bool] = []

        if isinstance(rhs, float):
            for value in self.values:
                end.append(value > rhs)
        
        # else:
            # assert len(rhs.values) == len(self.values)

        if isinstance(rhs, Simpy):
            for value in range(0, len(self.values)):
                end.append(self.values[value] > rhs.values[value])

        return end

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Add the ability to use the _subscription_ operator with `Simpy` objects. To add _subscription notation_ support to objects of classes you design, you must implement the special method named `__getitem__`."""
        if isinstance(rhs, int):
            return self.values[rhs]
        
        else:
            end: Simpy = Simpy([])
            assert len(self.values) == len(rhs)

            for value in range(0, len(rhs)):
                if rhs[value] is True:
                    end.values.append(self.values[value])

# if isinstance(rhs, Simpy):
# for value in range(0, len(self.values)):
# end.append(self.values[value] == rhs.values[value])

        return end