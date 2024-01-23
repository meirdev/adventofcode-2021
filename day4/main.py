import dataclasses
import itertools
import re
from typing import Iterator, NamedTuple, TypeAlias

import more_itertools

Numbers: TypeAlias = list[int]


@dataclasses.dataclass
class Slot:
    number: int
    is_marked: bool = False

    def mark(self) -> None:
        self.is_marked = True


@dataclasses.dataclass
class Board:
    rows: list[list[Slot]]

    def get_slots(self) -> Iterator[Slot]:
        yield from itertools.chain.from_iterable(self.rows)

    def check_number(self, number: int) -> bool:
        slot = next((slot for slot in self.get_slots() if slot.number == number), None)

        if slot:
            slot.mark()
            return True

        return False

    def get_unmarked_numbers(self) -> list[int]:
        return [slot.number for slot in self.get_slots() if not slot.is_marked]

    def is_win(self) -> bool:
        for numbers in (self.rows, zip(*self.rows)):
            if any(all(i.is_marked for i in cols) for cols in numbers):
                return True

        return False


class Bingo(NamedTuple):
    numbers: Numbers
    boards: list[Board]


def to_ints(s: list[str]) -> list[int]:
    return list(map(int, s))


def parse_input(input: str) -> Bingo:
    rows = input.strip().splitlines()

    boards: list[Board] = []

    for i in range(2, len(rows), 6):
        board = []
        for j in range(5):
            board.append(
                list(map(Slot, to_ints(re.split(r"\s+", rows[i + j].strip()))))
            )
        boards.append(Board(board))

    return Bingo(
        numbers=to_ints(rows[0].split(",")),
        boards=boards,
    )


def solution(input: str) -> Iterator[int]:
    bingo = parse_input(input)

    winners = {}

    for number in bingo.numbers:
        for i, board in enumerate(bingo.boards):
            if i not in winners:
                if board.check_number(number):
                    if board.is_win():
                        yield sum(board.get_unmarked_numbers() * number)
                        winners[i] = number


def part1(input: str) -> int:
    return next(solution(input))


def part2(input: str) -> int:
    return more_itertools.last(solution(input))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
