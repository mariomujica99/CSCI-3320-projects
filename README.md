# Data Structures & Algorithms - Programming Assignments

## Overview

This repository contains three programming assignments for algorithm analysis, data structure implementation, and complexity optimization.

## Assignment 1: Minimum Subsequence Sum Analysis

### Problem Description
Modify maximum subsequence sum algorithms to find the minimum subsequence sum, including starting and ending indices. Analyze and compare the execution times of three different algorithms across various input sizes.

### Algorithms Implemented

Algorithm 2 - O(n²) Brute Force:
- Nested loop checking all possible subsequences

Algorithm 3 - O(n log n) Divide and Conquer:
- Recursive divide-and-conquer approach

Algorithm 4 - O(n) Dynamic Programming:
- Single-pass linear algorithm

### Performance Analysis

- 10 test runs per input size
- Input sizes: 100, 200, 400, 800, 1600, 3200, 64000
- Excel graphs showing execution time vs. input size

### Sample Output
```
Please enter the size of the problem (N): 15
673 -869 -153 214 -139 40 65 -925 -639 -696 956 823 -714 500 967

Algorithm 2: 
MinSum: -3102, S_index: 1, E_index: 9
Execution Time: 82048 nanoseconds

Algorithm 3: 
MinSum: -3102, S_index: 1, E_index: 9
Execution Time: 23165 nanoseconds

Algorithm 4: 
MinSum: -3102, S_index: 1, E_index: 9
Execution Time: 11345 nanoseconds
```

## Assignment 2: Stack & Queue Implementation with Linked Lists

### Problem Description
Implement Queue and TwoStacks data structures using singly and doubly linked lists.

### Data Structures Implemented

Singly Linked List
- In-place recursive list reversal

Queue (using Singly Linked List)

Doubly Linked List
- Bidirectional traversal capability

TwoStacks (using Doubly Linked List)

### Features

- Menu-driven command-line interface
- 17 different operations
- Input validation and error handling
- Edge case coverage (empty stacks/queues)

### Menu Options
```
1)  Construct list L1
2)  Reverse the list
3)  Print list L1
4)  Construct queue Q1
5)  Print front of Q1
6)  Dequeue from Q1
7)  Enqueue to Q1
8)  Print queue Q1
9)  Construct twoStack T1
10) Print top of S1
11) Pop from S1
12) Push to S1
13) Print top of S2
14) Pop from S2
15) Push to S2
16) Print twoStack T1
17) Exit
```

## Assignment 3: Zero-Sum Subarray Detection

### Problem Description
Determine if a continuous sequence of elements in an array sums to zero. The solution must be more efficient than O(n²) brute force approach.

### Algorithm Implementation

Hash-Based Solution - O(n):
- Uses prefix sum and hash map
- Detects zero-sum subarrays in single pass
- Returns starting and ending indices

### Algorithm Strategy

- Prefix Sum Calculation: Track cumulative sum trough iteratation
- Hash Map Storage: Store each prefix sum with its index
- Zero Detection:
   - If `current_sum == 0`: subarray from index 0 to current index
   - If `current_sum` seen before: subarray between stored index and current index

### Features

- Random integer generation with configurable ranges (N)
- Print all numbers when N < 50
- Formatted output with negative number display

### Sample Output

**Example 1: Zero-sum found**
```
Please enter the size of the problem (N): 5
4 2 -3 1 6

Yes, there is a sequence where the sum of the elements equals zero.
Starting index: 1
Ending index: 3
Sum: 2 + (-3) + 1 = 0
```

**Example 2: No zero-sum**
```
Please enter the size of the problem (N): 5
1 -5 3 4 5

No, there is no sequence where the sum of the elements equals zero.
```

### Complexity Analysis

- Time Complexity: O(n) - Single pass through array
- Hash Operations: O(1) - Average case for insertion/lookup

## Learning Outcomes

Algorithm Analysis
- Time complexity analysis (Big-O notation)

Data Structures
- Linked list implementations (singly and doubly)
- Stack and Queue abstractions
- Pointer manipulation techniques

Optimization Techniques
- Hash-based optimization
- Divide-and-conquer strategies
- Dynamic programming principles
- Prefix sum technique

Software Engineering
- Menu-driven interface
- Input validation and error handling

## Academic Integrity Notice

These assignments were completed as coursework for CSCI 3320: Data Structures & Algorithms. The code is provided for portfolio purposes. Please do not copy or reproduce for academic submissions.
