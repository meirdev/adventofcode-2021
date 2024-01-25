import collections
import re


def parse_input(input: str) -> list[int]:
    return list(map(int, re.findall(r"(\d+)", input)))


def solution(input: str, days: int) -> int:
    lanternfishs = parse_input(input)

    day_lanternfishs = collections.deque(lanternfishs.count(i) for i in range(9))

    for _ in range(days):
        day_lanternfishs[7] += day_lanternfishs[0]
        day_lanternfishs.rotate(-1)

    return sum(day_lanternfishs)


def part1(input: str) -> int:
    return solution(input, 80)


def part2(input: str) -> int:
    return solution(input, 256)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
