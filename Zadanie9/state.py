from enum import Enum
from typing import List

class BoatLocation(int, Enum):
    LEFT = 0
    RIGHT = 1

class State():
    def __init__(self, canibals_left: int, canibals_right: int, missioner_left: int, missioner_right: int, boat: BoatLocation) -> None:
        self.canibals_left = canibals_left
        self.canibals_right = canibals_right
        self.missioner_left = missioner_left
        self.missioner_right = missioner_right
        self.boat = boat
    
    @property
    def is_solution(self) -> bool:
        return self.missioner_left == 0 and self.canibals_left == 0

    @property
    def is_valid(self) -> bool:
        return (self.missioner_left == 0 or (self.missioner_left >= self.canibals_left)) and (self.missioner_right == 0 or (self.missioner_right >= self.canibals_right))

    @property
    def next_states(self) -> List:
        result = []
        if self.boat == BoatLocation.LEFT:
            if self.canibals_left > 0 and self.missioner_left > 0:
                result.append(State(self.canibals_left - 1, self.canibals_right + 1, self.missioner_left - 1, self.missioner_right + 1, BoatLocation.RIGHT))
            if self.canibals_left > 0:
                result.append(State(self.canibals_left - 1, self.canibals_right + 1, self.missioner_left, self.missioner_right, BoatLocation.RIGHT))
            if self.missioner_left > 0:
                result.append(State(self.canibals_left, self.canibals_right, self.missioner_left - 1, self.missioner_right + 1, BoatLocation.RIGHT))
            if self.canibals_left >= 2:
                result.append(State(self.canibals_left - 2, self.canibals_right + 2, self.missioner_left, self.missioner_right, BoatLocation.RIGHT))
            if self.missioner_left >= 2:
                result.append(State(self.canibals_left, self.canibals_right, self.missioner_left - 2, self.missioner_right + 2, BoatLocation.RIGHT))
        else:
            if self.canibals_right > 0 and self.missioner_right > 0:
                result.append(State(self.canibals_left + 1, self.canibals_right - 1, self.missioner_left + 1, self.missioner_right - 1, BoatLocation.LEFT))
            if self.canibals_right > 0:
                result.append(State(self.canibals_left + 1, self.canibals_right - 1, self.missioner_left, self.missioner_right, BoatLocation.LEFT))
            if self.missioner_right > 0:
                result.append(State(self.canibals_left, self.canibals_right, self.missioner_left + 1, self.missioner_right - 1, BoatLocation.LEFT))
            if self.canibals_right >= 2:
                result.append(State(self.canibals_left + 2, self.canibals_right - 2, self.missioner_left, self.missioner_right, BoatLocation.LEFT))
            if self.missioner_right >= 2:
                result.append(State(self.canibals_left, self.canibals_right, self.missioner_left + 2, self.missioner_right - 2, BoatLocation.LEFT))
        return result

    def __eq__(self, other):
        return (self.canibals_left == other.canibals_left and
                self.canibals_right == other.canibals_right and
                self.missioner_left == other.missioner_left and
                self.missioner_right == other.missioner_right and
                self.boat == other.boat)

    def __ne__(self, o: object) -> bool:
        return not (self == o)

    def __hash__(self) -> int:
        return self.canibals_left + self.canibals_right*10 + self.missioner_left*100 + self.missioner_right*1000 + self.boat.value * 10000

    def __str__(self) -> str:
        return f"[{self.canibals_left}:{self.canibals_right}] [{self.missioner_left}:{self.missioner_right}] [{self.boat}]"

    def __repr__(self) -> str:
        return self.__str__()