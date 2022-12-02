def solve(lines):
    scores = 0
    for opponent, your_move in lines:

        diff_opponent = ord(opponent) - ord("A")
        diff_your_move = ord(your_move) - ord("X")

        if diff_opponent == diff_your_move:
            scores += 3
        if (diff_your_move - 1) % 3 == diff_opponent:
            scores += 6

        scores += diff_your_move + 1

    return scores


def main():
    lines = []
    with open("02.txt") as f:
        for line in f.readlines():
            lines.append(line.split())

    return solve(lines)


if __name__ == "__main__":
    print(main())
