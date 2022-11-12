from random import randint

class Input():
    def getInp(self):

        inputdict = {"s":[1, 0], "w":[-1, 0], "a":[0, -1], "d":[0, 1]}
        curInput = input(" w/a/s/d/enter: ")
        try:
            out = inputdict[curInput]
            self._history.append(curInput)
        except:
            out = inputdict[self._history[-1]]
            self._history.append(self._history[-1])
        return out

class Snake(Input):
    def __init__(self):
        self._pos = [[3, 3], [3, 3], [3, 3]]
        self._len = 2
        self._history = ["w","w"]
        self.applePos = [4, 5]

    def spawnApple(self):
        freeSpace = []
        for y in range(10):
            for x in range(10):
                if [y, x] not in self._pos:
                    freeSpace.append([y, x])
        self.applePos = freeSpace[randint(0, len(freeSpace))]

    def move(self):
        for i in range (len(self._pos) - self._len):
            del self._pos[0]
            del self._history[0]

        curInp = self.getInp()
        self._pos.append([self._pos[-1][0]+curInp[0], self._pos[-1][1]+curInp[1]])
        if self._pos[-1][0] >= 10 or self._pos[-1][0] < 0:
            return False
        if self._pos[-1][1] >= 10 or self._pos[-1][1] < 0:
            return False
        if self._pos[-1] in self._pos[0: -2]:
            return False
        if self._pos[-1] == self.applePos:
            self._len += 1
            self.spawnApple()
        return True
    
    def draw(self):
        for y in range(10):
            print(" ")
            for x in range(10):
                if [y, x] == self.applePos:
                    print('\033[91m' + "@", end=" ")
                elif [y, x] not in self._pos:
                    print('\033[0m' + "`", end=" ")
                else:
                    if [y, x] == self._pos[-1]:
                        print('\033[91m' + "#", end=" ")
                    else: 
                        print('\033[92m' + "%", end=" ")

snk = Snake()
snk.spawnApple()
while snk.move() is True:
    snk.draw()