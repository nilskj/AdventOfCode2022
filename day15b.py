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

    search_space = 4000_000

    def find_exl(excluded_intervals):
        excluded_intervals = sorted(excluded_intervals)
        candidate = 0
        for f, t in excluded_intervals:
            if candidate < f:
                return candidate
            candidate = max(candidate, t + 1)
        return candidate if candidate < search_space else -1

    x = y = -1
    for step in range(search_space + 1):
        ex, ey = [], []
        for (sx, sy, bx, by) in sensors:
            distance = abs(sx - bx) + abs(sy - by)
            if distance >= abs(step - sy):
                distance_y = distance - abs(step - sy)
                ey.append((max(sx - distance_y, 0), min(sx + distance_y, search_space)))
            if distance >= abs(step - sx):
                distance_x = distance - abs(step - sx)
                ex.append((max(sy - distance_x, 0), min(sy + distance_x, search_space)))
        y = max(y, find_exl(ex))
        x = max(x, find_exl(ey))
    return x * 4000_000 + y


def main():
    lines = []
    with open("15.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    import time

    start_time = time.time()
    print(main())
    print("--- %s seconds ---" % (time.time() - start_time))
