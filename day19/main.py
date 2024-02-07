import itertools
import re
from typing import NamedTuple


class Beacon(NamedTuple):
    x: int
    y: int
    z: int


def parse_input(input: str) -> list[tuple[int, list[Beacon]]]:
    data = []

    substrings = re.split(r"--- scanner (\d+) ---", input)

    for scanner, substring in itertools.batched(substrings[1:], 2):
        beacons = re.findall(r"(-?\d+),(-?\d+),(-?\d+)", substring)

        data.append((int(scanner), [Beacon(*map(int, i)) for i in beacons]))

    return data


def part1(input: str) -> int:
    data = parse_input(input)


def part2(input: str):
    pass


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
