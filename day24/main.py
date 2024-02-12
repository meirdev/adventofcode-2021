import enum
from typing import TypeAlias

Varibles: TypeAlias = dict[str, int]


class Instruction(enum.IntEnum):
    INP = 0
    ADD = 1
    MUL = 2
    DIV = 3
    MOD = 4
    EQL = 5


Instructions: TypeAlias = list[tuple[Instruction, str, int | str | None]]


def parse_input(input: str) -> Instructions:
    instructions: Instructions = []

    def val(i: str) -> str | int:
        return i if i in ["w", "x", "y", "z"] else int(i)

    for line in input.strip().splitlines():
        instruction, *ops = line.split(" ")

        match instruction:
            case "inp":
                instructions.append((Instruction.INP, ops[0], None))
            case "add":
                instructions.append((Instruction.ADD, ops[0], val(ops[1])))
            case "mul":
                instructions.append((Instruction.MUL, ops[0], val(ops[1])))
            case "div":
                instructions.append((Instruction.DIV, ops[0], val(ops[1])))
            case "mod":
                instructions.append((Instruction.MOD, ops[0], val(ops[1])))
            case "eql":
                instructions.append((Instruction.EQL, ops[0], val(ops[1])))

    return instructions


def run(instructions: str, input: list[int]) -> Varibles:
    variables = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    for instruction in parse_input(instructions):
        match instruction:
            case Instruction.INP, a, _:
                variables[a] = input.pop(0)
            case Instruction.ADD, a, b:
                variables[a] += variables.get(b, b)
            case Instruction.MUL, a, b:
                variables[a] *= variables.get(b, b)
            case Instruction.DIV, a, b:
                variables[a] //= variables.get(b, b)
            case Instruction.MOD, a, b:
                variables[a] %= variables.get(b, b)
            case Instruction.EQL, a, b:
                variables[a] = int(variables[a] == variables.get(b, b))

    return variables


def solution(input: str) -> tuple[int, int]:
    instructions = parse_input(input)

    stack = []

    largest, smallest = 99999999999999, 11111111111111

    for i in range(14):
        a = int(instructions[18 * i + 5][-1])  # type: ignore
        b = int(instructions[18 * i + 15][-1])  # type: ignore

        if a > 0:
            stack += [(i, b)]
            continue

        j, b = stack.pop()

        largest -= abs((a + b) * 10 ** (13 - [i, j][a > -b]))
        smallest += abs((a + b) * 10 ** (13 - [i, j][a < -b]))

    return largest, smallest


def part1(input: str) -> int:
    return solution(input)[0]


def part2(input: str):
    return solution(input)[1]


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
