# from helloworld import HelloWorld

# hw1 = HelloWorld('Alina')
# hw1.show()

from asciimatics.screen import Screen
from time import sleep
from block import Block

block = Block(2, '¤', 6, 6)

def demo(screen):
    screen.print_at(block.style, block.coord[0], block.coord[1], block.color, 1)
    screen.refresh()
    sleep(10)

Screen.wrapper(demo)
