from functools import reduce

with open('input/03.txt', 'r') as f:
    arr = f.read().split('\n')


def priority(letter):
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38


def part1():
    print(sum(priority(
        (set(line[len(line)//2:]) & set(line[:len(line)//2])).pop()) for line in arr))


def part2():
    tot = 0
    for i in range(0, len(arr), 3):
        intersections = reduce(set.intersection, arr[i:i+3], set(arr[i]))
        tot += priority(intersections.pop())
    print(tot)


part1()
part2()
