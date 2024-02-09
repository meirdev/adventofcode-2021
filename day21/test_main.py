from .main import part1, part2


INPUT = """
Player 1 starting position: 4
Player 2 starting position: 8
"""


def test_part1():
    assert part1(INPUT) == 739785


def test_part2():
    assert part2(INPUT) == 444356092776315


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 503478
    assert part2(input) == 716241959649754
