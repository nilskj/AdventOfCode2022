def solve(lines):

    height = len(lines)
    width = len(lines[0])

    sy = -1
    sx = -1
    ex = -1
    ey = -1

    for y in range(height):
        for x in range(width):
            if lines[y][x] == "S":
                sy = y
                sx = x
            if lines[y][x] == "E":
                ey = y
                ex = x

    visited = set()
    visited.add((sy, sx))

    front = [[0, sy, sx]]

    for steps, y, x in front:
        if y == ey and x == ex:
            return steps

        h = ord("a") if y == sy and x == sx else ord(lines[y][x])

        neighs = []

        if y > 0:
            neighs.append([y - 1, x])

        if y < height - 1:
            neighs.append([y + 1, x])

        if x > 0:
            neighs.append([y, x - 1])

        if x < width - 1:
            neighs.append([y, x + 1])

        for ny, nx in neighs:
            if (ny, nx) in visited:
                continue

            nh = ord(lines[ny][nx]) if lines[ny][nx].islower() else ord("z")

            if nh - h > 1:
                continue

            visited.add((ny, nx))
            front.append((steps + 1, ny, nx))


def main():
    lines = []
    with open("12.txt") as f:
        for line in f.readlines():
            lines.append(line.rstrip())

    return solve(lines)


if __name__ == "__main__":
    print(main())
