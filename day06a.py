def solve(lines):
    letters = []

    def all_different(s):
        return len(s) > 3 and len(s) == len(set(s))

    count = 0
    for ch in lines[0]:
        count += 1
        letters.append(ch)
        if len(letters) > 3 and all_different(letters[-4:]):
            return count


def main():
    lines = []
    with open("06.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
