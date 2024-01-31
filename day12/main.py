import collections

import more_itertools


def parse_input(input: str) -> list[tuple[str, ...]]:
    return [tuple(line.split("-")) for line in input.strip().splitlines()]


def solution(input: str, twice: bool = False) -> int:
    edges = parse_input(input)

    small_caves = {
        i
        for i in more_itertools.flatten(edges)
        if i.islower() and i not in ["start", "end"]
    }

    graph = collections.defaultdict(set)

    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    def rec(a: str, path: list[str]) -> int:
        if a == "end":
            return 1

        twice_in_path = not twice or any(
            path.count(i) == 2 for i in path if i in small_caves
        )

        return sum(
            rec(b, path + [b])
            for b in graph[a]
            if not (
                (b in path and b in small_caves and twice_in_path) or (b == "start")
            )
        )

    return rec("start", ["start"])


def part1(input: str) -> int:
    return solution(input)


def part2(input: str) -> int:
    return solution(input, True)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
