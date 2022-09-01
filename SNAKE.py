from random import randint


def draw(field):
    print("\n"*10)
    snakeTextureIndex = 0
    for y in range(len(field)):
        print(" ")  # Separator
        for x in range(len(field[y])):
            if field[y][x] > 0:  # Snake skin Draw
                snakeTextureIndex += 1
                snakeTextureIndex = 0 if snakeTextureIndex > len(
                    snakeTexture)-1 else snakeTextureIndex
                if y == snakePos[1] and x == snakePos[0]:
                    print("▣", end=' ')
                else:
                    print((snakeTexture[snakeTextureIndex]
                           ), end=" ")
            elif field[y][x] == 0:  # Empty Space
                print("·", end=" ")
            else:
                print("@", end=" ")


def moveSnake(field, snakePos):
    x = snakePos[0]
    y = snakePos[1]

    btn = input("wasd: ")
    if btn == "w":
        y -= 1
    elif btn == 's':
        y += 1
    elif btn == 'a':
        x -= 1
    elif btn == 'd':
        x += 1

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
        for x in range(len(field)):
            if field[y][x] == 0:
                fieldZeros.append([x, y])
    rNum = randint(0, len(fieldZeros)-1)
    field[fieldZeros[rNum][1]][fieldZeros[rNum][0]] = -1
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
snakePos = [4, 4]
snakePosHistory = [[0, 0]]
snakeLen = 1
snakeTexture = ['$', '%', '#']
# snakeTexture = #['◧', '◩', '◨', '◪']  #  ['e', 's', 'n', 'a', 'k']

field = spawnApple(field)
while True:
    draw(field)
    field = clearSnakeTail(field, snakePosHistory, snakeLen)
    snakePos = moveSnake(field, snakePos)

    if field[snakePos[1]][snakePos[0]] == 0:
        snakeLen += 1
        field = spawnApple(field)
        field[snakePos[1]][snakePos[0]] = 1

    if snakeLen == 100:
        print("Victory")
        break

    if field[snakePos[1]][snakePos[0]] > 1:
        print("Game Over!")
        break
