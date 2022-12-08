def solve(lines):
    dir_sizes = []

    def walk(input, dir_sizes):
        size = 0
        try:
            while current_line := input.pop(0):
                parts = current_line.split()
                if parts[0] == "$":
                    if parts[1] == "cd" and parts[2] == "..":
                        dir_sizes.append(size)
                        return size
                    elif parts[1] == "cd":
                        size += walk(input, dir_sizes)
                elif parts[0] == "dir":
                    pass
                else:
                    size += int(parts[0])
        except:
            # dont care if we could'nt pop
            pass
        return size

    total_size = walk(lines, dir_sizes)
    needed_to_free = 30000000 - (70000000 - total_size)
    possible_dirs_to_free = [x for x in dir_sizes if x > needed_to_free]
    return (total_size, min(possible_dirs_to_free))


def main():
    lines = []
    with open("07.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
