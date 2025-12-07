#Implementa la clase Deportista
from dataclasses import dataclass


@dataclass
class SportsMan:
    id: int
    name: str
    age: int
    performance: int