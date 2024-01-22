from typing import Tuple


db = set()


def almacenar_orden(orden: Tuple[str, ...]) -> bool:
    pass

class DB:
    def __init__(self):
        self.orders = set()

    def add(self, order):
        if order in self.orders:
            return False
        self.orders.add(order)
        return True

db = DB()

def almacenar_orden(order):
    return db.add(order)