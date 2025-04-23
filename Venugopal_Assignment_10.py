#Tuples — Coordinate Distance Calculator
import math

points = [(0, 0), (3, 4), (7, 1)]

dist = []

for i in range(len(points)-1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]

    # Euclidean distance formula
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    dist.append(distance)

    print(f"Distance between {points[i]} and {points[i + 1]}: {distance:.1f}")


total = sum(dist)
print(f"Total distance: {total:.1f}")