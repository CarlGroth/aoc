with open('input.txt', 'r') as f:
    arr = f.read().split('\n\n')


def part1():
    calories = [sum(int(x) for x in lines.split('\n')) for lines in arr]
    fattest = max(calories)
    print(fattest)


def part2():
    calories = [sum(int(x) for x in lines.split('\n')) for lines in arr]
    fattest = sum(sorted(calories, reverse=True)[:3])
    print(fattest)


part1()
part2()
