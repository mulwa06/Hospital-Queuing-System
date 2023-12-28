class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, item, priority):
        entry = (item, priority)
        self.queue.insert(self._find_insert_index(priority), entry)
        print(self.queue)
        return "added successfuly"

    def min(self):
        return self.queue[-1][1]

    def remove_min(self):
        item, priority = self.queue.pop()
        return item

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def _find_insert_index(self, priority):
        for i, (_,p) in enumerate(self.queue):
            if priority < p:
                return i
        return len(self.queue)

    def remove_by_priority(self, priority):
        for i, (item, p) in enumerate(self.queue):
            if p == priority:
                del self.queue[i]
                return item
        return None 

class Patient:
    def __init__(self, name, age, priority, weight, blood_pressure, gender):
        self.name = name
        self.age = age
        self.priority = priority
        self.weight = weight
        self.gender = gender
        self.blood_pressure = blood_pressure

pq = PriorityQueue()

#new code