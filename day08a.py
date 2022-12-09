def solve(lines):
    def rays(grid, y, x):
        return [
            [grid[y][dx] for dx in range(x)],
            [grid[y][dx] for dx in range(x + 1, len(grid[0]))],
            [grid[dy][x] for dy in range(y)],
            [grid[dy][x] for dy in range(y + 1, len(grid))],
        ]

    height = len(lines)
    width = len(lines[0])
    num_visible = 0

    for i in range(height):
        for j in range(width):
            if any(
                ray == [] or all(tree < lines[i][j] for tree in ray)
                for ray in rays(lines, i, j)
            ):
                num_visible += 1

    return num_visible


def main():
    lines = []
    with open("08.txt") as f:
        for line in f.readlines():
            lines.append(list(map(int, list(line.rstrip()))))

    return solve(lines)


if __name__ == "__main__":
    print(main())
