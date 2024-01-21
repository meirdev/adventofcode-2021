from .main import part1, part2


INPUT = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def test_part1():
    assert part1(INPUT) == 150


def test_part2():
    assert part2(INPUT) == 900


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1507611
    assert part2(input) == 1880593125
