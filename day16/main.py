import enum
import math
from typing import TypeAlias

Hex: TypeAlias = int

Bin: TypeAlias = str


class TypeId(enum.IntEnum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL_VALUE = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


class LengthTypeId(enum.IntEnum):
    TOTAL_LENGTH = 0
    NUM_SUB_PACKETS = 1


def parse_input(input: str) -> list[Hex]:
    return [int(i, base=16) for i in input.strip()]


def bin_to_int(l: Bin) -> int:
    return int(l, base=2)


def solution(input: str) -> tuple[int, list[int], int]:
    message = parse_input(input)

    def parse(binary: Bin, packets: float = float("inf")):
        versions = 0
        idx = 0
        values = []

        while any(i == "1" for i in binary) and packets > 0:
            version, type_id, binary = (
                bin_to_int(binary[:3]),
                bin_to_int(binary[3:6]),
                binary[6:],
            )
            idx += 6

            versions += version

            if type_id == TypeId.LITERAL_VALUE:
                num = ""
                prefix: str | None = None

                while prefix != "0":
                    prefix, num, binary = binary[0], num + binary[1:5], binary[5:]
                    idx += 5

                values += [bin_to_int(num)]
            else:
                length_type_id, binary = binary[0], binary[1:]

                if int(length_type_id) == LengthTypeId.TOTAL_LENGTH:
                    total_length, binary = bin_to_int(binary[:15]), binary[15:]
                    _, packet_values, packet_versions = parse(binary[:total_length])
                    idx += 16 + total_length
                else:
                    sub_packets, binary = bin_to_int(binary[:11]), binary[11:]
                    total_length, packet_values, packet_versions = parse(
                        binary, sub_packets
                    )
                    idx += 12 + total_length

                binary = binary[total_length:]

                versions += packet_versions

                match type_id:
                    case TypeId.SUM:
                        values += [sum(packet_values)]
                    case TypeId.PRODUCT:
                        values += [math.prod(packet_values)]
                    case TypeId.MINIMUM:
                        values += [min(packet_values)]
                    case TypeId.MAXIMUM:
                        values += [max(packet_values)]
                    case TypeId.GREATER_THAN:
                        values += [int(packet_values[0] > packet_values[1])]
                    case TypeId.LESS_THAN:
                        values += [int(packet_values[0] < packet_values[1])]
                    case TypeId.EQUAL_TO:
                        values += [int(packet_values[0] == packet_values[1])]

            packets -= 1

        return idx, values, versions

    return parse("".join(f"{i:04b}" for i in message))


def part1(input: str) -> int:
    return solution(input)[2]


def part2(input: str) -> int:
    return solution(input)[1][0]


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
