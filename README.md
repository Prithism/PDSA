# PDSA - Problem-Solving and Data Structures & Algorithms

A collection of Python implementations for various data structure and algorithm problems.

## Code Summaries

### Sorting Algorithms

#### `insertion_sort.py`
Implements the **Insertion Sort** algorithm using a `Solution` class.
- **Function:** `insertionSort(nums: list[int]) -> list[int]`
- **Description:** Sorts an array by iterating through elements and placing each element in its correct position within the already-sorted portion. Builds the sorted array one item at a time.
- **Time Complexity:** O(n²) in worst case, O(n) in best case
- **Space Complexity:** O(1)

#### `merge_sort.py`
Implements the **Merge Sort** algorithm using a `Solution` class.
- **Function:** `sortArray(nums: list[int]) -> list[int]`
- **Description:** A divide-and-conquer sorting algorithm that recursively divides the array into halves, sorts them, and merges the sorted subarrays back together.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

#### `selection_sort.py`
Implements the **Selection Sort** algorithm using a `Solution` class.
- **Function:** `sortArray(nums: list[int]) -> list[int]`
- **Description:** Sorts an array by repeatedly finding the minimum element from the unsorted portion and placing it at the beginning.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

### Array & List Problems

#### `w1_grpa1.py`
**Minimum Difference in P Elements**
- **Function:** `find_Min_Difference(L, P)`
- **Description:** Finds the minimum difference between the maximum and minimum elements when choosing P elements from a list. Uses a sliding window approach on the sorted array.
- **Approach:** Sort the list, then use a window of size P to find the smallest range.
- **Example:** For list `[3, 4, 1, 9, 56, 7, 9, 12, 13]` with P=5, returns 6.

#### `w1_grpa3.py`
**Find the Odd One Out - Type Detector**
- **Function:** `odd_one(L)`
- **Description:** Identifies the data type that appears exactly once in a mixed-type list. Counts occurrences of int, float, str, and bool types.
- **Returns:** The data type (as a string) that appeared exactly once in the list.

### Geometry - Triangle Classification

#### `w1_ppa2.py`
**Triangle Properties and Classification**
- **Class:** `Triangle`
- **Methods:**
  - `__init__(a, b, c)`: Initialize triangle with three side lengths
  - `Is_valid()`: Validates if the sides form a valid triangle (triangle inequality theorem)
  - `Side_Classification()`: Classifies as Equilateral, Isosceles, or Scalene
  - `Angle_Classification()`: Classifies as Acute, Right, or Obtuse
  - `Area()`: Calculates the area using Heron's formula
- **Description:** Comprehensive triangle analyzer that validates triangles and provides classifications based on side lengths and angles.

### Number Theory

#### `w2_grpa2.py`
**Goldbach's Conjecture Solver**
- **Functions:**
  - `is_prime(num)`: Helper function to check if a number is prime
  - `Goldbach(n)`: Returns all pairs of prime numbers that sum to a given even number
- **Description:** Implements Goldbach's conjecture which states that every even number greater than 2 can be expressed as the sum of two primes. Returns all valid prime pairs (a, b) where a + b = n and a ≤ b.

---

## Project Structure

```
PDSA/
├── README.md                 # This file
├── insertion_sort.py         # Insertion sort implementation
├── merge_sort.py            # Merge sort implementation
├── selection_sort.py        # Selection sort implementation
├── w1_grpa1.py              # Minimum difference problem
├── w1_grpa3.py              # Type detection problem
├── w1_ppa2.py               # Triangle classification
└── w2_grpa2.py              # Goldbach's conjecture
```

## Usage

Each file can be run directly in Python:

```bash
python insertion_sort.py
python merge_sort.py
python selection_sort.py
python w1_grpa1.py
python w1_grpa3.py
python w1_ppa2.py
python w2_grpa2.py
```

---

## Key Concepts Covered

- **Sorting:** Insertion Sort, Merge Sort, Selection Sort
- **Array Manipulation:** Sliding windows, minimum/maximum problems
- **Type Handling:** Mixed-type list processing
- **Geometry:** Triangle validation and classification
- **Number Theory:** Prime checking, Goldbach's conjecture

---

## Status & Updates

⚠️ **Note:** GRPAs (Group Programming Assignments) and PPAs (Practice Programming Assignments) will be updated every week by the end of the week.

**Current assignments:**
- `w1_grpa1.py` - Updated
- `w1_grpa3.py` - Updated
- `w1_ppa2.py` - Updated
- `w2_grpa2.py` - Updated
