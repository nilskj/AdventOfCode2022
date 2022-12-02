def solve(lines):
    scores = 0
    for opponent, your_move in lines:

        # loose
        if your_move == "X":
            if opponent == "A":
                scores += 3
            elif opponent == "B":
                scores += 1
            else:
                scores += 2

        # draws
        elif your_move == "Y":
            if opponent == "A":
                scores += 1
            elif opponent == "B":
                scores += 2
            else:
                scores += 3
            scores += 3

        # win
        elif your_move == "Z":
            if opponent == "A":
                scores += 2
            elif opponent == "B":
                scores += 3
            else:
                scores += 1
            scores += 6

    return scores


def main():
    lines = []
    with open("02.txt") as f:
        for line in f.readlines():
            lines.append(line.split())

    return solve(lines)


if __name__ == "__main__":
    print(main())
