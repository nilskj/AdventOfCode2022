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
            next_y = y + dir_y
            next_x = x + dir_x

            current_dir_y = dir_y
            current_dir_x = dir_x

            # check all 14 "portals" for next positions
            if next_y < 0 and 50 <= next_x < 100 and dir_y == -1:
                dir_y, dir_x = 0, 1
                next_y, next_x = next_x + 100, 0
            elif next_x < 0 and 150 <= next_y < 200 and dir_x == -1:
                dir_y, dir_x = 1, 0
                next_y, next_x = 0, next_y - 100
            elif next_y < 0 and 100 <= next_x < 150 and dir_y == -1:
                next_y, next_x = 199, next_x - 100
            elif next_y >= 200 and 0 <= next_x < 50 and dir_y == 1:
                next_y, next_x = 0, next_x + 100
            elif next_x >= 150 and 0 <= next_y < 50 and dir_x == 1:
                dir_x = -1
                next_y, next_x = 149 - next_y, 99
            elif next_x == 100 and 100 <= next_y < 150 and dir_x == 1:
                dir_x = -1
                next_y, next_x = 149 - next_y, 149
            elif next_y == 50 and 100 <= next_x < 150 and dir_y == 1:
                dir_y, dir_x = 0, -1
                next_y, next_x = next_x - 50, 99
            elif next_x == 100 and 50 <= next_y < 100 and dir_x == 1:
                dir_y, dir_x = -1, 0
                next_y, next_x = 49, next_y + 50
            elif next_y == 150 and 50 <= next_x < 100 and dir_y == 1:
                dir_y, dir_x = 0, -1
                next_y, next_x = next_x + 100, 49
            elif next_x == 50 and 150 <= next_y < 200 and dir_x == 1:
                dir_y, dir_x = -1, 0
                next_y, next_x = 149, next_y - 100
            elif next_y == 99 and 0 <= next_x < 50 and dir_y == -1:
                dir_y, dir_x = 0, 1
                next_y, next_x = next_x + 50, 50
            elif next_x == 49 and 50 <= next_y < 100 and dir_x == -1:
                dir_y, dir_x = 1, 0
                next_y, next_x = 100, next_y - 50
            elif next_x == 49 and 0 <= next_y < 50 and dir_x == -1:
                dir_x = 1
                next_y, next_x = 149 - next_y, 0
            elif next_x < 0 and 100 <= next_y < 150 and dir_x == -1:
                dir_x = 1
                next_y, next_x = 149 - next_y, 50

            if grid[next_y][next_x] == "#":
                dir_y = current_dir_y
                dir_x = current_dir_x
                break

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
