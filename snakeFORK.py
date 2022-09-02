from random import randint
import os


def draw(field, snakePos, snakeTexture):
    for y in range(len(field)):
        print(" ")  # Separator
        for x in range(len(field[y])):
            if 16 > field[y][x] > 0:  # Snake skin Draw
                if y == snakePos[1] and x == snakePos[0]:
                    print("●", end=' ')
                else:
                    # left = 11 right = 12 up = 13 down = 14 len gained = 15
                    if field[y][x] == 11:
                        print(snakeTexture[0], end=' ')
                    elif field[y][x] == 12:
                        print(snakeTexture[1], end=' ')
                    elif field[y][x] == 13:
                        print(snakeTexture[2], end=' ')
                    elif field[y][x] == 14:
                        print(snakeTexture[3], end=' ')
                    elif field[y][x] == 15:
                        print(snakeTexture[4], end=' ')
            
            elif field[y][x] == 0:  # Empty Space
                print("⠀", end=" ")
            elif field[y][x] == 255:
                print("🞒", end=" ")
            else:
                print("◯", end=" ")


def moveSnake(field, snakePos, btn):
    for _ in range(len(btn) - snakeLen):
        del btn[0] 

    x = snakePos[0]
    y = snakePos[1]
    
    btn.append(input(" w,a,s,d or enter: "))
    if btn[-1] == '':
        btn[-1] = btn[-2]

    # left = 11 right = 12 up = 13 down = 14 len gained = 15
    if btn[-1][0:1] == 'a':
        x -= 1
        field[y][x] += 11
    elif btn[-1][0:1] == 'd':
        x += 1
        field[y][x] += 12
    elif btn[-1][0:1] == "w":
        y -= 1
        field[y][x] += 13
    elif btn[-1][0:1] == 's':
        y += 1
        field[y][x] += 14

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
    field[fieldZeros[rNum][1]][fieldZeros[rNum][0]] = -16 # if lower apple will not spawn
    return field


field = [
    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, ],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 255, ],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 255, ],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 255, ],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 255, ],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 255, ],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 255, ],
    [255, 0, 0, 0, 0, 0, 0, 0, 0, 255, ],
    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, ],
]


field[3][3] = 0 # starting position
btn = ['w', 'w', 'w'] # needed for last direction move
snakePos = [4, 4]  
snakePosHistory = [[4, 4], [4, 4]] # needed for tail remove
snakeLen = 1
snakeTexture = ['🠴', '🠶', '🠵', '🠷', '#']


field = spawnApple(field)
while snakeLen <= 56:

    os.system('clear')
    draw(field, snakePos, snakeTexture)
    field = clearSnakeTail(field, snakePosHistory, snakeLen)
    print(f'\n Your Score: {snakeLen}/56 ')
    snakePos = moveSnake(field, snakePos, btn)

    if field[snakePos[1]][snakePos[0]] <= 0:
        snakeLen += 1
        field = spawnApple(field)
        field[snakePos[1]][snakePos[0]] = 15

    if snakeLen == 56:
        print("Victory")

    if field[snakePos[1]][snakePos[0]] > 15:
        print("Game Over!")
        break
