# from __future__ import annotations


class Resources:

    def __init__(self, resources: list):
        self.lumber = int(resources[0])
        self.clay = int(resources[1])
        self.iron = int(resources[2])
        self.crop = int(resources[3])

    def as_list(self):
        return [self.lumber, self.clay, self.iron, self.crop]

    def is_enough_for(self, other):
        for owned, required in zip(self.as_list(), other.as_list()):
            if owned < required:
                return False
        return True
