import itertools
import re
from typing import Iterator, NamedTuple

import more_itertools


class TargetArea(NamedTuple):
    x_min: int
    x_max: int
    y_min: int
    y_max: int


def parse_input(input: str) -> TargetArea:
    match = re.search(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", input)
    if match is None:
        raise ValueError("invalid input")

    return TargetArea(*map(int, match.groups()))


def trajectory(
    velocity: tuple[int, int], position: tuple[int, int] = (0, 0)
) -> Iterator[tuple[int, int]]:
    x, y = position
    vx, vy = velocity

    while True:
        yield x, y

        x += vx
        y += vy

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1


def solution(input: str) -> Iterator[tuple[bool, list[tuple[int, int]]]]:
    target_area = parse_input(input)

    y_max = max(abs(target_area.y_min), abs(target_area.y_max))

    x = range(target_area.x_max + 1)
    y = range(-y_max, y_max + 1)

    in_target_area = (
        lambda i: target_area.x_min <= i[0] <= target_area.x_max
        and target_area.y_min <= i[1] <= target_area.y_max
    )

    stop = lambda i: i[1] >= target_area.y_min and not in_target_area(i)

    for velocity in itertools.product(x, y):
        trajectory_ = list(
            more_itertools.takewhile_inclusive(stop, trajectory(velocity))
        )
        yield len(trajectory_) > 0 and in_target_area(trajectory_[-1]), trajectory_


def part1(input: str) -> int:
    return max(
        max(y for _, y in trajectory_) for ok, trajectory_ in solution(input) if ok
    )


def part2(input: str) -> int:
    return sum(1 for ok, _ in solution(input) if ok)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
