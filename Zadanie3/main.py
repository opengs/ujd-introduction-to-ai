from typing import List


class Table():
    def __init__(self, n: int) -> None:
        self._n = n
        self._table = []
        for i in range(n):
            self._table.append([])
            for j in range(n):
                self._table[i].append(False)

    @property
    def all_visited(self) -> bool:
        for i in range(self._n):
            for j in range(self._n):
                if not self._table[i][j]:
                    return False
        return True

    def get(self, x: int, y: int) -> True:
        return self._table[x][y]

    def set(self, x: int, y: int, value: True):
        self._table[x][y] = value

jump_directions = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

def heuristic_score(table: Table, n: int, x: int, y: int) -> int:
    score = 0
    for jump in jump_directions:
        new_x = x + jump[0]
        new_y = y + jump[1]
        if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n: continue
        if table.get(new_x, new_y): continue
        score += 1
    return score

def jump_rec(table: Table, n: int, x: int, y: int):
    if x < 0 or y < 0 or x >= n or y >= n: return None
    if table.get(x, y): return None

    table.set(x, y, True)
    if table.all_visited: return [(x, y)]
    
    jumps_scored =  map(lambda jump: (heuristic_score(table, n, x+jump[0], y+jump[1]), jump), jump_directions)
    jumps_scored = sorted(jumps_scored, key=lambda jump: jump[0])
    jumps_scored = map(lambda jump_scored: jump_scored[1], jumps_scored)
    jumps_scored = list(jumps_scored)

    for jump in jumps_scored:
        result = jump_rec(table, n, x + jump[0], y + jump[1])
        if result:
            result.insert(0, (x, y))
            return result

    table.set(x, y, False)

def jump(n: int, x: int, y: int):
    table = Table(n)
    print(jump_rec(table, n, x, y))
    

jump(16, 0, 0)