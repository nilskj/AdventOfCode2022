import re


def solve(gridlines, commands):
    # pad empty space around grid
    max_width = max(map(len, gridlines))
    grid = [gridline + " " * (max_width - len(gridline)) for gridline in gridlines]
    y = 0
    x = 0
    dir_y = 0
    dir_x = 1

    # find starting position in grid
    while grid[y][x] != ".":
        x += 1
        if x == len(grid[y]):
            x = 0
            y += 1

    # parse commands
    commands = re.findall(r"(\d+)([RL]?)", commands)
    for xx, yy in commands:
        xx = int(xx)
        for _ in range(xx):
            next_y = y
            next_x = x

            while True:
                next_y = (next_y + dir_y) % len(grid)
                next_x = (next_x + dir_x) % len(grid[0])
                if grid[next_y][next_x] != " ":
                    break

            if grid[next_y][next_x] == "#":
                break

            # commit actual move
            y = next_y
            x = next_x

        if yy == "L":
            dir_y, dir_x = -dir_x, dir_y
        elif yy == "R":
            dir_y, dir_x = dir_x, -dir_y

    # parse end direction
    end_dir = 0
    if dir_y == 0:
        if dir_x == 1:
            end_dir = 0
        else:
            end_dir = 2
    else:
        if dir_y == 1:
            end_dir = 1
        else:
            end_dir = 3

    return 1000 * (y + 1) + 4 * (x + 1) + end_dir


def main():
    grid = []
    grid_done = False
    commands = ""
    lines = []
    with open("22.txt") as f:
        for line in f.readlines():
            if not line.strip():
                grid_done = True
            if grid_done:
                commands = line
            else:
                grid.append(line.rstrip())
            lines.append(line)

    return solve(grid, commands)


if __name__ == "__main__":
    print(main())
