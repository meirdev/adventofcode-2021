import itertools
from typing import Iterable, TypeAlias

Puzzle: TypeAlias = list[list[int]]


def parse_input(input: str) -> Puzzle:
    return [list(map(int, line)) for line in input.strip().splitlines()]


def solution(puzzle: Puzzle, iterable: Iterable[int]) -> Iterable[tuple[int, int]]:
    for i in iterable:
        flashes = []

        for y in range(len(puzzle)):
            for x in range(len(puzzle[y])):
                puzzle[y][x] += 1

                if puzzle[y][x] > 9:
                    flashes.append((y, x))

        flashed = set(flashes)

        while len(flashes):
            y, x = flashes.pop()

            for yi in range(max(0, y - 1), min(y + 2, len(puzzle))):
                for xi in range(max(0, x - 1), min(x + 2, len(puzzle[yi]))):
                    if (yi, xi) not in flashed:
                        puzzle[yi][xi] += 1

                        if puzzle[yi][xi] > 9:
                            flashes.append((yi, xi))
                            flashed.add((yi, xi))

        for y, x in flashed:
            puzzle[y][x] = 0

        yield i, len(flashed)


def part1(input: str) -> int:
    puzzle = parse_input(input)

    return sum(flashed for _, flashed in solution(puzzle, range(100)))


def part2(input: str) -> int:
    puzzle = parse_input(input)

    puzzle_len = len(puzzle) * len(puzzle[0])

    return next(
        i
        for i, flashed in solution(puzzle, itertools.count(1))
        if flashed == puzzle_len
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
