from .main import part1


INPUT = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""


def test_part1():
    assert part1(INPUT) == 58


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 432
