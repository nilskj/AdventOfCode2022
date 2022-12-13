def solve(lines):

    groups = []
    current_group = []
    for i in lines:
        stripped = i.strip()
        if stripped:
            current_group.append(stripped)
        else:
            groups.append(current_group)
            current_group = []
    groups.append(current_group)

    def compare(left, right):

        left_is_list = isinstance(left, list)
        right_is_list = isinstance(right, list)

        if left_is_list and right_is_list:
            for i, element in enumerate(left):
                if i == len(right):
                    return 1

                recursive_compare = compare(element, right[i])
                if recursive_compare != 0:
                    return recursive_compare

            if len(right) > len(left):
                return -1
            return 0

        elif left_is_list:
            return compare(left, [right])

        elif right_is_list:
            return compare([left], right)

        elif left < right:
            return -1

        elif left == right:
            return 0

        return 1

    groups.append(["[[2]]", "[[6]]"])

    all = [eval(item) for sublist in groups for item in sublist]

    import functools

    all.sort(key=functools.cmp_to_key(compare))

    key_one = [i + 1 for i, x in enumerate(all) if x == [[2]]][0]
    key_two = [i + 1 for i, x in enumerate(all) if x == [[6]]][0]
    return key_one * key_two


def main():
    lines = []
    with open("13.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
