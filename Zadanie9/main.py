from state import State, BoatLocation

def find_rec(states: set, current_state: State):
    if current_state.is_solution: return []

    for state in current_state.next_states:
        if state not in states and state.is_valid:
            states.add(state)
            solution = find_rec(states, state)
            if solution != None:
                solution.append(state)
                return solution

    return None

def find(states: set, current_state: State):
    solution = find_rec(states, current_state)
    if solution:
        solution.append(current_state)
        solution.reverse()
    return solution

def main():
    start_state = State(3, 0, 3, 0, BoatLocation.LEFT)
    states = set([start_state])
    solution = find(states, start_state)
    if solution:
        print(f"Solution founded in {len(solution)} iterations")
        print(solution)
    else:
        print("There is no solution")

if __name__ == "__main__":
    main()