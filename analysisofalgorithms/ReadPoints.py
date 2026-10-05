def read_points_from_csv(randomPoints="10"):
    # Read points from the CSV file
    csv_file_path = f"./points/{randomPoints}_random_points.csv"
    print(f"Reading points from {csv_file_path}")
    points = []
    with open(csv_file_path, 'r') as file:
        content = file.read()
        coordinate_pairs = content.split('),')
        for pair in coordinate_pairs:
            if pair == '':
                continue
            pair = pair.replace('(', '')
            x, y = pair.split(',')
            points.append((float(x), float(y)))

    return points
