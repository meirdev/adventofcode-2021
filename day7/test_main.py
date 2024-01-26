from .main import part1, part2


INPUT = "16,1,2,0,4,2,7,1,2,14"


def test_part1():
    assert part1(INPUT) == 37


def test_part2():
    assert part2(INPUT) == 168


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 353800
    assert part2(input) == 98119739
