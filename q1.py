# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:21:31 2023

@author: Tushar_Dalvi
"""

import math

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def circumcenter(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    s = (a + b + c) / 2
    r = (a * b * c) / (4 * math.sqrt(s * (s - a) * (s - b) * (s - c)))
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - y2 * x3
    B = (x1**2 + y1**2) * (y3 - y2) + (x2**2 + y2**2) * (y1 - y3) + (x3**2 + y3**2) * (y2 - y1)
    C = (x1**2 + y1**2) * (x2 - x3) + (x2**2 + y2**2) * (x3 - x1) + (x3**2 + y3**2) * (x1 - x2)
    x = -B / (2 * A)
    y = -C / (2 * A)
    return (x, y), r

l1 = [(1, 0), (2, -7), (8, 1), (9, -6)]
cc1, r1 = circumcenter(l1[0], l1[1], l1[2])
cc2, r2 = circumcenter(l1[0], l1[1], l1[3])
cc3, r3 = circumcenter(l1[0], l1[2], l1[3])
cc4, r4 = circumcenter(l1[1], l1[2], l1[3])
for point in l1:
    d1 = distance(point, cc1)
    d2 = distance(point, cc2)
    d3 = distance(point, cc3)
    d4 = distance(point, cc4)
    if d1 > r1 and d2 > r2 and d3 > r3 and d4 > r4:
        print("The four points are not on the same circle.")
        break
else:
    print("The four points are on the same circle.")
