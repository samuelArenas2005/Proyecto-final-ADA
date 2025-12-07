from dataclasses import dataclass

@dataclass
class SportsMan:
    id = int
    name = str
    age = int
    performance = int

class Team():
    def __init__(self, name, rbTree, average_performance):
        self.name = name
        self.rbTree = rbTree
        self.average_performance = average_performance


