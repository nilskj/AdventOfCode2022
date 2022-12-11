def solve(lines):
    visited = set()
    visited.add((0, 0))

    hy = 0
    hx = 0
    ty = 0
    tx = 0

    for line in lines:
        command = line.split()
        direction = command[0]
        step = int(command[1])
        for _ in range(step):
            # move head
            if direction == "U":
                hy -= 1
            elif direction == "D":
                hy += 1
            elif direction == "L":
                hx -= 1
            elif direction == "R":
                hx += 1

            nexty = hy
            nextx = hx
            tail_x = tx
            tail_y = ty

            # move tail
            if abs(nexty - tail_y) >= 2 or abs(nextx - tail_x) >= 2:
                dx = 0
                dy = 0
                if nexty > tail_y:
                    dy = 1
                elif nexty < tail_y:
                    dy = -1

                if nextx > tail_x:
                    dx = 1
                elif nextx < tail_x:
                    dx = -1

                tail_y += dy
                tail_x += dx

            ty = tail_y
            tx = tail_x
            nexty = tail_y
            nextx = tail_x

            visited.add((ty, tx))
    return len(visited)


def main():
    lines = []
    with open("09.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
