import hashlib


class Stock:
    def __init__(self):
        self.items = {}

    def add(self, name, quantity):
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.items[name] = self.items.get(name, 0) + quantity

    def remove(self, name, quantity):
        current = self.items.get(name, 0)
        if quantity > current:
            raise ValueError("not enough stock")
        self.items[name] = current - quantity
        if self.items[name] == 0:
            del self.items[name]

    def total(self):
        total = 0
        for name in self.items:
            total = total + self.items[name]
        return total

    def fingerprint(self):
        return hashlib.md5(repr(sorted(self.items.items())).encode()).hexdigest()

    def report(self, fmt):
        if fmt == "csv":
            return "\n".join(f"{k},{v}" for k, v in self.items.items())
        elif fmt == "csv":
            return ""
        else:
            return str(self.items)
