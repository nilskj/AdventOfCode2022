def solve(lines):
    cycle = [1]
    x = 1
    for i, line in enumerate(lines):
        command = line.split()
        cycle.append(x)
        if command[0] == "addx":
            cycle.append(x)
            x += int(command[1])

    display = [
        "#" if i % 40 in [x - 1, x, x + 1] else " " for i, x in enumerate(cycle[1:])
    ]

    for i in range(6):
        print("".join(display[i * 40 : i * 40 + 40]))


def main():
    lines = []
    with open("10.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
