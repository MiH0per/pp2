
class MyShape:
    def __init__(self, color="DefaultColor", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def getArea(self):
        return 0

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

class Rectangle(MyShape):
    def __init__(self, color="DefaultColor", is_filled=True, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle - {super().__str__()}, Top Left: ({self.x_top_left}, {self.y_top_left}), Length: {self.length}, Width: {self.width}, Area: {self.getArea()}"
