def solve(lines):
    scores = 0
    for opponent, your_move in lines:

        # Sten
        if your_move == "X":
            if opponent == "A":
                scores += 3
            elif opponent == "C":
                scores += 6
            scores += 1

        # Sax
        elif your_move == "Y":
            if opponent == "B":
                scores += 3
            elif opponent == "A":
                scores += 6
            scores += 2

        # Påse
        elif your_move == "Z":
            if opponent == "C":
                scores += 3
            elif opponent == "B":
                scores += 6
            scores += 3

    return scores


def main():
    lines = []
    with open("02.txt") as f:
        for line in f.readlines():
            lines.append(line.split())

    return solve(lines)


if __name__ == "__main__":
    print(main())
