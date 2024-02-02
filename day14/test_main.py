from .main import part1, part2


INPUT = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def test_part1():
    assert part1(INPUT) == 1588


def test_part2():
    assert part2(INPUT) == 2188189693529


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 2003
    assert part2(input) == 2276644000111
