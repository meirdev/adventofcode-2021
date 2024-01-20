import itertools

import more_itertools


def parse_input(input: str) -> list[int]:
    return list(map(int, input.strip().splitlines()))


def solution(input: str, window_size: int = 1) -> int:
    measurements = parse_input(input)

    return sum(
        a < b
        for a, b in itertools.pairwise(
            map(sum, more_itertools.windowed(measurements, window_size))  # type: ignore
        )
    )


def part1(input: str) -> int:
    return solution(input)


def part2(input: str) -> int:
    return solution(input, 3)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
