import enum
import collections
import itertools
import re
from typing import Counter, NamedTuple, Optional, TypeAlias


class State(enum.IntEnum):
    OFF = -1
    ON = 1


class Range(NamedTuple):
    start: int
    stop: int

    def intersection(self, other: "Range") -> Optional["Range"]:
        start, stop = max(self.start, other.start), min(self.stop, other.stop)

        if start <= stop:
            return Range(start, stop)

        return None


Txyz: TypeAlias = tuple[Range, Range, Range]


class RebootSteps(NamedTuple):
    state: State
    xyz: Txyz


def parse_input(input: str) -> list[RebootSteps]:
    reboot_steps = []

    for state_, *ranges_ in re.findall(
        r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", input
    ):
        state = State.ON if state_ == "on" else State.OFF

        x, y, z = [
            Range(min_, max_) for min_, max_ in itertools.batched(map(int, ranges_), 2)
        ]

        reboot_steps.append(RebootSteps(state, (x, y, z)))

    return reboot_steps


def solution(reboot_steps: list[RebootSteps]) -> int:
    cubes: Counter[Txyz] = collections.Counter()

    for state, (x, y, z) in reboot_steps:
        update: Counter[Txyz] = collections.Counter()

        for (x1, y1, z1), state1 in cubes.items():
            x2 = x.intersection(x1)
            y2 = y.intersection(y1)
            z2 = z.intersection(z1)

            if x2 and y2 and z2:
                update[(x2, y2, z2)] -= state1

        if state == State.ON:
            update[(x, y, z)] += State.ON

        cubes.update(update)

    return sum(
        (x.stop - x.start + 1) * (y.stop - y.start + 1) * (z.stop - z.start + 1) * state
        for (x, y, z), state in cubes.items()
    )


def part1(input: str) -> int:
    reboot_steps_list = parse_input(input)

    return solution(
        [
            i
            for i in reboot_steps_list
            if all(-50 <= range_.start and range_.stop <= 50 for range_ in i.xyz)
        ]
    )


def part2(input: str) -> int:
    reboot_steps_list = parse_input(input)

    return solution(reboot_steps_list)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
