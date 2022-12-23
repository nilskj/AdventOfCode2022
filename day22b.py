
def solve(lines):
    pass

def main():
    lines = []
    with open('22.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return solve(lines)

if __name__ == '__main__':
    print(main())
