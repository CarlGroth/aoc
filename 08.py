with open('input/08.txt', 'r') as f:
    txt = f.read().splitlines()


def scenic(trees, height):
    for i, tree in enumerate(trees, 1):
        if tree >= height:
            return i
    return len(trees)


def part1():
    visible = 0
    for i, row in enumerate(txt):
        for j, height in enumerate(row):
            right = all(txt[i][col] < height for col in range(j+1, len(row)))
            left = all(txt[i][col] < height for col in range(0, j))
            down = all(txt[r][j] < height for r in range(i+1, len(row)))
            up = all(txt[r][j] < height for r in range(0, i))
            edge = len(set([i, j]) & set([0, len(row) - 1])) != 0
            visible += any([right, left, up, down, edge])
    print(visible)


def part2():
    scene = 0
    for i, row in enumerate(txt):
        for j, height in enumerate(row):
            edge = len(set([i, j]) & set([0, len(row) - 1])) != 0
            if edge:
                continue
            right = scenic([txt[i][col]
                           for col in range(j+1, len(row))], height)
            left = scenic(list(reversed([txt[i][col]
                          for col in range(0, j)])), height)
            down = scenic([txt[r][j] for r in range(i+1, len(row))], height)
            up = scenic(list(reversed([txt[r][j]
                        for r in range(0, i)])), height)
            scene = max(scene, right * left * down * up)
    print(scene)


part1()
part2()
