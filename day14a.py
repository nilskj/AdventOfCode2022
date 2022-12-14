def solve(lines):

    bottom = 0
    blocked = set()
    for line in lines:
        x = [list(map(int, pair.split(","))) for pair in line.strip().split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted((x1, x2))
            y1, y2 = sorted((y1, y2))

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    blocked.add((x, y))
                    bottom = max(bottom, y + 1)

    t = 0
    reached_bottom = False

    while not reached_bottom:
        x = 500
        y = 0
        while True:
            if y >= bottom:
                reached_bottom = True
                break

            if (x, y + 1) not in blocked:
                y += 1
                continue
            if (x - 1, y + 1) not in blocked:
                x -= 1
                y += 1
                continue
            if (x + 1, y + 1) not in blocked:
                x += 1
                y += 1
                continue
            blocked.add((x, y))
            t += 1
            break

    return t


def main():
    lines = []
    with open("14.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    import time

    start_time = time.time()
    print(main())
    print("--- %s seconds ---" % (time.time() - start_time))
