# Data Structures and Algorithms

This repository contains solutions to various data structure and algorithm problems implemented in Python. The problems are categorized into three main sections: Arrays and Strings, Linked Lists, and Binary Trees, along with a section for Graphs.

## Table of Contents

- [Array and String](#array-and-string)
- [Linked List](#linked-list)
- [Binary Tree](#binary-tree)
- [Graphs](#graphs)

## Array and String

### Uncompress
The `uncompress` method takes a compressed string as input and returns the uncompressed string. If a character is a digit, it increments `j` to continue scanning the number. If a non-digit character is encountered, it extracts the number from the substring.  
Example: `3a2b4c` → `aaabbcccc`

### Compress
The `compress` method takes an uncompressed string and converts it into a compressed string. If a character appears only once, it is represented by just the character itself.

### Anagrams
The `anagrams` function takes in two strings as arguments and returns a boolean indicating whether or not they are anagrams.

### Most Frequent Character
The `MostFrequentChar` function takes in a string and returns the most frequent character. If there are ties, it returns the character that appears first.

### Pair Sum
The `PairSum` function takes a list and a target sum and returns a tuple containing a pair of indices whose elements sum to the target.

### Pair Product
The `PairProduct` function takes a list and a target product and returns a tuple containing a pair of indices whose elements multiply to the target.

### Intersection
The `Intersection` function takes in two arrays and returns an array of their common elements.

### Five Sort
The `FiveSort` function rearranges an array such that all 5s appear at the end, mutating the original list in place.

## Linked List

### LinkedListValues
The `LinkedListValues` function takes in the head of a linked list and returns an array containing all values of the nodes.

### Sum List
The `SumList` function takes in the head of a linked list and returns the sum of its values.

### LinkedListFind
The `LinkedListFind` function checks if a target value exists in the linked list.

### Get Node Value
The `GetNodeValue` function takes in the head of a linked list and an index, returning the value at that index or -1 if out of bounds.

### Reverse Linked List
The `ReverseLinkedList` function takes in the head of a linked list and returns the head of the reversed list.

### Zipper List
The `ZipperList` function merges two lists together in a zipper fashion.

### Merge Lists
The `MergeLists` function merges two sorted linked lists into a single sorted linked list.

### Longest Streak
The `LongestStreak` function returns the length of the longest consecutive streak of the same value in a linked list.

### Remove Node
The `RemoveNode` function deletes a node containing a target value from the linked list.

### Insert Node
The `InsertNode` function inserts a new node with a specified value at a given index.

### Create Linked List
The `CreateLinkedList` function creates a linked list from a list of values.

### Add Lists
The `AddLists` function sums two linked lists representing numbers and returns the result as a new linked list.

## Binary Tree

### All Tree Paths
The `all_tree_paths` function returns a 2-Dimensional list representing all root-to-leaf paths in a binary tree.

### Level Averages
The `level_averages` function returns a list containing the average value of each level in a binary tree.

### Bottom Right Value
The `bottom_right_value` function returns the right-most value in the bottom-most level of the tree.

### Breadth First Values
The `breadth_first_values` function returns a list of all values in the tree in breadth-first order.

### Depth First Values
The `depth_first_values` function returns a list of all values in the tree in depth-first order.

### How High
The `how_high` function returns the height of the binary tree.

### Leaf List
The `leaf_list` function returns a list containing the values of all leaf nodes.

### Max Path Sum
The `max_path_sum` function returns the maximum sum of any root-to-leaf path in the tree.

### Path Finder
The `path_finder` function returns a path to a target value in the tree.

### Tree Includes
The `tree_includes` function checks if a target value exists in the tree.

### Tree Levels
The `tree_levels` function returns a 2-Dimensional list representing each level of the tree.

### Tree Min Value
The `tree_min_value` function returns the minimum value within the tree.

### Tree Sum
The `tree_sum` function returns the total sum of all values in the tree.

### Tree Value Count
The `tree_value_count` function returns the number of times a target value occurs in the tree.

## Graphs

### Has Path
The `has_path` function determines if there exists a directed path between two nodes in a directed acyclic graph.

---

## Setup and Usage

Each problem solution is implemented as a standalone function. To run these solutions:

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2. Run any problem solution using your preferred Python environment.


