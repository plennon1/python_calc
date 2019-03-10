class Counter():
    count = 0
    def inc(self):
        self.count += 1
        return self.count

    def dec(self):
        self.count -= 1
        return self.count