import re


def dfs(bp, maxspend, cache, time, bots, amount):
    if time == 0:
        return amount[3]

    key = tuple([time, *bots, *amount])
    if key in cache:
        return cache[key]

    maxval = amount[3] + bots[3] * time

    for bot_type, recipe in enumerate(bp):
        # Optimize: do we already have enough of this bot?
        if bot_type != 3 and bots[bot_type] >= maxspend[bot_type]:
            continue

        # How long do we have to wait untill we have enough resources to build this bot
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

            print("wait", wait, "bots", bots_, "amt", amount_)

            # Optimize: throw away excessive resources
            for i in range(3):
                amount_[i] = min(amount_[i], maxspend[i] * remtime)
            maxval = max(maxval, dfs(bp, maxspend, cache, remtime, bots_, amount_))

    cache[key] = maxval
    return maxval


def main():
    total = 1
    for i, line in enumerate(list(open("19.txt"))[:3]):
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
        v = dfs(bp, maxspend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
        total *= v

    return total


if __name__ == "__main__":
    print(main())
