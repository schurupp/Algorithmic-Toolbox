from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def strip_closest(strip, min_distance):
    strip_size = len(strip)
    for i in range(strip_size):
        j = i + 1
        while j < strip_size and (strip[j].y - strip[i].y) ** 2 < min_distance:
            min_distance = min(min_distance, distance_squared(strip[i], strip[j]))
            j += 1
    return min_distance


def closest_pair_distance(points_x, points_y):
    n = len(points_x)

    if n <= 3:
        return min(distance_squared(points_x[i], points_x[j]) for i, j in combinations(range(n), 2))

    mid = n // 2
    mid_point = points_x[mid]

    left_x = points_x[:mid]
    right_x = points_x[mid:]

    left_y = [point for point in points_y if point.x <= mid_point.x]
    right_y = [point for point in points_y if point.x > mid_point.x]

    left_distance = closest_pair_distance(left_x, left_y)
    right_distance = closest_pair_distance(right_x, right_y)

    min_distance = min(left_distance, right_distance)

    strip = [point for point in points_y if abs(point.x - mid_point.x) < sqrt(min_distance)]

    return min(min_distance, strip_closest(strip, min_distance))


def minimum_distance(points):
    sorted_points_x = sorted(points, key=lambda point: point.x)
    sorted_points_y = sorted(points, key=lambda point: point.y)

    return sqrt(closest_pair_distance(sorted_points_x, sorted_points_y))


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(minimum_distance(input_points)))
