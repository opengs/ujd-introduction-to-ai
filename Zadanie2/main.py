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
def jump_rec(table: Table, n: int, x: int, y: int):
    if x < 0 or y < 0 or x >= n or y >= n: return None
    if table.get(x, y): return None

    table.set(x, y, True)
    if table.all_visited: return [(x, y)]
    
    for jump in jump_directions:
        result = jump_rec(table, n, x + jump[0], y + jump[1])
        if result:
            result.insert(0, (x, y))
            return result

    table.set(x, y, False)

def jump(n: int, x: int, y: int):
    table = Table(n)
    print(jump_rec(table, n, x, y))
    

jump(8, 0, 0)