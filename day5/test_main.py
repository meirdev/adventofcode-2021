from .main import part1, part2


INPUT = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_part1():
    assert part1(INPUT) == 5


def test_part2():
    assert part2(INPUT) == 12


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 7674
    assert part2(input) == 20898
