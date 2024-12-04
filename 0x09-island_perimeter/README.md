# island_perimeter Function

## Description
The `island_perimeter` function calculates the perimeter of an island represented in a grid. The grid is a 2D list of integers, where:
- `0` represents water.
- `1` represents land.

The function determines the total perimeter by analyzing the land cells and their adjacent cells.

## Usage
```python
def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculates the perimeter of the island described in the grid.

    Parameters:
        grid (List[List[int]]): A 2D list representing the grid.

    Returns:
        int: The perimeter of the island.
    """
