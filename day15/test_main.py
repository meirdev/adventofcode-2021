from .main import part1, part2


INPUT = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


def test_part1():
    assert part1(INPUT) == 40


def test_part2():
    assert part2(INPUT) == 315


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 537
    assert part2(input) == 2881
