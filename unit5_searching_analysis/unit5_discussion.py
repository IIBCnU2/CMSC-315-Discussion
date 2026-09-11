"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # NEW COMMENT:
    # Linear search checks each element one-by-one.
    # In the worst case, it must inspect *every* item,
    # so the time grows proportionally with the list size → O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1  # Target not found


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # NEW COMMENT:
    # Binary search works only on sorted lists.
    # Each iteration compares the middle element to the target.
    # Based on that comparison, it discards HALF of the list.
    # This halving process gives binary search O(log n) time complexity.
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # NEW COMMENT: Target must be in the right half,
            # so we eliminate the entire left half.
            left = mid + 1
        else:
            # NEW COMMENT: Target must be in the left half,
            # so we eliminate the entire right half.
            right = mid - 1

    return -1  # Target not found


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    small_dataset = [1, 3, 5, 7, 9, 11]
    print("Small dataset:", small_dataset)

    # Searching for a value that exists
    print("Linear search (exists):", linear_search(small_dataset, 7))
    print("Binary search (exists):", binary_search(small_dataset, 7))

    # Searching for a value that does NOT exist
    print("Linear search (not found):", linear_search(small_dataset, 100))
    print("Binary search (not found):", binary_search(small_dataset, 100))

    # NEW COMMENT:
    # In small datasets, both algorithms appear fast.
    # The difference becomes noticeable only as the dataset grows.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    large_dataset = list(range(0, 500000))  # Half a million sorted numbers

    # Searching for a value near the end
    print("Linear search (large dataset):", linear_search(large_dataset, 499999))
    print("Binary search (large dataset):", binary_search(large_dataset, 499999))

    # NEW COMMENT:
    # Linear search must scan nearly 500,000 items.
    # Binary search finds the value in about ~19 comparisons (log2(500000)).
    # This demonstrates why binary search becomes dramatically more efficient
    # as datasets grow larger.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Empty list
    empty_list = []
    print("Empty list (linear):", linear_search(empty_list, 5))
    print("Empty list (binary):", binary_search(empty_list, 5))
    # NEW COMMENT: Both searches immediately return -1 because no elements exist.

    # Single-element list
    single = [42]
    print("Single-element list (linear):", linear_search(single, 42))
    print("Single-element list (binary):", binary_search(single, 42))
    # NEW COMMENT: Both algorithms succeed instantly because the only element matches.

    # Value at first position
    print("Value at first position:", linear_search(small_dataset, 1))

    # Value at last position
    print("Value at last position:", linear_search(small_dataset, 11))

    # NEW COMMENT:
    # These edge cases show how search behavior changes depending on list size
    # and element position.


if __name__ == "__main__":
    main()
