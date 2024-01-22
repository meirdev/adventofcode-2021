import collections
from typing import Callable, Counter, Iterable, NamedTuple


class Num(NamedTuple):
    counter: Counter[str]
    max: str
    min: str


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


def parse_num(num: Iterable) -> Num:
    counter = collections.Counter(num)

    max_ = max(counter, key=lambda i: counter[i])
    min_ = min(counter, key=lambda i: counter[i])

    return Num(counter, max_, min_)


def part1(input: str) -> int:
    report = parse_input(input)

    gamma_rate = ""
    epsilon_rate = ""

    for i in zip(*report):
        num = parse_num(i)

        gamma_rate += num.max
        epsilon_rate += num.min

    return int(gamma_rate, base=2) * int(epsilon_rate, base=2)


def part2(input: str) -> int:
    report = parse_input(input)

    def inner(report: list[str], search_for: Callable[[Num], str]) -> str:
        k = 0

        while len(report) != 1:
            num_col = [i[k] for i in report]
            value = search_for(parse_num(num_col))
            report = [report[i] for i, n in enumerate(num_col) if n == value]
            k += 1

        return report[0]

    oxygen_generator_rating = inner(
        report[:], lambda num: "1" if num.max == num.min else num.max
    )
    co2_scrubber_rating = inner(
        report[:], lambda num: "0" if num.max == num.min else num.min
    )

    return int(oxygen_generator_rating, base=2) * int(co2_scrubber_rating, base=2)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
