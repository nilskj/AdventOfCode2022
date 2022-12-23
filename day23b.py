def neighbours_8(elf_complex):
    neighbours = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            neighbours.append(elf_complex + complex(x, y))
    return neighbours


def print_rect(elves):
    min_width = min(int(x.real) for x in elves)
    max_width = max(int(x.real) for x in elves)
    max_height = max(int(x.imag) for x in elves)
    min_height = min(int(x.imag) for x in elves)

    e = 0
    for y in range(min_height, max_height + 1):
        for x in range(min_width, max_width + 1):
            if complex(x, y) in elves:
                print("#", end="")
            else:
                e += 1
                print(".", end="")
        print()

    return (max_width - min_width, max_height - min_height, e)


def solve(lines):

    num_rounds = 1000

    # parse grid
    elves = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                elf = complex(x, y)
                elves.add(elf)

    dirs = [complex(0, -1), complex(0, 1), complex(-1, 0), complex(1, 0)]
    scan = {
        complex(0, -1): [-1j - 1, -1j, -1j + 1],
        complex(0, 1): [1j - 1, 1j, 1j + 1],
        complex(1, 0): [1 - 1j, 1, 1 + 1j],
        complex(-1, 0): [-1 - 1j, -1, -1 + 1j],
    }

    last_grid = set(elves)
    for r in range(num_rounds):
        dir_num = r % 4
        destinations = set()
        conflicts = set()

        # consider
        for elf in elves:
            neighbours = neighbours_8(elf)
            close_elves = [n for n in neighbours if n in elves]
            if len(close_elves) == 0:
                continue

            for i in range(4):
                target_dir = (dir_num + i) % 4
                if all([elf + x not in elves for x in scan[dirs[target_dir]]]):
                    proposed = elf + dirs[target_dir]
                    if proposed in conflicts:
                        pass
                    if proposed in destinations:
                        conflicts.add(proposed)
                    else:
                        destinations.add(proposed)
                    break

        clone = set(elves)

        # commit
        for elf in clone:
            neighbours = neighbours_8(elf)
            close_elves = [n for n in neighbours if n in clone]
            if len(close_elves) == 0:
                continue

            for i in range(4):
                target_dir = (dir_num + i) % 4
                if all([elf + x not in clone for x in scan[dirs[target_dir]]]):
                    proposed = elf + dirs[target_dir]
                    if proposed not in conflicts:
                        elves.remove(elf)
                        elves.add(proposed)
                    break

        if last_grid == elves:
            print(r + 1)
            return r + 1
        last_grid = set(elves)

    return print_rect(elves)


def main():
    lines = []
    with open("23.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
