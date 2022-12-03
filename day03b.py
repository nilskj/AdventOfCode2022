def solve(lines):
    priorities = 0
    for i in range(0, len(lines), 3):
        [in_all] = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
        char_code = ord(in_all)

        p = char_code - 65 + 27 if char_code < 97 else char_code - 96
        priorities += p
    return priorities


def main():
    lines = []
    with open("03.txt") as f:
        for line in f.readlines():
            lines.append(line.strip())

    return solve(lines)


if __name__ == "__main__":
    print(main())
