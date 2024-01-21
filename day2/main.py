import enum
import re
from typing import NamedTuple


class Direction(enum.IntEnum):
    UP = 0
    DOWN = 1
    FORWARD = 2


class Command(NamedTuple):
    direction: Direction
    units: int


def parse_input(input: str) -> list[Command]:
    commands: list[Command] = []

    for dir, units in re.findall(r"(\w+) (\d+)", input):
        match dir:
            case "up":
                direction = Direction.UP
            case "down":
                direction = Direction.DOWN
            case "forward":
                direction = Direction.FORWARD
            case _:
                raise ValueError("unknown direction")

        commands.append(Command(direction, int(units)))

    return commands


def part1(input: str) -> int:
    commands = parse_input(input)

    horizontal = 0
    depth = 0

    for dir, units in commands:
        if dir == Direction.UP:
            depth -= units
        elif dir == Direction.DOWN:
            depth += units
        elif dir == Direction.FORWARD:
            horizontal += units

    return horizontal * depth


def part2(input: str) -> int:
    commands = parse_input(input)

    horizontal = 0
    depth = 0
    aim = 0

    for dir, units in commands:
        if dir == Direction.UP:
            aim -= units
        elif dir == Direction.DOWN:
            aim += units
        elif dir == Direction.FORWARD:
            horizontal += units
            depth += aim * units

    return horizontal * depth


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
