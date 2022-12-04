def solve(lines):
    overlaps = 0
    for line in lines:
        left, right = line.split(",")
        left = left.split("-")
        right = right.split("-")
        left = [int(x) for x in left]
        right = [int(x) for x in right]

        if set(range(left[0], left[1] + 1)) & set(range(right[0], right[1] + 1)):
            overlaps += 1

    return overlaps


def main():
    lines = []
    with open("04.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
