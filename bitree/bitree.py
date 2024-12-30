from __future__ import annotations


class BiTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left: BiTree = None
        self.right: BiTree = None

    def __eq__(self, other: object) -> bool:
        if self.data == other.data:
            left_equal = False
            right_equal = False

            if self.left is not None and other.left is not None:
                left_equal = self.left == other.left
            elif self.left is None and other.left is None:
                left_equal = True

            if self.right is not None and other.right is not None:
                right_equal = self.right == other.right
            elif self.right is None and other.right is None:
                right_equal = True

            return left_equal and right_equal
        return False

    def height(self) -> int:
        left = 0
        right = 0
        if self.left is not None:
            left += self.left.height()
        if self.right is not None:
            right += self.right.height()
        return 1 + max(left, right)

    def get_list(self) -> list:
        tree_list = []
        if self is None:
            return

        queue = []
        queue.append(self)

        while len(queue) > 0:
            if queue[0] is not None:
                tree_list.append(queue[0].data)
            else:
                tree_list.append(None)
                queue.pop(0)
                continue
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            elif node.right is not None:
                queue.append(None)

            if node.right is not None:
                queue.append(node.right)
            elif node.left is not None:
                queue.append(None)

        return tree_list

    @staticmethod
    def rotate_left(root) -> BiTree:
        new = root.right
        root.right = new.left
        new.left = root
        return new

    @staticmethod
    def rotate_right(root) -> BiTree:
        new = root.left
        root.left = new.right
        new.right = root
        return new

    @staticmethod
    def build(node_list) -> BiTree:
        for i in range(1, len(node_list) + 1):
            if node_list[i - 1] is not None and node_list[int(i / 2 - 1)] is None:
                raise TypeError(
                    "cannot create tree with parent type 'NoneType'. Index "
                    + str(i - 1)
                    + "."
                )
        return BiTree._generate_tree(node_list)

    @staticmethod
    def _generate_tree(node_list, i=1) -> BiTree:
        tree = BiTree(node_list[i - 1])
        i = 2 * i
        if i - 1 < len(node_list):
            if node_list[i - 1] is not None:
                tree.left = BiTree._generate_tree(node_list, i)
        i += 1
        if i - 1 < len(node_list):
            if node_list[i - 1] is not None:
                tree.right = BiTree._generate_tree(node_list, i)
        return tree
