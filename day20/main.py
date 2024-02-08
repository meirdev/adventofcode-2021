from typing import TypeAlias

Image: TypeAlias = list[list[str]]


def parse_input(input: str) -> tuple[str, Image]:
    algorithm, input_image = input.strip().split("\n\n")

    return algorithm, [list(row) for row in input_image.split("\n")]


def solution(input: str, enhance: int) -> int:
    algorithm, input_image = parse_input(input)

    for i in range(1, enhance + 1):
        default = (
            "#" if algorithm[0] == "#" and algorithm[-1] == "." and not i % 2 else "."
        )

        width = len(input_image[0])

        input_image.insert(0, [default] * width)
        input_image.append([default] * width)

        for row in input_image:
            row.insert(0, default)
            row.append(default)

        output = {}

        for y in range(len(input_image)):
            for x in range(len(input_image[y])):
                binary_number = [
                    int(
                        (
                            input_image[yi][xi]
                            if 0 <= yi < len(input_image)
                            and 0 <= xi < len(input_image[yi])
                            else default
                        )
                        == "#"
                    )
                    for yi in range(y - 1, y + 2)
                    for xi in range(x - 1, x + 2)
                ]

                output[y, x] = algorithm[int("".join(map(str, binary_number)), base=2)]

        lit = 0

        for (y, x), pixel in output.items():
            lit += pixel == "#"
            input_image[y][x] = pixel

    return lit


def part1(input: str) -> int:
    return solution(input, 2)


def part2(input: str) -> int:
    return solution(input, 50)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
