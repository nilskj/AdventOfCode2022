import re


def solve(lines):
    sensors = []
    for line in lines:
        re_match = re.match(
            "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
            line,
        )
        if re_match:
            sx, sy, bx, by = map(int, re_match.groups())
            sensors.append(((sx, sy, bx, by)))

    insides = []
    room_y = 2000_000

    for sx, sy, bx, by in sensors:
        distance = abs(sx - bx) + abs(sy - by)
        distance -= abs(room_y - sy)
        if distance >= 0:
            insides.append((sx - distance, sx + distance))

    possible_beacon = []
    for low, high in sorted(insides):
        if possible_beacon and possible_beacon[-1][1] >= low - 1:
            possible_beacon[-1][1] = max(possible_beacon[-1][1], high)
        else:
            possible_beacon.append([low, high])

    return sum(high - low for low, high in possible_beacon)


def main():
    lines = []
    with open("15.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
