from .main import part1, part2


INPUT = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_part1():
    assert part1(INPUT) == 15


def test_part2():
    assert part2(INPUT) == 1134


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 500
    assert part2(input) == 970200
