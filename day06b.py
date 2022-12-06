def solve(lines, packet_size=4):
    letters = []

    def all_different(s):
        return len(s) >= packet_size and len(s) == len(set(s))

    count = 0
    for ch in lines[0]:
        count += 1
        letters.append(ch)
        if len(letters) >= packet_size and all_different(letters[-packet_size:]):
            return count


def main():
    lines = []
    with open("06.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines, 14)


if __name__ == "__main__":
    print(main())
