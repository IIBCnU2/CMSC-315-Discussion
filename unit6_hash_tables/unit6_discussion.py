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

    # A Python dictionary acts like a hash table because:
    # - Each key is run through a hash function.
    # - The hash determines where the value is stored in memory.
    # - This allows fast insertion and lookup.

    hash_table = {}  # empty dictionary (empty hash table)

    # Insert key-value pairs
    hash_table["name"] = "DJ"
    hash_table["age"] = 22
    hash_table["city"] = "Redzikowo"
    hash_table["favorite_game"] = "Tarkov"
    hash_table["student"] = True

    print("Hash table after inserts:", hash_table)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Lookup works by hashing the key and jumping directly
    # to the memory location where the value is stored.
    print("Lookup 'name':", hash_table["name"])
    print("Lookup 'city':", hash_table["city"])

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

    print("Before update:", hash_table)

    # Updating a key simply replaces the old value stored at that hashed location.
    hash_table["favorite_game"] = "Call of Duty"

    print("After update:", hash_table)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", hash_table)

    # Deleting a key removes the entry from the hash table entirely.
    del hash_table["student"]

    print("After deletion:", hash_table)

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
    print("\nEdge Case 1: Lookup missing key 'salary'")
    # Using .get() avoids a crash and returns None instead of an error
    print("Result:", hash_table.get("salary"))

    # Edge Case 2: Safely deleting a missing key
    print("\nEdge Case 2: Safe delete of missing key 'address'")
    if "address" in hash_table:
        del hash_table["address"]
    else:
        print("Key 'address' does not exist, so it cannot be deleted.")

    # Edge Case 3: Updating a missing key (creates a new entry)
    print("\nEdge Case 3: Updating a missing key 'hobby'")
    hash_table["hobby"] = "Car maintenance"
    print("Updated hash table:", hash_table)


if __name__ == "__main__":
    main()
