import collections
import functools
from typing import Counter, Iterable, NamedTuple


class Num(NamedTuple):
    counter: Counter[str]
    max: str
    min: str


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


@functools.cache
def parse_num(num: Iterable) -> Num:
    counter = collections.Counter(num)

    max_ = max(counter, key=counter.get)
    min_ = min(counter, key=counter.get)

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

    oxygen_generator_rating = report[:]
    co2_scrubber_rating = report[:]

    k = 0

    while len(oxygen_generator_rating) != 1:
        num_col = tuple(i[k] for i in oxygen_generator_rating)
        num = parse_num(num_col)
        if num.max == num.min:
            search = "1"
        else:
            search = num.max
        oxygen_generator_rating = [oxygen_generator_rating[i] for i, n in enumerate(num_col) if n == search]
        k += 1

    co2_scrubber_rating = report[:]

    k = 0

    while len(co2_scrubber_rating) != 1:
        num_col = tuple(i[k] for i in co2_scrubber_rating)
        num = parse_num(num_col)
        if num.max == num.min:
            search = "0"
        else:
            search = num.min
        co2_scrubber_rating = [co2_scrubber_rating[i] for i, n in enumerate(num_col) if n == search]
        k += 1

    return int(oxygen_generator_rating[0], base=2) * int(co2_scrubber_rating[0], base=2)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
