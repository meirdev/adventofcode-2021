import itertools

import networkx as nx  # type: ignore


def parse_input(input: str) -> list[list[int]]:
    return [list(map(int, row)) for row in input.strip().splitlines()]


def solution(input: str, size: int) -> int:
    cavern = parse_input(input)

    height, width = len(cavern), len(cavern[0])

    grid = [[0] * (width * size) for _ in range(height * size)]

    grid_height, grid_width = height * size, width * size

    for row, col in itertools.product(range(grid_height), range(grid_width)):
        value = cavern[row % height][col % width] + (row // height) + (col // width)
        grid[row][col] = value - 9 if value > 9 else value

    G: nx.DiGraph = nx.grid_2d_graph(grid_height, grid_width, create_using=nx.DiGraph)

    for n, (x, y) in G.edges:
        G[n][(x, y)]["weight"] = grid[y][x]

    return nx.shortest_path_length(
        G, (0, 0), (grid_height - 1, grid_width - 1), weight="weight"
    )


def part1(input: str) -> int:
    return solution(input, 1)


def part2(input: str) -> int:
    return solution(input, 5)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
