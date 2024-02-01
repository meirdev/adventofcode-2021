from .main import part1, part2


INPUT = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def test_part1():
    assert part1(INPUT) == 17


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 704
    # assert part2(input) == "HGAJBEHC"
