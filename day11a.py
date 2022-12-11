def find_int(string):
    return int("".join([c for c in string if c.isdigit()]))


def solve(lines):
    monkeys = []
    monkey = []

    # read monkeys as line groups
    for line in lines:
        if line.strip():
            monkey.append(line.strip())
        else:
            monkeys.append(monkey)
            monkey = []
    monkeys.append(monkey)

    def monkey_business(monkey_lines):
        items = [int(item) for item in monkey_lines[1].split(":")[1].split(",")]

        operation = monkey_lines[2].split(":")[1].strip()
        operand = operation.split(" ")[3]
        operand_target = operation.split(" ")[-1]
        test_division = find_int(monkey_lines[3].split(":")[1].strip())
        a = find_int(monkey_lines[4].split(":")[1].strip())
        b = find_int(monkey_lines[5].split(":")[1].strip())

        inspections = 0

        def round(all_monkeys):
            current_items = get_items()[0]
            add_inspections(len(current_items))
            for item in current_items:
                # run operation
                op = run_operation(item)
                # floor divide by 3
                op = op // 3
                # dispatch to a or b depending on condition
                if op % test_division == 0:
                    all_monkeys[a]["add"](op)
                else:
                    all_monkeys[b]["add"](op)
            items.clear()

        def add_inspections(n):
            nonlocal inspections
            inspections += n

        def get_items():
            return (items, inspections)

        def add_item(item):
            items.append(item)

        def run_operation(item):
            if operand == "*":
                return item * (
                    int(operand_target) if operand_target.isdigit() else item
                )
            if operand == "+":
                return item + (
                    int(operand_target) if operand_target.isdigit() else item
                )
            return item

        return {
            "round": round,
            "add": add_item,
            "get": get_items,
        }

    # create monkeys
    monkeys = [monkey_business(monkey) for monkey in monkeys]
    for i in range(20):
        for monkey in monkeys:
            monkey["round"](monkeys)

    monkey_inspection_counts = [monkey["get"]()[1] for monkey in monkeys]
    print("Inspections:", monkey_inspection_counts)

    inspections_sorted = sorted(monkey_inspection_counts, reverse=True)
    return inspections_sorted[0] * inspections_sorted[1]


def main():
    lines = []
    with open("11.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
