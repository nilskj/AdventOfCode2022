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
    tiny_dirs = [x for x in dir_sizes if x < 100000]
    return (total_size, sum(tiny_dirs))


def main():
    lines = []
    with open("07.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
