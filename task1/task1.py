# -*- coding: utf-8 -*-


n, m = map(int, input().split())
i = m
path = '1'
while (i % n) != 1:
    if i % n == 0:
        path = path + str(n)
    else:
        path = path + str(i % n)
    i = i + m - 1
print(path)