import collections
import functools
from typing import Iterator


POINTS_PART_1: dict[str, int] = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

POINTS_PART_2: dict[str, int] = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

OPEN_CLOSE: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

CLOSE_OPEN: dict[str, str] = {v: k for k, v in OPEN_CLOSE.items()}


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


def parse_line(line: str) -> list[str]:
    stack = []

    for chr in line:
        if chr in OPEN_CLOSE:
            stack.append(chr)
        elif len(stack) == 0 or CLOSE_OPEN.get(chr) != stack[-1]:
            raise ValueError(chr)
        else:
            stack.pop()

    return stack


def parse_lines(input: str) -> Iterator[tuple[bool, list[str]]]:
    lines = parse_input(input)

    for line in lines:
        try:
            yield True, parse_line(line)
        except ValueError as error:
            yield False, list(error.args)


def part1(input: str) -> int:
    count = collections.Counter(
        result[-1] for ok, result in parse_lines(input) if not ok
    )

    return sum(count[i] * POINTS_PART_1[i] for i in count)


def part2(input: str) -> int:
    scores = sorted(
        functools.reduce(
            lambda total, chr: total * 5 + POINTS_PART_2[OPEN_CLOSE[chr]],
            reversed(result),
            0,
        )
        for ok, result in parse_lines(input)
        if ok
    )

    return scores[len(scores) // 2]


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
