import sys
from termcolor import *
import time

#print('\u001b[31mHello World!')
#print('\u001b[0m')
p = '+'

def b(n):
    return ' ' * n

def red(text, n):
    return '\u001b[31m{}'.format(text) * n

def black(text, n):
    return '\u001b[30m{}'.format(text) * n

def green(text, n):
    return '\u001b[32m{}'.format(text) * n

def yellow(text, n):
    return '\u001b[33m{}'.format(text) * n

def blue(text, n):
    return '\u001b[34m{}'.format(text) * n

def magenta(text, n):
    return '\u001b[35m{}'.format(text) * n

def cyan(text, n):
    return '\u001b[36m{}'.format(text) * n

def white(text, n):
    return '\u001b[37m{}'.format(text) * n

def orange(text, n):
    return '\u001b[38;5;9m{}'.format(text) * n

def purple(text, n):
    return '\u001b[38;5;88m{}'.format(text) * n

def gray(text, n):
    return '\u001b[38;5;8m{}'.format(text) * n

def byelow(text, n):
    return '\u001b[38;5;226m{}'.format(text) * n

def violet(text, n):
    return '\u001b[38;5;93m{}'.format(text) * n

def resetti():
    print('\u001b[0m')

def palette():
    print(red('a', 1))
    print(black('a', 1))
    print(green('a', 1))
    print(yellow('a', 1))
    print(blue('a', 1))
    print(cyan('a', 1))
    print(magenta('a', 1))
    print(white('a', 1))
    print(orange('a', 1))
    print(purple('a', 1))
    print(gray('a', 1))
    print(byelow('a', 1))
    print(violet('a', 1))

def frame1():
    print(b(23) + black(p, 17) + b(8))
    print(b(3) + red(p, 6) + b(6) + red(p, 7) + black(p, 1) + yellow(p, 17) + black(p, 1) + b(7))
    print(red(p, 21) + black(p, 1) + yellow(p, 3) + magenta(p, 13) + yellow(p, 3) + black(p, 1) + b(6))
    print(red(p, 21) + black(p, 1) + yellow(p, 2) + magenta(p, 15) + yellow(p, 2) + black(p, 1) + b(6))
    print(red(p, 3) + orange(p, 6) + red(p, 6) + orange(p, 6) + black(p, 1) + yellow(p, 1) + magenta(p, 2) + purple(p, 1) + magenta(p, 14) + yellow(p, 1) + black(p, 1) + b(6))
    print(orange(p, 21) + black(p, 1) + yellow(p, 1) + magenta(p, 10) + black(p, 2) + magenta(p, 2) + purple(p, 1) + magenta(p, 2) + yellow(p, 1) + black(p, 1) + b(1) + black(p, 2) + b(3))
    print(orange(p, 21) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 2) + black(p, 1) + magenta(p, 4) + yellow(p, 1) + black(p, 2) + gray(p, 2) + black(p, 1) + b(2))
    print(orange(p, 3) + byelow(p, 6) + orange(p, 6) + black(p, 4) + byelow(p, 2) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 3) + black(p, 1) + magenta(p, 3) + yellow(p, 1) + black(p, 1) + gray(p, 3) + black(p, 1) + b(2))
    print(byelow(p, 15) + black(p, 1) + gray(p, 2) + black(p, 2) + byelow(p, 1) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 4) + black(p, 4) + gray(p, 4) + black(p, 1) + b(2))
    print(byelow(p, 15) + black(p, 2) + gray(p, 2) + black(p, 3) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 12) + black(p, 1) + b(2))
    print(byelow(p, 3) + green(p, 6) + byelow(p, 6) + green(p, 1) + black(p, 2) + gray(p, 2) + black(p, 2) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 14) + black(p, 1) + b(1))
    print(green(p, 17) + black(p, 2) + gray(p, 2) + black(p, 1) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 3) + white(p, 1) + black(p, 1) + gray(p, 5) + white(p, 1) + black(p, 1) + gray(p, 2) + black(p, 1) + b(1))
    print(green(p, 18) + black(p, 4) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 3) + black(p, 2) + gray(p, 3) + black(p, 1) + gray(p, 1) + black(p, 2) + gray(p, 2) + black(p, 1) + b(1))
    print(green(p, 3) + blue(p, 6) + green(p, 6) + blue(p, 5) + black(p, 2) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 1) + purple(p, 2) + gray(p, 9) + purple(p, 2) + black(p, 1) + b(1))
    print(blue(p, 21) + black(p, 1) + yellow(p, 2) + magenta(p, 7) + black(p, 1) + gray(p, 1) + purple(p, 2) + gray(p, 1) + black(p, 1) + gray(p, 2) + black(p, 1) + gray(p, 2) + black(p, 1) + gray(p, 1) + purple(p, 2) + black(p, 1) + b(1))
    print(blue(p, 21) + black(p, 1) + yellow(p, 3) + magenta(p, 7) + black(p, 1) + gray(p, 3) + black(p, 7) + gray(p, 2) + black(p, 1) + b(2))
    print(blue(p, 3) + violet(p, 6) + blue(p, 6) + violet(p, 5) + black(p, 3) + yellow(p, 10) + black(p, 1) + gray(p, 10) + black(p, 1) + b(3))
    print(violet(p, 19) + black(p, 1) + gray(p, 3) + black(p, 21) + b(4))
    print(violet(p, 19) + black(p, 1) + gray(p, 2) + black(p, 2) + b(1) + black(p, 1) + gray(p, 2) + b(5) + black(p, 1) + gray(p, 2) + black(p, 1) + b(1) + black(p, 1) + gray(p, 2) + black(p, 1) + b(5))
    print(violet(p, 3) + b(6) + violet(p, 6) + b(4) + black(p, 4) + b(2) + black(p, 3) + b(7) + black(p, 3) + b(2) + black(p, 2) + b(6))

def frame2():
    print(b(23) + black(p, 17) + b(8))
    print(b(3) + red(p, 6) + b(6) + red(p, 7) + black(p, 1) + yellow(p, 17) + black(p, 1) + b(7))
    print(red(p, 21) + black(p, 1) + yellow(p, 3) + magenta(p, 13) + yellow(p, 3) + black(p, 1) + b(6))
    print(red(p, 21) + black(p, 1) + yellow(p, 2) + magenta(p, 15) + yellow(p, 2) + black(p, 1) + b(6))
    print(red(p, 3) + orange(p, 6) + red(p, 6) + orange(p, 6) + black(p, 1) + yellow(p, 1) + magenta(p, 2) + purple(p, 1) + magenta(p, 14) + yellow(p, 1) + black(p, 1) + b(6))
    print(orange(p, 21) + black(p, 1) + yellow(p, 1) + magenta(p, 10) + black(p, 2) + magenta(p, 2) + purple(p, 1) + magenta(p, 2) + yellow(p, 1) + black(p, 1) + b(1) + black(p, 2) + b(3))
    print(orange(p, 21) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 2) + black(p, 1) + magenta(p, 4) + yellow(p, 1) + black(p, 2) + gray(p, 2) + black(p, 1) + b(2))
    print(orange(p, 3) + byelow(p, 6) + orange(p, 4) + black(p, 4) + byelow(p, 4) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 3) + black(p, 1) + magenta(p, 3) + yellow(p, 1) + black(p, 1) + gray(p, 3) + black(p, 1) + b(2))
    print(byelow(p, 13) + black(p, 1) + gray(p, 2) + black(p, 2) + byelow(p, 3) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 4) + black(p, 4) + gray(p, 4) + black(p, 1) + b(2))
    print(byelow(p, 13) + black(p, 2) + gray(p, 2) + black(p, 2) + byelow(p, 2) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 12) + black(p, 1) + b(2))
    print(byelow(p, 3) + green(p, 6) + byelow(p, 5) + black(p, 2) + gray(p, 2) + black(p, 2) + green(p, 1) + black(p, 1) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 14) + black(p, 1) + b(1))
    print(green(p, 15) + black(p, 2) + gray(p, 2) + black(p, 3) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 3) + white(p, 1) + black(p, 1) + gray(p, 5) + white(p, 1) + black(p, 1) + gray(p, 2) + black(p, 1) + b(1))
    print(green(p, 16) + black(p, 6) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 3) + black(p, 2) + gray(p, 3) + black(p, 1) + gray(p, 1) + black(p, 2) + gray(p, 2) + black(p, 1) + b(1))
    print(green(p, 3) + blue(p, 6) + green(p, 6) + blue(p, 3) + black(p, 4) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 1) + purple(p, 2) + gray(p, 9) + purple(p, 2) + black(p, 1) + b(1))
    print(blue(p, 21) + black(p, 1) + yellow(p, 2) + magenta(p, 7) + black(p, 1) + gray(p, 1) + purple(p, 2) + gray(p, 1) + black(p, 1) + gray(p, 2) + black(p, 1) + gray(p, 2) + black(p, 1) + gray(p, 1) + purple(p, 2) + black(p, 1) + b(1))
    print(blue(p, 21) + black(p, 1) + yellow(p, 3) + magenta(p, 7) + black(p, 1) + gray(p, 3) + black(p, 7) + gray(p, 2) + black(p, 1) + b(2))
    print(blue(p, 3) + violet(p, 6) + blue(p, 6) + violet(p, 5) + black(p, 3) + yellow(p, 10) + black(p, 1) + gray(p, 10) + black(p, 1) + b(3))
    print(violet(p, 19) + black(p, 1) + gray(p, 3) + black(p, 21) + b(4))
    print(violet(p, 18) + black(p, 1) + gray(p, 2) + black(p, 2) + b(1) + black(p, 1) + gray(p, 2) + b(7) + black(p, 1) + gray(p, 2) + black(p, 1) + b(1) + black(p, 1) + gray(p, 2) + black(p, 1) + b(4))
    print(violet(p, 3) + b(6) + violet(p, 6) + b(4) + black(p, 4) + b(2) + black(p, 3) + b(7) + black(p, 3) + b(2) + black(p, 2) + b(6))

def frame3():
    print(b(23) + black(p, 17) + b(8))
    print(red(p, 3) + b(6) + red(p, 6) + b(7) + black(p, 1) + yellow(p, 17) + black(p, 1) + b(7))
    print(red(p, 21) + black(p, 1) + yellow(p, 3) + magenta(p, 13) + yellow(p, 3) + black(p, 1) + b(6))
    print(red(p, 21) + black(p, 1) + yellow(p, 2) + magenta(p, 15) + yellow(p, 2) + black(p, 1) + b(6))
    print(orange(p, 3) + red(p, 6) + orange(p, 6) + red(p, 6) + black(p, 1) + yellow(p, 1) + magenta(p, 2) + purple(p, 1) + magenta(p, 14) + yellow(p, 1) + black(p, 1) + b(6))
    print(orange(p, 21) + black(p, 1) + yellow(p, 1) + magenta(p, 10) + black(p, 2) + magenta(p, 2) + purple(p, 1) + magenta(p, 2) + yellow(p, 1) + black(p, 1) + b(1) + black(p, 2) + b(3))
    print(orange(p, 21) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 2) + black(p, 1) + magenta(p, 4) + yellow(p, 1) + black(p, 2) + gray(p, 2) + black(p, 1) + b(2))
    print(byelow(p, 3) + orange(p, 6) + byelow(p, 4) + black(p, 4) + orange(p, 4) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 3) + black(p, 1) + magenta(p, 3) + yellow(p, 1) + black(p, 1) + gray(p, 3) + black(p, 1) + b(2))
    print(byelow(p, 13) + black(p, 1) + gray(p, 2) + black(p, 2) + byelow(p, 3) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 4) + black(p, 4) + gray(p, 4) + black(p, 1) + b(2))
    print(byelow(p, 13) + black(p, 2) + gray(p, 2) + black(p, 2) + byelow(p, 2) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 12) + black(p, 1) + b(2))
    print(green(p, 3) + byelow(p, 6) + green(p, 5) + black(p, 2) + gray(p, 2) + black(p, 2) + yellow(p, 1) + black(p, 1) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 14) + black(p, 1) + b(1))
    print(green(p, 15) + black(p, 2) + gray(p, 2) + black(p, 3) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 3) + white(p, 1) + black(p, 1) + gray(p, 5) + white(p, 1) + black(p, 1) + gray(p, 2) + black(p, 1) + b(1))
    print(green(p, 16) + black(p, 6) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 3) + black(p, 2) + gray(p, 3) + black(p, 1) + gray(p, 1) + black(p, 2) + gray(p, 2) + black(p, 1) + b(1))
    print(blue(p, 3) + green(p, 6) + blue(p, 6) + green(p, 3) + black(p, 4) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 1) + purple(p, 2) + gray(p, 9) + purple(p, 2) + black(p, 1) + b(1))
    print(blue(p, 21) + black(p, 1) + yellow(p, 2) + magenta(p, 7) + black(p, 1) + gray(p, 1) + purple(p, 2) + gray(p, 1) + black(p, 1) + gray(p, 2) + black(p, 1) + gray(p, 2) + black(p, 1) + gray(p, 1) + purple(p, 2) + black(p, 1) + b(1))
    print(blue(p, 21) + black(p, 1) + yellow(p, 3) + magenta(p, 7) + black(p, 1) + gray(p, 3) + black(p, 7) + gray(p, 2) + black(p, 1) + b(2))
    print(violet(p, 3) + blue(p, 6) + violet(p, 6) + blue(p, 5) + black(p, 3) + yellow(p, 10) + black(p, 1) + gray(p, 10) + black(p, 1) + b(3))
    print(violet(p, 19) + black(p, 1) + gray(p, 3) + black(p, 21) + b(4))
    print(violet(p, 18) + black(p, 1) + gray(p, 2) + black(p, 2) + b(1) + black(p, 1) + gray(p, 2) + b(7) + black(p, 1) + gray(p, 2) + black(p, 1) + b(1) + black(p, 1) + gray(p, 2) + black(p, 1) + b(4))
    print(b(3) + violet(p, 6) + b(6) + violet(p, 4) + black(p, 4) + b(2) + black(p, 3) + b(7) + black(p, 3) + b(2) + black(p, 2) + b(6))


def frame4():
    print(b(23) + black(p, 17) + b(8))
    print(red(p, 3) + b(6) + red(p, 6) + b(6) + red(p, 1) + black(p, 1) + yellow(p, 17) + black(p, 1) + b(7))
    print(red(p, 21) + black(p, 1) + yellow(p, 3) + magenta(p, 13) + yellow(p, 3) + black(p, 1) + b(6))
    print(red(p, 21) + black(p, 1) + yellow(p, 2) + magenta(p, 15) + yellow(p, 2) + black(p, 1) + b(6))
    print(orange(p, 3) + red(p, 6) + orange(p, 6) + red(p, 6) + black(p, 1) + yellow(p, 1) + magenta(p, 2) + purple(p, 1) + magenta(p, 14) + yellow(p, 1) + black(p, 1) + b(6))
    print(orange(p, 21) + black(p, 1) + yellow(p, 1) + magenta(p, 10) + black(p, 2) + magenta(p, 2) + purple(p, 1) + magenta(p, 2) + yellow(p, 1) + black(p, 1) + b(1) + black(p, 2) + b(3))
    print(orange(p, 21) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 2) + black(p, 1) + magenta(p, 4) + yellow(p, 1) + black(p, 2) + gray(p, 2) + black(p, 1) + b(2))
    print(byelow(p, 3) + orange(p, 6) + byelow(p, 6) + black(p, 4) + orange(p, 2) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 3) + black(p, 1) + magenta(p, 3) + yellow(p, 1) + black(p, 1) + gray(p, 3) + black(p, 1) + b(2))
    print(byelow(p, 15) + black(p, 1) + gray(p, 2) + black(p, 2) + byelow(p, 1) + black(p, 1) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 4) + black(p, 4) + gray(p, 4) + black(p, 1) + b(2))
    print(byelow(p, 15) + black(p, 2) + gray(p, 2) + black(p, 3) + yellow(p, 1) + magenta(p, 9) + black(p, 1) + gray(p, 12) + black(p, 1) + b(2))
    print(green(p, 3) + byelow(p, 6) + green(p, 6) + byelow(p, 1) + black(p, 2) + gray(p, 2) + black(p, 2) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 14) + black(p, 1) + b(1))
    print(green(p, 17) + black(p, 2) + gray(p, 2) + black(p, 1) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 3) + white(p, 1) + black(p, 1) + gray(p, 5) + white(p, 1) + black(p, 1) + gray(p, 2) + black(p, 1) + b(1))
    print(green(p, 18) + black(p, 4) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 3) + black(p, 2) + gray(p, 3) + black(p, 1) + gray(p, 1) + black(p, 2) + gray(p, 2) + black(p, 1) + b(1))
    print(blue(p, 3) + green(p, 6) + blue(p, 6) + green(p, 5) + black(p, 2) + yellow(p, 1) + magenta(p, 8) + black(p, 1) + gray(p, 1) + purple(p, 2) + gray(p, 9) + purple(p, 2) + black(p, 1) + b(1))
    print(blue(p, 21) + black(p, 1) + yellow(p, 2) + magenta(p, 7) + black(p, 1) + gray(p, 1) + purple(p, 2) + gray(p, 1) + black(p, 1) + gray(p, 2) + black(p, 1) + gray(p, 2) + black(p, 1) + gray(p, 1) + purple(p, 2) + black(p, 1) + b(1))
    print(blue(p, 21) + black(p, 1) + yellow(p, 3) + magenta(p, 7) + black(p, 1) + gray(p, 3) + black(p, 7) + gray(p, 2) + black(p, 1) + b(2))
    print(violet(p, 3) + blue(p, 6) + violet(p, 6) + blue(p, 5) + black(p, 3) + yellow(p, 10) + black(p, 1) + gray(p, 10) + black(p, 1) + b(3))
    print(violet(p, 19) + black(p, 1) + gray(p, 3) + black(p, 21) + b(4))
    print(violet(p, 19) + black(p, 1) + gray(p, 2) + black(p, 2) + b(1) + black(p, 1) + gray(p, 2) + b(5) + black(p, 1) + gray(p, 2) + black(p, 1) + b(1) + black(p, 1) + gray(p, 2) + black(p, 1) + b(5))
    print(b(3) + violet(p, 6) + b(6) + violet(p, 4) + black(p, 4) + b(2) + black(p, 3) + b(7) + black(p, 3) + b(2) + black(p, 2) + b(6))

def runAnimation():
    frame1()
    time.sleep(0.25)
    frame2()
    time.sleep(0.25)
    frame3()
    time.sleep(0.25)
    frame4()
    time.sleep(0.25)

#palette()

while True:
    runAnimation()

#runAnimation()

#frame2()
#frame3()

resetti()
