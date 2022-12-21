class Node:
    def __init__(self, text):
        name, *props = text.strip().split(": ")
        self.name = name

        if props[0].strip().isdigit():
            self.leaf = True
            self.value = int(props[0])
        else:
            self.leaf = False
            values = props[0].split(" ")
            self.left_name, self.op, self.right_name = values

    def evaluate(self)
        if self.leaf:
            return self.value
        return eval(f"{self.left.evaluate()} {self.op} {self.right.evaluate()}")

def solve(lines):
    nodes = [Node(line) for line in lines]
    nodes = {n.name: n for n in nodes}

    for node in nodes.values():
        if not node.leaf:
            node.left = nodes[node.left_name]
            node.right = nodes[node.right_name]

    return nodes["root"].evaluate()


def main():
    lines = []
    with open("21.txt") as f:
        for line in f.readlines():
            lines.append(line)

    return solve(lines)


if __name__ == "__main__":
    print(main())
