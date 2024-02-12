from .main import part1, part2, run


def test_run():
    input = """
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
"""

    assert run(input, [9]) == {"w": 1, "x": 0, "y": 0, "z": 1}


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 95299897999897
    assert part2(input) == 31111121382151
