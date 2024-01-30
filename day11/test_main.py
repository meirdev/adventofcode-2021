from .main import part1, part2


INPUT = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def test_part1():
    assert part1(INPUT) == 1656


def test_part2():
    assert part2(INPUT) == 195


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1599
    assert part2(input) == 418
