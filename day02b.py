def solve(lines):
    scores = 0
    for opponent, your_move in lines:

        diff_opponent = ord(opponent) - ord("A")
        diff_your_move = ord(your_move) - ord("X")

        scores += 3 * diff_your_move

        # loose
        if your_move == "X":
            scores += (diff_opponent - 1) % 3 + 1

        # draw
        elif your_move == "Y":
            scores += diff_opponent + 1

        # win
        elif your_move == "Z":
            scores += (diff_opponent + 1) % 3 + 1

    return scores


def main():
    lines = []
    with open("02.txt") as f:
        for line in f.readlines():
            lines.append(line.split())

    return solve(lines)


if __name__ == "__main__":
    print(main())
