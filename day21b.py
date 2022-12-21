import sympy


def operation(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b


def solve(lines):
    monkeys = {"humn": sympy.Symbol("x")}
    for a in lines:
        name, expr = a.split(": ")
        if name in monkeys:
            continue
        if expr.isdigit():
            monkeys[name] = sympy.Integer(expr)
        else:
            left, op, right = expr.split()
            if left in monkeys and right in monkeys:
                if name == "root":
                    print(sympy.solve(monkeys[left] - monkeys[right]))
                    break
                monkeys[name] = operation(monkeys[left], monkeys[right], op)
            else:
                lines.append(a)
    return monkeys["humn"]


def main():
    lines = []
    with open("21.txt") as f:
        for line in f.readlines():
            lines.append(line.strip())

    return solve(lines)


if __name__ == "__main__":
    print(main())
