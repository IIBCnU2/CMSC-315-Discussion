"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # I chose a real-world example: an inventory lookup system.
    # Each product name acts as a key, and its quantity acts as the value.
    # Python dictionaries behave like hash tables because each key is hashed
    # and mapped to a memory location, allowing fast access.

    inventory = {}  # empty hash table

    # Insert key-value pairs (product → quantity)
    inventory["water_bottle"] = 30
    inventory["headphones"] = 12
    inventory["keyboard"] = 8
    inventory["mouse"] = 15
    inventory["monitor"] = 5

    print("Inventory after inserts:", inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Lookup works by hashing the key and jumping directly to its stored value.
    print("Lookup 'keyboard':", inventory["keyboard"])
    print("Lookup 'mouse':", inventory["mouse"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", inventory)

    # Updating a key replaces the old value at the same hashed location.
    inventory["monitor"] = 10  # restocked monitors

    print("After update:", inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", inventory)

    # Removing a key deletes the entry entirely from the hash table.
    del inventory["headphones"]

    print("After deletion:", inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Lookup a missing key
    print("\nEdge Case 1: Lookup missing key 'tablet'")
    # Using .get() avoids a crash and returns None instead of an error
    print("Result:", inventory.get("tablet"))

    # Edge Case 2: Safe delete of missing key
    print("\nEdge Case 2: Safe delete of missing key 'charger'")
    if "charger" in inventory:
        del inventory["charger"]
    else:
        print("Key 'charger' does not exist, so it cannot be deleted.")

    # Edge Case 3: Updating a missing key (creates a new entry)
    print("\nEdge Case 3: Updating a missing key 'webcam'")
    inventory["webcam"] = 20
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
