from collections import Counter


class DetectSquares:
    def __init__(self):
        self.points = Counter()

    def add(self, point):
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point):
        x, y = point
        total_squares = 0

        # Check all points with same x-coordinate as current point
        for (px, py), count in self.points.items():
            # Skip if not vertically aligned (can't be on same vertical line)
            if px != x or py == y:
                continue

            # Distance between y-coordinates gives square side length
            d = abs(py - y)

            # Check the 2 possible horizontal positions to form a square
            for dx in [d, -d]:
                total_squares += (
                    self.points.get((x + dx, y), 0)
                    * self.points.get((x + dx, py), 0)
                    * count
                )

        return total_squares
