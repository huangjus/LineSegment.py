# Author: Justin Huang
# GitHub username: huangjus
# Date: 3/7/23
# Description: The Point class has an init method to initialize the x and y coordinates of a Point object.
# It also has get methods for the x and y coordinates, and a distance_to method to calculate the distance between
# two points using the distance formula.

# The LineSegment class has an init method to initialize the two endpoints (which are Point objects)
# of a LineSegment object. It also has get methods for the endpoints, a length method to calculate the length of
# the line segment using the distance_to method of the Point class, a slope method to calculate the slope of the
# line segment using the slope formula, and an is_parallel_to method to check if this line segment is parallel
# to another line segment by comparing their slopes.

class Point:
    """Class representing a point in 2D space"""

    def __init__(self, x_coord, y_coord):
        """Initialize a Point object with x and y coordinates"""
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """Get the x-coordinate of the point"""
        return self._x_coord

    def get_y_coord(self):
        """Get the y-coordinate of the point"""
        return self._y_coord

    def distance_to(self, other_point):
        """Calculate the distance between this point and another point"""
        x1 = self._x_coord
        y1 = self._y_coord
        x2 = other_point._x_coord
        y2 = other_point._y_coord
        distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return distance

   class LineSegment:
        """Class representing a line segment between two points"""

        def __init__(self, endpoint_1, endpoint_2):
            """Initialize a LineSegment object with two endpoints"""
            self._endpoint_1 = endpoint_1
            self._endpoint_2 = endpoint_2

        def get_endpoint_1(self):
            """Get the first endpoint of the line segment"""
            return self._endpoint_1

        def get_endpoint_2(self):
            """Get the second endpoint of the line segment"""
            return self._endpoint_2

        def length(self):
            """Calculate the length of the line segment"""
            endpoint_1 = self._endpoint_1
            endpoint_2 = self._endpoint_2
            length = endpoint_1.distance_to(endpoint_2)
            return length

        def slope(self):
            """Calculate the slope of the line segment"""
            x1 = self._endpoint_1.get_x_coord()
            y1 = self._endpoint_1.get_y_coord()
            x2 = self._endpoint_2.get_x_coord()
            y2 = self._endpoint_2.get_y_coord()
            slope = (y2 - y1) / (x2 - x1)
            return slope

        def is_parallel_to(self, other_line_segment):
            """Check if this line segment is parallel to another line segment"""
            slope1 = self.slope()
            slope2 = other_line_segment.slope()
            if abs(slope1 - slope2) < 1e-7:
                return True
            else:
                return False
