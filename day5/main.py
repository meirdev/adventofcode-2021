import collections
import dataclasses
import itertools
import re
from typing import Counter


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclasses.dataclass
class Line:
    a: Point
    b: Point

    def points(self, diagonal: bool = False) -> list[Point]:
        x_min = min(self.a, self.b, key=lambda i: i.x)
        x_max = max(self.a, self.b, key=lambda i: i.x)
        y_min = min(self.a, self.b, key=lambda i: i.y)
        y_max = max(self.a, self.b, key=lambda i: i.y)

        x_y = None

        if self.a.x == self.b.x:
            x_y = itertools.cycle([self.a.x]), range(y_min.y, y_max.y + 1)
        elif self.a.y == self.b.y:
            x_y = range(x_min.x, x_max.x + 1), itertools.cycle([self.a.y])
        elif diagonal:
            x_y = itertools.count(y_min.x, 1 if y_min.x <= y_max.x else -1), range(
                y_min.y, y_max.y + 1
            )

        if x_y:
            return [Point(x, y) for x, y in zip(*x_y)]

        return []


def parse_input(input: str) -> list[Line]:
    lines = []
    for i in re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", input):
        x1, y1, x2, y2 = map(int, i)
        lines.append(Line(Point(x1, y1), Point(x2, y2)))
    return lines


def solution(input: str, diagonal: bool) -> int:
    lines = parse_input(input)

    intersections = collections.Counter(
        itertools.chain.from_iterable(i.points(diagonal) for i in lines)
    )

    return sum(i > 1 for i in intersections.values())


def draw(points: Counter[Point]) -> None:
    x_min = min(i.x for i in points)
    x_max = max(i.x for i in points)
    y_min = min(i.y for i in points)
    y_max = max(i.y for i in points)

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            n = points[Point(x, y)]
            print(f"{'.' if n == 0 else n}", end="")
        print()


def part1(input: str) -> int:
    return solution(input, False)


def part2(input: str) -> int:
    return solution(input, True)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
