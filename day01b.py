def solve(lines):
    elves = []
    food = []
    for i in lines:
        if i.strip():
            food.append(int(i))
        else:
            elves.append(food)
            food = []

    elves.append(food)

    calory_sums = [sum(int(c) for c in e) for e in elves]
    return sum(sorted(calory_sums)[-3:])


def main():
    lines = []
    with open("01.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
