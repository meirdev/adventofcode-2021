from .main import part1, part2


INPUT_PART_1 = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

INPUT_PART_2 = """
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
"""


def test_part1():
    assert part1(INPUT_PART_1) == 12521


def test_part2():
    assert part2(INPUT_PART_2) == 44169


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 18300
    assert part2(input) == 50190
