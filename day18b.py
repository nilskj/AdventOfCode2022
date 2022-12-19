def solve(coords):

    surface_area = 0
    block_set = set()
    for block in coords:
        block_set.add(tuple(block))

    min_x = min([x for x, _, _ in block_set]) - 1
    max_x = max([x for x, _, _ in block_set]) + 1
    min_y = min([y for _, y, _ in block_set]) - 1
    max_y = max([y for _, y, _ in block_set]) + 1
    min_z = min([z for _, _, z in block_set]) - 1
    max_z = max([z for _, _, z in block_set]) + 1

    seen = {(min_x, min_y, min_z)}
    frontier = [(min_x, min_y, min_z)]

    def within_bounds(x, y, z):
        return min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z

    for x, y, z in frontier:
        for delta in (-1, 1):
            for coord in range(3):
                neigh = [x, y, z]
                neigh[coord] += delta
                neigh = tuple(neigh)
                if neigh in block_set:
                    surface_area += 1
                elif within_bounds(*neigh) and neigh not in seen:
                    seen.add(neigh)
                    frontier.append(neigh)
    return surface_area


def main():
    lines = []
    with open("18.txt") as f:
        for line in f.readlines():
            lines.append([int(co) for co in line.strip().split(",")])

    return solve(lines)


if __name__ == "__main__":
    print(main())
