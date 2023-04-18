# -*- coding: utf-8 -*-
"""
    Created on Tue Mar 21 23:24:42 2023

@author: Tushar_Dalvi
"""

def shoelace_formula(p1, p2, p3):
    return 0.5 * abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1]))

def print_triangles(points):
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                area = shoelace_formula(points[i], points[j], points[k])
                if area > 0:
                    print(points[i], points[j], points[k])


n = int(input("Enter the number of points: "))
points = []
for i in range(n):
    x, y = map(int, input(f"Enter the x and y coordinates of point {i+1}: ").split())
    points.append((x, y))
    

print("All possible triangles:")
print_triangles(points)

