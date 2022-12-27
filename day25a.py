def solve(lines):

    total = 0

    for line in lines:
        coef = 1
        for x in line[::-1]:
            total += ("=-012".find(x) - 2) * coef
            coef *= 5

    output = ""

    while total:
        rem = total % 5
        total //= 5

        if rem <= 2:
            output = str(rem) + output
        else:
            if rem == 3:
                output = "=" + output
            elif rem == 4:
                output = "-" + output
            total += 1
    return output


def main():
    lines = []
    with open("25.txt") as f:
        for line in f.readlines():
            lines.append(line.strip())

    return solve(lines)


if __name__ == "__main__":
    print(main())
