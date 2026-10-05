import sys
import random

floor = 1
ceiling = 10000

def generate_random_points(n):
    points = ''
    listOfPoints = []
    
    for i in range(n):
        # Random numbers should be in a range of 1 - 1000
        x = round(random.uniform(floor, ceiling), 2)
        y = round(random.uniform(floor, ceiling), 2)

        # To avoid duplicate points
        while listOfPoints and (x, y) in points:
            x = round(random.uniform(floor, ceiling), 2)
            y = round(random.uniform(floor, ceiling), 2)
        # Append the points
        points += '(' + str(x) + ',' + str(y) + '),'
        #points.append((x, y))

    return points

# Main
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the number of points to generate as an argument.")
        sys.exit(1)
    num_points = int(sys.argv[1])
    listOfPoints = generate_random_points(num_points)

    print(listOfPoints);
