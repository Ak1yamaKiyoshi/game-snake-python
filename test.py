from time import sleep

class Obj:
    def __init__(self):
        self.vector = 0 # deg
        self.speed = 1
        self.pos = [10, 10]

    def draw(self):
        print( "\n" + "_"*10)
        sleep(0.2)
        for y in range(20):
            print(" ")
            for x in range(30):
                if ([y, x] == self.pos):
                    print("#", end=" ")
                else:
                    print("`", end=" ")
    def move(self):
        p = self.pos
        v = self.vector
        mv = {270:[pv], 90}


obj = Obj()

while (True):
    obj.draw()
