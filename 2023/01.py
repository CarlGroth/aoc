import re

with open('input/01.txt', 'r') as f:
    arr = f.read().split('\n')


def part1():
    numeric = [''.join(c for c in line if c.isnumeric()) for line in arr]

    calibration = sum(int(n[0] + n[-1]) for n in numeric)
    print(calibration)


def part2():
    s = 0
    for line in arr:
        for i, k in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], 1):
            line = line.replace(k, f'{k[0]}{i}{k[1:]}')
        nums = ''.join(c for c in line if c.isnumeric())
        s += int(nums[0] + nums[-1]) 
    
    print(s)


part1()
part2()
