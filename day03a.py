def solve(lines):
    priorities = 0
    for line in lines:
        middle = len(line) >> 1
        [comp1, comp2] = line[:middle], line[middle:]
        [in_both] = set(comp1) & set(comp2)
        char_code = ord(in_both)

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
