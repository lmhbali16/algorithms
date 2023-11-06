from collections import deque
##Phase 1
def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    if not lab:
        return

    num_rows = len(lab)
    num_columns = max(len(row) for row in lab)

    print("   ", end="")
    for col in range(num_columns):
        print(col % 10, end="")
    print()

    for row, line in enumerate(lab):
        if path and row < len(path):
            for element in path:
                if element[0] == row:
                    line = replace_at_index(line, "X", element[1])

        print(f"{row % 10}  {line}  {row % 10}")

    print("   ", end="")
    for col in range(num_columns):
        print(col % 10, end="")
    print()
## Phase 2
def prompt_integer(message: str) -> int:
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid integer.")

def prompt_user_for_location(name: str) -> tuple[int, int]:
    print(f"For {name}:")
    row = prompt_integer("Row: ")
    column = prompt_integer("Column: ")
    return row, column

## Phase 3
def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque()
    visited = set()
    queue.append([start])

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        path = queue.popleft()
        last = path[-1]

        if last == end:
            return path

        if last not in visited:
            visited.add(last)

            for move in moves:
                next_location = (last[0] + move[0], last[1] + move[1])

                if is_traversable(lab, next_location):
                    new_path = list(path)
                    new_path.append(next_location)
                    queue.append(new_path)
def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    row, col = location
    if 0 <= row < len(lab) and 0 <= col < len(lab[row]):
        return lab[row][col] == " "
    return False

def replace_at_index(s: str, r: str, idx: int) -> str:
    return s[:idx] + r + s[idx + len(r):]

labyrinth = [
    "#######",
    "#     #",
    "#   ###",
    "# ### #",
    "#     #",
    "#######",
]

print_labyrinth(labyrinth)
start_location = prompt_user_for_location("start")
end_location = prompt_user_for_location("end")
path = bfs(labyrinth, start_location, end_location)
print(path)
print_labyrinth(labyrinth, path)