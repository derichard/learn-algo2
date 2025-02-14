import random


def heuristic(next, dest):
    return abs(next.x - dest.x) + abs(next.y - dest.y)


def a_star_search(traffic_grid, src, dest):
    q = PriorityQueue()
    q.push(0, src)
    predecessors = {}
    predecessors[src] = None
    costs = {}
    costs[src] = 0
    visited = set()

    while not q.empty():
        next = q.pop()
        
        if next == dest:
            break

        if next in visited:
            continue

        visited.add(next)

        neighbors = traffic_grid.neighbors(next)
        for neighbor in neighbors:
            total_cost = costs[next] + neighbor.cost()
            if neighbor not in costs or total_cost < costs[neighbor]:
                costs[neighbor] = total_cost
                priority = total_cost + heuristic(neighbor, dest)
                q.push(priority, neighbor)
                predecessors[neighbor] = next

    path = []
    pred = dest
    while pred is not None:
        path.append(pred)
        pred = predecessors[pred]

    path.reverse()
    return path

    # don't touch below this line


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None
        min = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min][0]:
                min = i
        item = self.elements[min]
        del self.elements[min]
        return item[1]


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        random.seed(hash(self))
        bucket = random.randint(1, 2)
        cost = random.randint(1, 5)
        if bucket == 2:
            cost = random.randint(15, 20)
        return cost

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) is tuple:
            return self.x == other[0] and self.y == other[1]
        else:
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class TrafficGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def in_bounds(self, tile):
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def neighbors(self, tile):
        neighbors = [
            Tile(tile.x + 1, tile.y),
            Tile(tile.x - 1, tile.y),
            Tile(tile.x, tile.y - 1),
            Tile(tile.x, tile.y + 1),
        ]
        results = filter(self.in_bounds, neighbors)
        return results

    def __repr__(self):
        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                t = Tile(x, y)
                s += f"[{t.cost():02d}]"
            s += "\n"
        return s
