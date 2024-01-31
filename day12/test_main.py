from .main import part1, part2


INPUT_1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

INPUT_2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

INPUT_3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

def test_part1():
    for input, expected in ((INPUT_1, 10), (INPUT_2, 19), (INPUT_3, 226)):
        assert part1(input) == expected


def test_part2():
    for input, expected in ((INPUT_1, 36), (INPUT_2, 103), (INPUT_3, 3509)):
        assert part2(input) == expected


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 5457
    assert part2(input) == 128506
