"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # If the tree is empty, the first value becomes the root
        if self.root is None:
            self.root = Node(value)
        else:
            # Use recursion to find the correct spot
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Smaller values always go left
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)

        # Larger values always go right
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

        # If equal, ignore (simple duplicate handling)
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is faster because each step cuts the search space down
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # Visit left first (smaller values)
        self._inorder_recursive(node.left, values)

        # Visit the node itself
        values.append(node.value)

        # Visit right (larger values)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    bst = BST()

    # Insert values (both left and right branches)
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    print("Inserting values:", values_to_insert)

    for v in values_to_insert:
        bst.insert(v)

    # BST reduces search space each step
    print("BST built. Each comparison cuts the search space down.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    inorder_list = bst.inorder()
    print("In-order traversal:", inorder_list)
    print("This is sorted because smaller values are stored on the left and larger on the right.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    print("Search 40:", bst.search(40))  # exists
    print("Search 70:", bst.search(70))  # exists
    print("Search 10:", bst.search(10))  # not found
    print("Search 99:", bst.search(99))  # not found

    print("BST search follows the tree path instead of checking every value.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    empty_tree = BST()
    print("Searching empty tree for 5:", empty_tree.search(5))
    print("Empty tree returns False because there are no nodes to check.")


if __name__ == "__main__":
    main()
