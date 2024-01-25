from .main import part1, part2


INPUT = "3,4,3,1,2"


def test_part1():
    assert part1(INPUT) == 5934


def test_part2():
    assert part2(INPUT) == 26984457539


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 376194
    assert part2(input) == 1693022481538
