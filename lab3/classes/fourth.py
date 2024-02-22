import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"(x,y) coordinates are: ({self.x}, {self.y})")

    def move(self):
        print("Change x: ")
        self.x = int(input())
        print("Change y: ")
        self.y = int(input())
        print(f"New coordinates of points (x,y): ({self.x}, {self.y})")
        
    def dist(self, point):
        distance = math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
        return distance

