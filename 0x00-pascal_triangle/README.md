# Pascal's Triangle Implementation 🧑‍💻

## 📋 Overview
This Python script generates Pascal's Triangle up to the `n`th row. Pascal's Triangle is a triangular array where each number is the sum of the two directly above it. This structure is widely used in combinatorics, algebra, and probability.

## 🚀 Usage
### Function: `pascal_triangle(n)`
- **Arguments:**
  - `n` (int): The number of rows of Pascal's Triangle to generate. Must be a positive integer.
- **Returns:**
  - `list`: A list of lists representing Pascal's Triangle up to the `n`th row.

### Example
```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5)
