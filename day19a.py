import re


def dfs(bp, maxspend, cache, time, bots, amount):
    if time == 0:
        return amount[3]

    key = tuple([time, *bots, *amount])
    if key in cache:
        return cache[key]

    maxval = amount[3] + bots[3] * time

    for bot_type, recipe in enumerate(bp):
        if bot_type != 3 and bots[bot_type] >= maxspend[bot_type]:
            continue

        wait = 0
        for res_amount, res_type in recipe:
            if bots[res_type] == 0:
                break
            # floor division hack
            wait = max(wait, -(-(res_amount - amount[res_type]) // bots[res_type]))
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            bots_ = bots[:]
            amount_ = [x + y * (wait + 1) for x, y in zip(amount, bots)]
            for res_amount, res_type in recipe:
                amount_[res_type] -= res_amount

            bots_[bot_type] += 1

            maxval = max(maxval, dfs(bp, maxspend, cache, remtime, bots_, amount_))

    cache[key] = maxval
    return maxval


def main():
    total = 0
    for i, line in enumerate(open("19.txt")):
        bp = []
        maxspend = [0, 0, 0]
        for section in line.split(": ")[1].split(". "):
            recipe = []
            for x, y in re.findall(r"(\d+) (\w+)", section):
                x = int(x)
                y = ["ore", "clay", "obsidian"].index(y)
                recipe.append((x, y))
                maxspend[y] = max(maxspend[y], x)
            bp.append(recipe)
        v = dfs(bp, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
        total += (i + 1) * v

    return total


if __name__ == "__main__":
    print(main())
