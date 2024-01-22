class Vector:
    pass
class Vector:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, other):
        return Vector([a * b for a, b in zip(self.data, other.data)])

    def __matmul__(self, other):
        return sum(a * b for a, b in zip(self.data, other.data))

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __eq__(self, other):
        return self.data == other.data