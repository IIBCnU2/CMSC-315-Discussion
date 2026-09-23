"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Create a copy so the original list is not modified
    sorted_list = lst.copy()

    n = len(sorted_list)

    # Repeatedly compare adjacent elements
    for i in range(n):
        for j in range(0, n - i - 1):

            # Swap values if they are out of order
            if sorted_list[j] > sorted_list[j + 1\]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Base case: a list with 0 or 1 element is already sorted
    if len(lst) <= 1:
        return lst

    # Find the midpoint and split the list
    midpoint = len(lst) // 2
    left_half = lst[:midpoint]
    right_half = lst[midpoint:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    result = []
    left_index = 0
    right_index = 0

    # Compare elements from both lists and add
    # the smaller element to the result list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index\]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left list
    result.extend(left[left_index:])

    # Append any remaining elements from the right list
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    dataset1 = [25, 8, 42, 17, 3, 31, 12]

    print("Original List:", dataset1)
    print("Bubble Sort Result:", bubble_sort(dataset1))
    print("Merge Sort Result:", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    dataset2 = [99, 45, 61, 2, 77, 14, 30, 50]

    print("Original List:", dataset2)
    print("Bubble Sort Result:", bubble_sort(dataset2))
    print("Merge Sort Result:", merge_sort(dataset2))

    print("\nComparison:")
    print("Both algorithms produce the same sorted output.")
    print("Merge Sort is generally more efficient on larger datasets.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []
    print("\nEmpty List:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("Explanation: Both algorithms return an empty list.")

    # Edge Case 2: Already sorted list
    sorted_list = [1, 2, 3, 4, 5]
    print("\nAlready Sorted List:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))
    print("Explanation: The list remains unchanged because it is already sorted.")

    # Edge Case 3: Duplicate values
    duplicates = [5, 2, 5, 1, 2, 3]
    print("\nList with Duplicates:", duplicates)
    print("Bubble Sort:", bubble_sort(duplicates))
    print("Merge Sort:", merge_sort(duplicates))
    print("Explanation: Duplicate values are kept and sorted correctly.")


if __name__ == "__main__":
    main()
    main()
