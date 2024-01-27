import collections
import enum


class Segment(enum.IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6


DIGITS = {
    0: {Segment.A, Segment.B, Segment.C, Segment.E, Segment.F, Segment.G},
    1: {Segment.C, Segment.F},
    2: {Segment.A, Segment.C, Segment.D, Segment.E, Segment.G},
    3: {Segment.A, Segment.C, Segment.D, Segment.F, Segment.G},
    4: {Segment.B, Segment.C, Segment.D, Segment.F},
    5: {Segment.A, Segment.B, Segment.D, Segment.F, Segment.G},
    6: {Segment.A, Segment.B, Segment.D, Segment.E, Segment.E, Segment.G},
    7: {Segment.A, Segment.C, Segment.F},
    8: {Segment.A, Segment.B, Segment.C, Segment.D, Segment.E, Segment.F, Segment.G},
    9: {Segment.A, Segment.B, Segment.C, Segment.D, Segment.F, Segment.G},
}


def parse_input(input: str) -> list[tuple[list[str], list[str]]]:
    rows = []

    for row in input.strip().splitlines():
        segments = row.strip().split(" ")
        idx = segments.index("|")
        rows.append((segments[:idx], segments[idx + 1 :]))

    return rows


def part1(input: str) -> int:
    parsed = parse_input(input)

    easy_digits = {len(DIGITS[i]) for i in (1, 4, 7, 8)}

    return sum(len(i) in easy_digits for _, output in parsed for i in output)


def part2(input: str) -> int:
    parsed = parse_input(input)

    output_sum = 0

    for signal_patterns, output in parsed:
        n_segments = collections.defaultdict(list)
        for i in signal_patterns:
            n_segments[len(i)].append(set(i))

        numbers = {
            1: n_segments[2][0],
            4: n_segments[4][0],
            7: n_segments[3][0],
            8: n_segments[7][0],
        }

        numbers[9] = next(i for i in n_segments[6] if len(i & numbers[4]) == 4)
        n_segments[6].remove(numbers[9])

        numbers[3] = next(i for i in n_segments[5] if len(i & numbers[1]) == 2)
        n_segments[5].remove(numbers[3])

        numbers[5] = next(i for i in n_segments[5] if len(i & numbers[9]) == 5)
        n_segments[5].remove(numbers[5])

        numbers[2] = n_segments[5][0]

        numbers[6] = next(i for i in n_segments[6] if len(i & numbers[5]) == 5)
        n_segments[6].remove(numbers[6])

        numbers[0] = n_segments[6][0]

        inverted = {tuple(sorted(j)): i for i, j in numbers.items()}

        output_sum += int("".join(f"{inverted[tuple(sorted(i))]}" for i in output))

    return output_sum


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
