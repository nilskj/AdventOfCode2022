def solve(lines):
    cycle = [1]
    x = 1
    for line in lines:
        command = line.split()
        cycle.append(x)
        if command[0] == "addx":
            cycle.append(x)
            x += int(command[1])

    zipped = list(zip(cycle[20::40], [i for i in range(20, 240, 40)]))
    return sum([x * y for (x, y) in zipped])


def main():
    lines = []
    with open("10.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
