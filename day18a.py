def solve(coords):

    surface_area = 0
    block_set = set()
    for block in coords:
        block_set.add(tuple(block))

    for block in block_set:
        collisions = 0
        x, y, z = block
        for x2, y2, z2 in block_set:
            if x == x2 and y == y2 and z == z2:
                continue
            if abs(x - x2) + abs(y - y2) + abs(z - z2) <= 1:
                collisions += 1
        surface_area += 6 - collisions

    return surface_area


def main():
    lines = []
    with open("18.txt") as f:
        for line in f.readlines():
            lines.append([int(co) for co in line.strip().split(",")])

    return solve(lines)


if __name__ == "__main__":
    print(main())
