from collections import deque
import math


def solve(blizzards, bounds):
    queue = deque([(0, -1, 0)])
    seen = set()

    r, c = bounds
    target = (r, c - 1)

    # Optimization: Blizzard state will repeat every lcm steps so we can skip checking all states
    lcm = r * c // math.gcd(r, c)

    possible_move_deltas = ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0))

    while queue:
        time, current_row, current_column = queue.popleft()
        time += 1

        for move_row, move_column in possible_move_deltas:
            next_row = current_row + move_row
            next_column = current_column + move_column

            if (next_row, next_column) == target:
                print("Target time:", time)
                exit(0)

            # Check within bounds?
            if not (0 <= next_row < r and 0 <= next_column < c) and not (
                (
                    next_row,
                    next_column,
                )
                == (-1, 0)
            ):
                continue

            # Check if next step fails? shift player position instead of all blizzards
            fail = False
            if (next_row, next_column) != (-1, 0):
                for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                    target_step = (
                        (next_row - tr * time) % r,
                        (next_column - tc * time) % c,
                    )
                    # print(target_step)
                    if target_step in blizzards[i]:
                        fail = True
                        break

            # Step into next iteration
            if not fail:
                key = (next_row, next_column, time % lcm)

                if key in seen:
                    continue

                seen.add(key)
                queue.append((time, next_row, next_column))


def main():
    blizzards = tuple(set() for _ in range(4))
    bounds = [0, 0]
    with open("24.txt") as f:
        for r, line in enumerate(f.read().splitlines()[1:]):
            bounds[0] = r
            for c, item in enumerate(line[1:]):
                bounds[1] = c
                if item in "<>^v":
                    kind = "<>^v".find(item)
                    blizzards[kind].add((r, c))

    return solve(blizzards, bounds)


if __name__ == "__main__":
    print(main())
