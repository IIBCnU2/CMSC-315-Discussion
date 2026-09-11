# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

While completing this assignment, I strengthened my understanding of how linear and binary search algorithms operate and why their performance differs. Implementing both searches in Python reinforced the concept of time complexity, especially how linear search grows proportionally with dataset size, while binary search becomes dramatically more efficient by repeatedly halving the search space. I also gained experience testing algorithms across small datasets, large datasets, and edge cases, which made the performance differences much more visible. One challenge I encountered was ensuring that binary search behaved correctly across all boundary conditions, especially when the target was near the beginning or end of the list. I overcame this by adding print tests and carefully walking through each iteration to confirm the left, right, and mid pointers updated correctly. Linear search is best for unsorted or very small data, since sorting would cost more time than simply scanning. Binary search is ideal for large, sorted datasets where fast lookup is important. The main tradeoff is preparation: binary search requires sorted data, while linear search works on anything but is slower as collections grow.
