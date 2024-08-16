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
from pascal_triangle import pascal_triangle

# Generate the first 5 rows of Pascal's Triangle
print(pascal_triangle(5))
