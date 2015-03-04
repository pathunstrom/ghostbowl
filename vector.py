from math import cos, radians, sin, sqrt
from numbers import Number


class Vector2(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        t = type(other)
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, (list, tuple)) and len(other) == 2:
            return Vector2(self.x + other[0], self.y + other[1])
        elif isinstance(other, (dict, set)) and 'x' in other and 'y' in other and len(other) == 2:
            return Vector2(self.x + other['x'], self.y + other['y'])
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, (list, tuple)) and len(other) == 2:
            return Vector2(self.x - other[0], self.y - other[1])
        elif isinstance(other, dict) and 'x' in other and 'y' in other and len(other) == 2:
            return Vector2(self.x - other['x'], self.y - other['y'])
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, Number):
            return Vector2(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, Number):
            return Vector2(self.x * other, self.y * other)

    def __len__(self):
        return sqrt(self.x*self.x + self.y*self.y)

    @property
    def length(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def __getitem__(self, item):
        item_type = type(item)

        if item_type is str:
            if item == 'x':
                return self.x
            elif item == 'y':
                return self.y
            else:
                raise KeyError
        elif item_type is int:
            if item == 0:
                return self.x
            elif item == 1:
                return self.y
            else:
                raise IndexError
        else:
            raise TypeError

    def __repr__(self):
        return "Vector2({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if isinstance(other, Vector2):
            return self.x != other.x or self.y != other.y

    def rotate(self, degrees):
        r = radians(degrees)
        rcos = cos(r)
        rsin = sin(r)
        x = round(self.x * rcos - self.y * rsin, 5)
        y = round(self.x * rsin + self.y * rcos, 5)
        return Vector2(x, y)

    def normalize(self):
        length = self.length
        x = self.x / length
        y = self.y / length
        return Vector2(x, y)


if __name__ == "__main__":

    print("Testing module vector.")
    print("Instantiate and __repr__")
    vector = Vector2(1, 0)
    rep = repr(vector)
    assert rep == "Vector2(1, 0)"
    print(rep + " passed.")

    print("Test addition.")
    print("With Vector2")
    vector2 = Vector2(0, 1)
    vector3 = vector + vector2
    assert vector3.x == 1 and vector3.y == 1
    print("Success.")
    print("With list")
    vector2 = [1, 0]
    vector3 = vector + vector2
    assert vector3.x == 2 and vector3.y == 0
    print("Success")
    print("With tuple")
    vector2 = (2, 0)
    vector3 = vector + vector2
    assert vector3.x == 3 and vector3.y == 0
    print("Success")

    print("Test rotation")
    vector2 = vector.rotate(90)
    assert repr(vector2) == "Vector2(0.0, 1.0)"
    vector2 = vector2.rotate(-90)
    assert repr(vector2) == "Vector2(1.0, 0.0)"
    vector2 = vector.rotate(-90)
    assert repr(vector2) == 'Vector2(0.0, -1.0)'
    print("Success")

    print("Test multiplication")
    vector = Vector2(1, 0)
    vector2 = Vector2(1, 0)
    result = vector * vector2
    assert result == 1
    vector2 = Vector2(-1, 0)
    result = vector * vector2
    assert result == -1
    result = vector * 2
    assert result == Vector2(2, 0)