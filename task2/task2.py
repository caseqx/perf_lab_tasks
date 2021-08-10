# -*- coding: utf-8 -*-


def point_position(x0, y0, r, x1, y1):
    if ((x1 - x0) ** 2 + (y1 - y0) ** 2 == r ** 2 ):
        print('0')
    if ((x1 - x0) ** 2 + (y1 - y0) ** 2 < r ** 2 ):
        print('1')
    if ((x1 - x0) ** 2 + (y1 - y0) ** 2 > r ** 2 ):
        print('2')

file1 = open(input(), "r")

x0, y0 = map(float, file1.readline().split())
r = float(file1.readline())

file1.close

file2 = open(input(), "r")

lines = file2.readlines()

for line in lines:
    x1, y1 = map(float, line.strip().split())
    point_position(x0, y0, r, x1, y1)

file2.close