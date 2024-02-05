from .main import part1, part2


INPUT = "target area: x=20..30, y=-10..-5"


def test_part1():
    assert part1(INPUT) == 45


def test_part2():
    assert part2(INPUT) == 112


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 4186
    assert part2(input) == 2709
