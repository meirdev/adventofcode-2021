import math
from typing import TypeAlias


HeightMap: TypeAlias = list[list[int]]


def parse_input(input: str) -> HeightMap:
    return [[int(cell) for cell in line] for line in input.strip().splitlines()]


def part1(input: str) -> int:
    heightmap = parse_input(input)

    def check_cell(y: int, x: int, value: int) -> bool:
        if y < 0 or x < 0:
            return True

        try:
            return heightmap[y][x] > value
        except:
            return True

    return sum(
        heightmap[y][x] + 1
        for y in range(len(heightmap))
        for x in range(len(heightmap[y]))
        if all(
            check_cell(y_, x_, heightmap[y][x])
            for x_, y_ in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y))
        )
    )


def part2(input: str) -> int:
    heightmap = parse_input(input)

    def check_cell(y: int, x: int, value: int, heights: set[tuple[int, int]]) -> bool:
        if y < 0 or x < 0:
            return False

        try:
            return (
                heightmap[y][x] != 9
                and heightmap[y][x] > value
                and (y, x) not in heights
            )
        except:
            return False

    def inner(y: int, x: int, heights: set[tuple[int, int]]):
        for x_, y_ in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
            if check_cell(y_, x_, heightmap[y][x], heights):
                heights |= inner(y_, x_, heights | {(y_, x_)})

        return heights

    return math.prod(
        sorted(
            (
                len(inner(y, x, {(y, x)}))
                for y in range(len(heightmap))
                for x in range(len(heightmap[y]))
            ),
            reverse=True,
        )[:3]
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
