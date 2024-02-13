def parse_input(input: str) -> list[list[str]]:
    return list(map(list, input.strip().splitlines()))


def part1(input: str) -> int:
    sea_cucumbers = parse_input(input)

    steps = 0

    moving = True

    while moving:
        moving = False

        for y in range(len(sea_cucumbers)):
            temp = {}

            for x in range(len(sea_cucumbers[y])):
                value = sea_cucumbers[y][x]

                if value == ">":
                    if x + 1 < len(sea_cucumbers[y]) and sea_cucumbers[y][x + 1] == ".":
                        temp[x] = x + 1
                    elif x + 1 == len(sea_cucumbers[y]) and sea_cucumbers[y][0] == ".":
                        temp[x] = 0

            if len(temp) > 0:
                for f, t in temp.items():
                    sea_cucumbers[y][f] = "."
                    sea_cucumbers[y][t] = ">"

                moving = True

        for x in range(len(sea_cucumbers[0])):
            temp = {}

            for y in range(len(sea_cucumbers)):
                value = sea_cucumbers[y][x]

                if value == "v":
                    if y + 1 < len(sea_cucumbers) and sea_cucumbers[y + 1][x] == ".":
                        temp[y] = y + 1
                    elif y + 1 == len(sea_cucumbers) and sea_cucumbers[0][x] == ".":
                        temp[y] = 0

            if len(temp) > 0:
                for f, t in temp.items():
                    sea_cucumbers[f][x] = "."
                    sea_cucumbers[t][x] = "v"

                moving = True

        steps += 1

    return steps


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))


if __name__ == "__main__":
    main()
