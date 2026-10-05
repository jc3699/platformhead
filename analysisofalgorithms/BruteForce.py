import math
import time
from ReadPoints import read_points_from_csv

def distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_points_brute_force(points):
    """Find the two closest points among a plane of points using brute force."""
    min_distance = float('inf')
    closest_pair = None, None
    
    # Compare every pair of points
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = points[i], points[j]
        
    return closest_pair

if __name__ == "__main__":
    count = 0
    for j in range(0, 10):  # Loop through file numbers from 1 to 10
        count += 5
        filename = str(count) + "k"
        points = read_points_from_csv(filename)
        print("Processing file:", filename)
        # Total time for average
        total_avg_time = 0

        for i in range(10):
            start = time.time()
            closest_pair_result = closest_points_brute_force(points)
            end = time.time()
            total_avg_time += end - start
            # print(".", end=" ")
            print("Total milliseconds: ", (end-start) * 1000)

        total_avg_time = (total_avg_time/10) * 1000
        print("\nClosest pair:", closest_pair_result)
        print("Total average time milliseconds: ", total_avg_time)