# type: ignore

import ast
import functools
import itertools
from typing import TypeAlias

SnailfishNumber: TypeAlias = list["SnailfishNumber"] | int


def parse_input(input: str) -> list[SnailfishNumber]:
    return [ast.literal_eval(line) for line in input.strip().splitlines()]


def add_left(sn: SnailfishNumber, n: int) -> SnailfishNumber:
    if isinstance(sn, int):
        return sn + n

    return [add_left(sn[0], n), sn[1]]


def add_right(sn: SnailfishNumber, n: int) -> SnailfishNumber:
    if isinstance(sn, int):
        return sn + n

    return [sn[0], add_right(sn[1], n)]


def explode(sn: SnailfishNumber, n: int = 4) -> tuple[bool, SnailfishNumber]:
    if isinstance(sn, int):
        return False, [0, sn, 0]

    if n == 0:
        return True, [sn[0], 0, sn[1]]

    a, b = sn

    exploded, (left, a, right) = explode(a, n - 1)
    if exploded:
        return True, [left, [a, add_left(b, right)], 0]

    exploded, (left, b, right) = explode(b, n - 1)
    if exploded:
        return True, [0, [add_right(a, left), b], right]

    return False, [0, sn, 0]


def split(sn: SnailfishNumber) -> tuple[bool, SnailfishNumber]:
    if isinstance(sn, int):
        if sn >= 10:
            return True, [sn // 2, (sn + 1) // 2]
        return False, sn

    a, b = sn

    splitted, a = split(a)
    if splitted:
        return splitted, [a, b]

    splitted, b = split(b)
    return splitted, [a, b]


def add(a: SnailfishNumber, b: SnailfishNumber) -> SnailfishNumber:
    sn = [a, b]

    while True:
        exploded, (_, sn, _) = explode(sn)
        if exploded:
            continue

        splitted, sn = split(sn)
        if not splitted:
            break

    return sn


def magnitude(sn: SnailfishNumber) -> int:
    if isinstance(sn, int):
        return sn

    return 3 * magnitude(sn[0]) + 2 * magnitude(sn[1])


def part1(input: str) -> int:
    snailfish_numbers = parse_input(input)

    return magnitude(functools.reduce(add, snailfish_numbers))


def part2(input: str) -> int:
    snailfish_numbers = parse_input(input)

    return max(
        magnitude(add(a, b)) for a, b in itertools.permutations(snailfish_numbers, 2)
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
