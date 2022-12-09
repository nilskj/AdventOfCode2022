from functools import reduce


def solve(lines):
    def rays(grid, y, x):
        return [
            [grid[y][dx] for dx in range(x)][::-1],
            [grid[y][dx] for dx in range(x + 1, len(grid[0]))],
            [grid[dy][x] for dy in range(y)][::-1],
            [grid[dy][x] for dy in range(y + 1, len(grid))],
        ]

    grid = [[0, 1, 3, 4], ["a", "b", "c", "d"], [7, 8, 9, 10]]
    grid = rays(grid, 2, 3)
    print(grid)

    height = len(lines)
    width = len(lines[0])

    tree_sum_lengths = []
    for i in range(height):
        for j in range(width):
            h = lines[i][j]

            view_lengths = []
            rays_outwards = rays(lines, i, j)

            for ray in rays_outwards:
                length = 0
                for tree in ray:
                    length += 1
                    if tree >= h:
                        break
                view_lengths.append(length)

            tree_sum_lengths.append(reduce(lambda a, b: a * b, view_lengths))
    return max(tree_sum_lengths)


def main():
    lines = []
    with open("08.txt") as f:
        for line in f.readlines():
            lines.append(list(map(int, list(line.rstrip()))))

    return solve(lines)


if __name__ == "__main__":
    print(main())
