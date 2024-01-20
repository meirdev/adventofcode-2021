from .main import part1, part2


INPUT = """
199
200
208
210
200
207
240
269
260
263
"""


def test_part1():
    assert part1(INPUT) == 7


def test_part2():
    assert part2(INPUT) == 5


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1521
    assert part2(input) == 1543
