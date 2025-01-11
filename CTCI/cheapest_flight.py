import sys

class Node:
    edges: list
    city: int

    def __init__(self, city):
        self.city = city
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

class Edge:
    src: Node
    dest: Node
    price: int

    def __init__(self, price: int, src: Node, dest: Node) -> None:
        self.src = src
        self.dest = dest
        self.price = price

class Solution:

    def generate_graph(self, flights: list) -> dict:
        graph_map: dict[Node] = {}

        for flight in flights:
            src: Node
            dest: Node

            if flight[0] not in graph_map.keys():
                src = Node(flight[0])
                graph_map[flight[0]] = src
            else:
                src = graph_map[flight[0]]

            if flight[1] not in graph_map.keys():
                dest = Node(flight[1])
                graph_map[flight[1]] = dest
            else:
                dest = graph_map[flight[1]]

            edge = Edge(flight[2], src, dest)
            src.add_edge(edge)

        return graph_map

    def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, k: int) -> int:
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph_map = self.generate_graph(flights)

        if src not in graph_map:
            return -1

        if dst not in graph_map:
            return -1
        
        src_node = graph_map[src]
        print(src_node.edges)

        cheapest = sys.maxsize
        visiting_edges = [[edge, 0] for edge in src_node.edges]

        while visiting_edges:
            edge, stop = visiting_edges.pop()
            if edge.price >= cheapest:
                continue
            
            if dst == edge.dest.city:
                cheapest = edge.price
            elif stop < k and edge.dest.city in graph_map.keys():
                for e in edge.dest.edges:
                    if edge.price+e.price < cheapest:
                        e.price += edge.price
                        visiting_edges.append([e, stop + 1])

        if cheapest != sys.maxsize:
            return cheapest
        else:
            return -1


sol = Solution()
print(sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))







