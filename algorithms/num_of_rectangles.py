class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_num_of_rectangles(points: list):
    verticals = {}
    for point in points:
        for point_above in points:
            if (point.x == point_above.x) and (point.y < point_above.y):
                y_diff = point_above.y - point.y
                if (y_diff) in verticals:
                    verticals[y_diff] += 1
                else:
                    verticals[y_diff] = 1

    print(f'Verticals: {verticals}')
    rectangles = [int((vertical*(vertical-1)/2)) for vertical in list(verticals.values())]
    return sum(rectangles)
  
