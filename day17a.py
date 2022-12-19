from enum import Enum


class Rock(Enum):
    BAR = {0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j}
    PLUS = {1 + 2j, 1 + 1j, 1 + 0j, 0 + 1j, 2 + 1j}
    ANGLE = {2 + 2j, 2 + 1j, 0, 1, 2}
    COLUMN = {0, 0 + 1j, 0 + 2j, 0 + 3j}
    SQUARE = {0 + 1j, 1 + 1j, 0, 1}

    def __init__(self, blocks):
        self.blocks = blocks
        self.position = 0 + 0j

    @property
    def positions(self):
        return {block + self.position for block in self.blocks}

    def move(self, delta: complex) -> None:
        self.position += delta

    def jump(self, position: complex) -> None:
        self.position = position


class TetrisChamber:
    def __init__(self, width, winds) -> None:
        self.width = width
        self.winds = winds

        self.filled = set()
        self.columns = [-1 for _ in range(width)]
        self.base_height = 0
        self.top = -1
        self.rock = Rock.BAR
        self.move_index = 0
        self.rock_gen = self.rock_generator()

    def __str__(self) -> str:
        return (
            "".join(
                "|"
                + "".join(
                    "#" if x + y * 1j in self.filled else "." for x in range(self.width)
                )
                + "|\n"
                for y in range(self.top, -1, -1)
            )
            + "+"
            + "-" * self.width
            + "+"
        )

    def rock_generator(self):
        from itertools import cycle

        return cycle(Rock)

    def add_rock(self, rock: Rock):
        positions = rock.positions
        self.filled |= positions

        for col, height in ((int(p.real), int(p.imag)) for p in positions):
            self.columns[col] = max(self.columns[col], height)
            self.top = max(self.top, height)

    def trim(self):
        if (height := min(self.columns)) > 0:
            self.filled = {p - height * 1j for p in self.filled if p.imag >= height}
            self.base_height += height
            self.top -= height
            self.columns = [c - height for c in self.columns]

    def height(self) -> int:
        return self.base_height + self.top + 1

    def simulate_fall(self):
        rock = next(self.rock_gen)
        rock.jump(2 + (self.top + 4) * 1j)
        positions = rock.positions
        move = 0 + 0j

        while True:
            wind_dir = -1 if self.winds[self.move_index] == "<" else 1
            self.move_index = (self.move_index + 1) % len(self.winds)
            next_positions = {p + wind_dir for p in positions}
            if all(
                p.real >= 0 and p.real < self.width and p not in self.filled
                for p in next_positions
            ):
                move += wind_dir
                positions = next_positions

            next_positions = {p - 1j for p in positions}
            if any(p.imag < 0 or p in self.filled for p in next_positions):
                break

            move = move - 1j
            positions = next_positions

        rock.move(move)
        self.add_rock(rock)
        self.trim()
        print(self)


def solve(winds):

    chamber = TetrisChamber(7, winds)
    for _ in range(2022):
        chamber.simulate_fall()
    return chamber.height()


def main():
    winds = ""
    with open("17.txt") as f:
        winds = f.read().rstrip()

    return solve(winds)


if __name__ == "__main__":
    print(main())
