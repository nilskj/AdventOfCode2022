def solve(lines):
    read_stacks = []

    def columns(matrix):
        return [[line[x] for line in matrix] for x in range(len(matrix[0]))]

    commands = []
    commands_start = False
    for line in lines:
        if not line.strip():
            commands_start = True
            continue
        if not commands_start:
            read_stacks.append(line)
        else:
            commands.append(line)

    cols = columns(read_stacks)
    crate_columns = []
    for col in cols:
        if col[-1].strip():
            trimmed = [x for x in col if x.strip()]
            trimmed.reverse()
            trimmed.pop(0)
            crate_columns.append(trimmed)

    for command in commands:
        parts = command.split()
        num = int(parts[1])
        src = int(parts[3])
        dest = int(parts[5])
        for i in range(num):
            crate_columns[dest - 1].append(crate_columns[src - 1].pop())

    letters = [x[-1] for x in crate_columns]
    return "".join(letters)


def main():
    lines = []
    with open("05.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
