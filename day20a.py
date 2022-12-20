class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None


def solve(lines):
    # Create a linked list of nodes
    nodes = [Node(n) for n in lines]
    for i in range(len(nodes)):
        nodes[i].left = nodes[(i - 1) % len(nodes)]
        nodes[i].right = nodes[(i + 1) % len(nodes)]

    max_node = len(nodes) - 1
    for i in nodes:
        if i.n == 0:
            z = i
            continue
        target = i

        # Iterating step right
        if i.n > 0:
            for _ in range(i.n % max_node):
                target = target.right
            if i == target:
                continue
            i.right.left = i.left
            i.left.right = i.right
            target.right.left = i
            i.right = target.right
            target.right = i
            i.left = target
        # Iterating step left
        else:
            for _ in range(-i.n % max_node):
                target = target.left
            if i == target:
                continue
            i.left.right = i.right
            i.right.left = i.left
            target.left.right = i
            i.left = target.left
            target.left = i
            i.right = target

    total = 0
    for _ in range(3):
        for _ in range(1000):
            z = z.right
        total += z.n
    return total


def main():
    lines = []
    with open("20.txt") as f:
        for line in f.readlines():
            lines.append(int(line))

    return solve(lines)


if __name__ == "__main__":
    print(main())
