# from __future__ import annotations


class Resources:

    def __init__(self, lumber=0, clay=0, iron=0, crop=0):
        self.lumber = lumber
        self.clay = clay
        self.iron = iron
        self.crop = crop

    def as_list(self):
        return [self.lumber, self.clay, self.iron, self.crop]

    def is_enough_for(self, other):
        for owned, required in zip(self.as_list(), other.as_list()):
            if owned < required:
                return False
        return True

    def lowest(self):
        lowest_value = min(self.as_list())
        return self.as_list().index(lowest_value) + 1

    def __repr__(self):
        return f'Resources - Lumber: {self.lumber}, Clay: {self.clay}, Iron: {self.iron}, Crop: {self.crop}'
