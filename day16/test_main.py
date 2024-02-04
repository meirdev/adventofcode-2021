from .main import part1, part2


def test_part1():
    for input, expected in (
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ):
        assert part1(input) == expected


def test_part2():
    for input, expected in (
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ):
        assert part2(input) == expected


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 945
    assert part2(input) == 10637009915279
