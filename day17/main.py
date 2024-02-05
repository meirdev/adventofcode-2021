import functools
import itertools
import re
from typing import Iterator, NamedTuple, TypeAlias


Txy: TypeAlias = tuple[int, int]


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


@functools.cache
def trajectory(
    velocity: Txy, target_area: TargetArea, position: Txy = (0, 0)
) -> list[Txy] | None:
    x, y = position
    vx, vy = velocity

    positions = []

    while True:
        positions.append((x, y))

        x += vx
        y += vy

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        if (
            target_area.x_min <= x <= target_area.x_max
            and target_area.y_min <= y <= target_area.y_max
        ):
            return positions

        if y < target_area.y_min:
            return None


def solution(input: str) -> Iterator[list[Txy] | None]:
    target_area = parse_input(input)

    y_max = max(abs(target_area.y_min), abs(target_area.y_max))

    x = range(target_area.x_max + 1)
    y = range(-y_max, y_max + 1)

    for velocity in itertools.product(x, y):
        yield trajectory(velocity, target_area)


def part1(input: str) -> int:
    return max(
        max(y for _, y in trajectory_) for trajectory_ in solution(input) if trajectory_
    )


def part2(input: str) -> int:
    return sum(1 for trajectory_ in solution(input) if trajectory_)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
