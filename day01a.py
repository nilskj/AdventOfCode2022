def solve(lines):
    max_cal = 0
    group = 0
    for i in lines:
        if i.strip():
            group += int(i)
        else:
            if group > max_cal:
                max_cal = group
            group = 0
    return max_cal


def main():
    lines = []
    with open("01.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
