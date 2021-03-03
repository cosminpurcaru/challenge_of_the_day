"""
Given a list of points represented as Points(x,y), find the maximum number of rectangles 
that can be formed using these points.

Note:
Rectangles are formed only so that their sides are parallel against Ox & Oy.

Example:

    Input:

  y ^
    |
   3+            *
    |            
   2+    *   *          *
    |                 
   1+    *   *   *      *
----|----+---+---+------+-----> x
  O |    1   2   3      5

    Output: 3
    
    Rectangle #1: Point(x=1,y=1), Point(x=1,y=2), Point(x=2,y=1), Point(x=2,y=2)
    Rectangle #2: Point(x=2,y=1), Point(x=2,y=2), Point(x=5,y=1), Point(x=5,y=2)
    Rectangle #3: Point(x=1,y=1), Point(x=1,y=2), Point(x=5,y=1), Point(x=5,y=2)
    
"""

from challenge_of_the_day.lib.point import Point


def get_num_of_rectangles(points: list):
    """
    Get maximum number of rectangles that can be formed from a list of points represented as Points(x,y).
    ..info: Rectangles are formed only so that their sides are parallel against Ox & Oy
    
    :param points: List of Points represented as Point(x, y)
    :return: Highest number of rectangles whose sides are parallel with Ox & Oy
    """
    verticals = {}

    for point in points:
        for point_above in points:
            if (point.x == point_above.x) and (point.y < point_above.y):
                vertical = (point.y, point_above.y)
                if vertical in verticals:
                    verticals[vertical] += 1
                else:
                    verticals[vertical] = 1

    print(f'Verticals: {verticals}')
    rectangles = [int((vertical*(vertical-1)/2)) for vertical in list(verticals.values())]
    return sum(rectangles)
  
