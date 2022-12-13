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

        a_is_list = isinstance(left, list)
        b_is_list = isinstance(right, list)

        if a_is_list and b_is_list:
            for i, element in enumerate(left):
                if i == len(right):
                    return 1

                recursive_compare = compare(element, right[i])
                if recursive_compare != 0:
                    return recursive_compare

            if len(right) > len(left):
                return -1
            return 0

        elif a_is_list:
            return compare(left, [right])

        elif b_is_list:
            return compare([left], right)

        elif left < right:
            return -1

        elif left == right:
            return 0

        return 1

    pair_order_sum = 0
    for i, group in enumerate(groups):
        if compare(eval(group[0]), eval(group[1])) == -1:
            pair_order_sum += i + 1
    return pair_order_sum


def main():
    lines = []
    with open("13.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
