import enum
import re
from typing import NamedTuple


class Dot(NamedTuple):
    x: int
    y: int


class Axis(enum.StrEnum):
    X = "x"
    Y = "y"


class Instruction(NamedTuple):
    axis: Axis
    value: int


class Paper:
    def __init__(self, dots: list[Dot]) -> None:
        self.height = max(dots, key=lambda i: i.y).y
        self.width = max(dots, key=lambda i: i.x).x

        self.dots = [[0] * (self.width + 1) for _ in range(self.height + 2)]

        for x, y in dots:
            self.dots[y][x] = 1

    def fold(self, instruction: Instruction) -> None:
        axis, value = instruction

        if axis == Axis.Y:
            for to_y, from_y in enumerate(range(self.height, value, -1)):
                for x in range(self.width + 1):
                    self.dots[to_y][x] |= self.dots[from_y][x]

            self.height = self.height // 2 - 1
        else:
            for to_x, from_x in enumerate(range(self.width, value, -1)):
                for y in range(self.height + 1):
                    self.dots[y][to_x] |= self.dots[y][from_x]

            self.width = self.width // 2 - 1

    def visible_dots(self) -> int:
        return sum(
            self.dots[y][x]
            for y in range(self.height + 1)
            for x in range(self.width + 1)
        )

    def draw(self) -> str:
        return "\n".join(
            "".join(f"{'#' if self.dots[y][x] else '.'}" for x in range(self.width + 1))
            for y in range(self.height + 1)
        )


def parse_input(input: str) -> tuple[list[Dot], list[Instruction]]:
    dots = [Dot(int(x), int(y)) for x, y in re.findall(r"(\d+),(\d+)", input)]

    instructions = [
        Instruction(Axis(axis), int(value))
        for axis, value in re.findall(r"fold along (x|y)=(\d+)", input)
    ]

    return dots, instructions


def part1(input: str) -> int:
    dots, instructions = parse_input(input)

    paper = Paper(dots)
    paper.fold(instructions[0])

    return paper.visible_dots()


def part2(input: str) -> str:
    dots, instructions = parse_input(input)

    paper = Paper(dots)

    for instruction in instructions:
        paper.fold(instruction)

    return "\n" + paper.draw()


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
