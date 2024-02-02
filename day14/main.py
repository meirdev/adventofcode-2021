import collections
import itertools
import re
from typing import Counter


def parse_input(input: str) -> tuple[str, dict[tuple[str, str], str]]:
    polymer_template, pairs = input.strip().split("\n", maxsplit=1)

    return polymer_template, {
        (a, b): c for a, b, c in re.findall(r"(\w)(\w) -> (\w+)", pairs)
    }


def solution(input: str, steps: int) -> int:
    polymer_template, pairs = parse_input(input)

    template_pairs = collections.Counter(itertools.pairwise(polymer_template))

    for _ in range(steps):
        temp_template_pairs: Counter[tuple[str, str]] = collections.Counter()

        elements = collections.Counter([polymer_template[-1]])

        for i in template_pairs.keys():
            pair = pairs[i]

            elements[i[0]] += template_pairs[i]
            elements[pair] += template_pairs[i]

            temp_template_pairs[(i[0], pair)] += template_pairs[i]
            temp_template_pairs[(pair, i[1])] += template_pairs[i]

        template_pairs = temp_template_pairs

    return max(elements.values()) - min(elements.values())


def part1(input: str) -> int:
    return solution(input, 10)


def part2(input: str) -> int:
    return solution(input, 40)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
