import itertools
import re
from typing import Callable


def parse_input(input: str) -> list[int]:
    return list(map(int, re.findall(r"(\d+)", input)))


def solution(input: str, total_cost: Callable[[int, int, int], int]) -> int:
    positions = parse_input(input)

    return min(
        sum(itertools.starmap(total_cost, ((i, a, b) for b in positions)))
        for i, a in enumerate(positions)
    )


def part1(input: str) -> int:
    return solution(input, lambda _, a, b: abs(b - a))


def part2(input: str) -> int:
    return solution(input, lambda i, _, b: ((n := abs(b - i)) * (n + 1) // 2))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
