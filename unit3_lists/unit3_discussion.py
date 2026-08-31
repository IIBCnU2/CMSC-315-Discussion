"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

    - Python's list.insert() shifts all elements to the right starting
      from the index. For example, inserting at index 0 moves every
      existing element one position over.
    - Inserting at the beginning is the slowest because many elements
      must shift. Inserting at the end is fastest because nothing shifts.
    """
    lst.insert(index, value)  # built‑in list insertion handles shifting


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    - We must validate the index to avoid crashes.
    - Safe deletion prevents errors and makes the function predictable.
    - If the index is valid, Python shifts all elements left to fill the gap.
    """
    if 0 <= index < len(lst):
        return lst.pop(index)  # pop returns the removed value
    else:
        return None  # invalid index → safe failure


def search_value(lst, value):
    """
    Search for a value within the list.

    - This is a linear search because Python lists do not have fast
      lookup by value. The search checks each element one-by-one
      from left to right until it finds a match.
    - If the value is not found, we return -1.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")

    # Create a list with several values
    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert at the beginning
    # This shifts all elements to the right
    insert_at(numbers, 0, 5)
    print("After inserting 5 at beginning:", numbers)

    # Insert in the middle
    # Only elements after index 2 shift
    insert_at(numbers, 2, 25)
    print("After inserting 25 in middle:", numbers)

    # Insert at the end
    # No shifting required
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")

    # Delete from beginning
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("List now:", numbers)

    # Delete from middle
    removed = delete_at(numbers, 2)
    print("Removed from middle:", removed)
    print("List now:", numbers)

    # Delete from end
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("List now:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # Search for a value that exists
    index_found = search_value(numbers, 25)
    print("Searching for 25 → index:", index_found)

    # Search for a value that does not exist
    index_missing = search_value(numbers, 999)
    print("Searching for 999 → index:", index_missing)

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge Case 1: Delete using invalid index
    print("Attempting to delete at invalid index 100:")
    print("Result:", delete_at(numbers, 100))  # returns None

    # Edge Case 2: Insert into an empty list
    empty_list = []
    print("\nInserting into an empty list:")
    insert_at(empty_list, 0, "first")
    print("Empty list after insertion:", empty_list)

    # Edge Case 3: Delete from an empty list
    print("\nDeleting from an empty list:")
    print("Result:", delete_at([], 0))  # None because list is empty

    # Edge Case 4: Search for missing value
    print("\nSearching for missing value in list:")
    print("Result:", search_value(numbers, -1))


if __name__ == "__main__":
    main()
