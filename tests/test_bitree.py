import pytest

from bitree.bitree import BiTree


@pytest.mark.parametrize(
    "test, expected",
    [
        (BiTree(1), {"data": 1, "left": None, "right": None}),
    ],
)
def test___init__(test, expected):
    assert test.data == expected["data"]
    assert test.left == expected["left"]
    assert test.right == expected["right"]


@pytest.fixture
def tree1():
    tree = BiTree(1)
    return tree


@pytest.fixture
def tree2():
    tree = BiTree(1)
    tree.left = BiTree(2)
    return tree


@pytest.fixture
def tree3():
    tree = BiTree(1)
    tree.left = BiTree(2)
    tree.right = BiTree(3)
    return tree


@pytest.fixture
def tree4():
    tree = BiTree(1)
    tree.right = BiTree(3)
    return tree


@pytest.fixture
def tree5():
    tree = BiTree(1)
    tree.left = BiTree(2)
    tree.right = BiTree(3)
    tree.left.left = BiTree(4)
    tree.left.right = BiTree(5)
    return tree


@pytest.fixture
def tree6():
    tree = BiTree(1)
    tree.left = BiTree(2)
    tree.left.left = BiTree(4)
    tree.left.right = BiTree(5)
    return tree


@pytest.mark.parametrize(
    "left, right, expected",
    [
        ("tree1", "tree1", True),
        ("tree2", "tree2", True),
        ("tree3", "tree3", True),
        ("tree4", "tree4", True),
        ("tree1", "tree2", False),
        ("tree1", "tree3", False),
        ("tree1", "tree4", False),
        ("tree2", "tree3", False),
        ("tree2", "tree4", False),
        ("tree3", "tree4", False),
    ],
)
def test___eq__(left, right, expected, request):
    assert (
        request.getfixturevalue(left) == request.getfixturevalue(right)
    ) == expected


@pytest.mark.parametrize(
    "test, expected",
    [
        ("tree1", 1),
        ("tree2", 2),
        ("tree3", 2),
        ("tree4", 2),
        ("tree5", 3),
        ("tree6", 3),
    ],
)
def test_height(test, expected, request):
    assert request.getfixturevalue(test).height() == expected


@pytest.mark.parametrize(
    "tree_list, exp_tree",
    [
        ([1, 2, 3], [3, 1, None, 2]),
        ([1, 2, 3, None, None, 4, 5], [3, 1, 5, 2, 4]),
    ],
)
def test_rotate_left(tree_list, exp_tree):
    tree = BiTree.build(tree_list)
    assert BiTree.rotate_left(tree) == BiTree.build(exp_tree)


@pytest.mark.parametrize(
    "tree_list, exp_tree",
    [
        ([1, 2, 3], [2, None, 1, None, None, None, 3]),
        ([1, 2, 3, 4, 5], [2, 4, 1, None, None, 5, 3]),
    ],
)
def test_rotate_right(tree_list, exp_tree):
    tree = BiTree.build(tree_list)
    assert BiTree.rotate_right(tree) == BiTree.build(exp_tree)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([1], "tree1"),
        ([1, 2], "tree2"),
        ([1, 2, 3], "tree3"),
        ([1, None, 3], "tree4"),
        ([1, 2, 3, 4, 5], "tree5"),
        ([1, 2, None, 4, 5], "tree6"),
    ],
)
def test_build(test, expected, request):
    assert BiTree.build(test) == request.getfixturevalue(expected)


@pytest.mark.parametrize(
    "test",
    [
        ([1, None, 3, 4]),
        ([1, None, 3, None, 5]),
        ([1, 2, None, 4, 5, 6]),
        ([1, 2, None, 4, 5, None, 7]),
    ],
)
def test_build_error(test):
    with pytest.raises(TypeError):
        BiTree.build(test)
