import math
import time
from ReadPoints import read_points_from_csv

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_in_strip(strip, delta):
    min_distance = delta
    closest_pair = None
    strip.sort(key=lambda x: x[1])
    for i in range(len(strip)):
        for j in range(i+1, min(i+16, len(strip))):
            distance = euclidean_distance(strip[i], strip[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (strip[i], strip[j])
    return closest_pair


def find_closest_distance(points):
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    return closest_pair

def closest_pair_rec(Px, Py):
    # Base case
    if len(Px) <= 3:
        return find_closest_distance(Px)
    
    mid = len(Px) // 2
    
    # Left side
    Qx = Px[:mid]

    # Right side
    Rx = Px[mid:]
    
    midpoint = Px[mid][0]
    Qy = []
    Ry = []
    for point in Py:
        if point[0] < midpoint:
            Qy.append(point)
        else:
            Ry.append(point)
    
    (q0, q1) = closest_pair_rec(Qx, Qy)
    (r0, r1) = closest_pair_rec(Rx, Ry)
    
    delta = min(euclidean_distance(q0, q1), euclidean_distance(r0, r1))
    
    x_star = Px[mid][0]
    strip = [point for point in Py if abs(point[0] - x_star) < delta]
    strip_value = closest_pair_in_strip(strip, delta)
    
    if strip_value is None:
        if euclidean_distance(q0, q1) < euclidean_distance(r0, r1):
            return (q0, q1)
        else:
            return (r0, r1)
    else:
        return closest_pair_in_strip(strip, delta)

def closest_pair(P):
    P.sort(key=lambda x: x[0])
    Px = P[:]
    Py = P[:]
    return closest_pair_rec(Px, Py)


if __name__ == "__main__":
    count = 0
    # Divide And Conquer algorithm
    for j in range(0, 10):  # Loop through file numbers from 1 to 10
        # Increment count by 5
        count += 5
        filename = str(count) + "k"
        print(filename)
        points = read_points_from_csv(filename)
        print("Processing file:", filename)
        # Total time for average
        total_avg_time = 0

        for i in range(10):
            start = time.time()
            closest_pair_result = closest_pair(points)
            end = time.time()
            total_avg_time += end - start
            print(".", end=" ")
        total_avg_time = (total_avg_time / 10) * 1000  
        print("\nClosest pair:", closest_pair_result)
        print("Total average time milliseconds: ", total_avg_time)

