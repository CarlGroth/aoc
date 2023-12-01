with open('input/10.txt', 'r') as f:
    txt = f.read().splitlines()

def get_history():
    aux = 1
    history = []
    for line in txt:
        match line.split():
            case ['noop']:
                history.append(aux)
            case ['addx', value]:
                history.append(aux)
                history.append(aux)
                aux += int(value)
    return history

def part1():
    history = get_history()
    print(sum(i * x for i, x in enumerate(history, start=1) if (i + 20) % 40 == 0))

def part2():
    history = get_history()
    image = ['#' if abs(sprite - position % 40) < 2 else '.' for position, sprite in enumerate(history)]
    print('\n'.join(''.join(image[i:i+40]) for i in range(0, 6*40, 40)))

part1()
part2()