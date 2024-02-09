import functools
import itertools
import re
from typing import NamedTuple


class Player(NamedTuple):
    position: int
    score: int = 0

    def update(self, new_position: int) -> "Player":
        return Player(new_position, self.score + new_position)


def parse_input(input: str) -> list[Player]:
    return [
        Player(int(i[0]))
        for i in re.findall(r"Player \d+ starting position: (\d+)", input)
    ]


def part1(input: str) -> int:
    players = parse_input(input)

    rolls = 0

    for i, die in zip(itertools.cycle(range(len(players))), itertools.count(1, 3)):
        player = players[i]

        rolls += 3

        players[i] = player.update((player.position - 1 + die * 3 + 3) % 10 + 1)

        if players[i].score >= 1000:
            break

    return rolls * min(players, key=lambda i: i.score).score


def part2(input: str) -> int:
    players = parse_input(input)

    @functools.cache
    def inner(player1: Player, player2: Player) -> tuple[int, int]:
        wins1, wins2 = 0, 0

        for i in itertools.product((1, 2, 3), repeat=3):
            player1_new = player1.update((player1.position - 1 + sum(i)) % 10 + 1)

            if player1_new.score >= 21:
                wins1 += 1
            else:
                wins2_new, wins1_new = inner(player2, player1_new)
                wins1 += wins1_new
                wins2 += wins2_new

        return wins1, wins2

    return max(inner(*players))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
