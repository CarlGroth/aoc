with open('input/06.txt', 'r') as f:
    txt = f.read()


def part1():
    for i in range(len(txt) - 4):
        if len(set(txt[i:i+4])) == 4:
            print(i + 4)
            break


def part2():
    for i in range(len(txt) - 14):
        if len(set(txt[i:i+14])) == 14:
            print(i + 14)
            break


part1()
part2()
