
class Set:

    def __init__(self):
        self.set = []

    def size(self):
        return len(self.set)

    def add(self, num):
        self.set.append(num)

    def isMember(self, num):
        for i in range(len(self.set)):
            if num == self.set[i]:
                return True
        return False

    def isEmpty(self):
        if len(self.set) == 0:
            return True
        return False

    def union(self, other):
        for i in range(len(other.set)):
            self.set.append(other.set[i])

        other.set.clear()
