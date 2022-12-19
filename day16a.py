import re


def solve(graph, flows):
    def find(graph, flows, start):
        frontier = [(0, [start], set())]
        for i in range(1, 31):
            if i > 5:
                frontier.sort(reverse=True)
                frontier = frontier[:3000]
            new_frontier = []
            for pressure, path, opened in frontier:
                location = path[-1]

                p = sum(flows[o] for o in opened)
                pressure += p

                for neigh in graph[location]:
                    new_frontier.append((pressure, path + [neigh], opened.copy()))

                if flows[location] > 0 and location not in opened:
                    new_frontier.append((pressure, path, opened | {location}))
            frontier = new_frontier
        return max(frontier)

    pressure, path, opened = find(graph, flows, "AA")
    return f"{pressure} {len(path) - 1} {opened}"


def main():
    with open("16.txt") as f:
        input = re.findall(r"Valve (\w\w).*?rate=(\d+).*?valves? (.*)", f.read())
        flows = dict((start, int(rate)) for start, rate, _ in input)
        graph = dict(
            (start, nabes.replace(" ", "").split(",")) for start, _, nabes in input
        )

        return solve(graph, flows)


if __name__ == "__main__":
    print(main())
