from random import randint
import os


def draw(field, snakePos, snakeTexture):
    for y in range(len(field)):
        print(" ")  # Separator
        for x in range(len(field[y])):

            if field[y][x] > 0:  # Snake skin Draw
                if y == snakePos[1] and x == snakePos[0]:
                    print("▣", end=' ')
                else:
                    print("#", end=" ")

            elif field[y][x] == 0:  # Empty Space
                print("·", end=" ")
            else:
                print("O", end=" ")


def moveSnake(field, snakePos, btn):
    x = snakePos[0]
    y = snakePos[1]
    del btn[0]

    btn.append(input("wasd: "))
    if btn[-1] == '':
        btn[-1] = btn[-2]

    if btn[-1][0:1] == "w":
        y -= 1
    elif btn[-1][0:1] == 's':
        y += 1
    elif btn[-1][0:1] == 'a':
        x -= 1
    elif btn[-1][0:1] == 'd':
        x += 1

    x = 0 if x > 9 else x
    x = 9 if x < 0 else x
    y = 0 if y >= 9 else y
    y = 8 if y < 0 else y

    field[y][x] += 1
    snakePosHistory.append([y, x])

    snakePos = [x, y]
    return snakePos


def clearSnakeTail(field, snakePosHistory, snakeLen):
    for _ in range(len(snakePosHistory) - snakeLen):
        field[snakePosHistory[0][0]][snakePosHistory[0][1]] = 0
        del snakePosHistory[0]
    return field


def spawnApple(field):
    fieldZeros = []
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 0:
                fieldZeros.append([x, y])
    rNum = randint(0, len(fieldZeros)-1)
    field[fieldZeros[rNum][1]][fieldZeros[rNum][0]] = -2
    return field


field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
]


field[3][3] = 0
btn = ['w', 'w']
snakePos = [4, 4]
snakePosHistory = [[4, 4], [4, 4]]
snakeLen = 1
snakeTexture = ['◁', '▷', '△', '▽']


field = spawnApple(field)
while snakeLen < 100:

    os.system('clear')
    draw(field, snakePos, snakeTexture)
    field = clearSnakeTail(field, snakePosHistory, snakeLen)
    snakePos = moveSnake(field, snakePos, btn)

    if field[snakePos[1]][snakePos[0]] <= 0:
        snakeLen += 1
        field = spawnApple(field)
        field[snakePos[1]][snakePos[0]] = 1

    if snakeLen == 100:
        print("Victory")

    if field[snakePos[1]][snakePos[0]] > 1:
        print("Game Over!")
        break
