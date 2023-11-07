from tree import DirectedNode

def route_between_nodes(node1, node2):
	list_nodes = [node1]

	while len(list_nodes) > 0:
		node = list_nodes[0]
		if node.visited:
			list_nodes = list_nodes[1:]
			continue

		if node == node2:
			return True

		node.markVisited()
		list_nodes = list_nodes[1:]
		list_nodes += node.adjacentNodes

	return False

node1 = DirectedNode(1)
node2 = DirectedNode(2)
node3 = DirectedNode(3)
node4 = DirectedNode(4)
node5 = DirectedNode(5)
node6 = DirectedNode(6)
node7 = DirectedNode(7)
node8 = DirectedNode(8)
node9 = DirectedNode(9)

node1.addAdjacentNode(node2)
node2.addAdjacentNode(node3)
node2.addAdjacentNode(node4)
node1.addAdjacentNode(node5)
node3.addAdjacentNode(node6)
node4.addAdjacentNode(node7)

node5.addAdjacentNode(node9)
node4.addAdjacentNode(node1)
node6.addAdjacentNode(node3)
node7.addAdjacentNode(node4)
node9.addAdjacentNode(node9)
node1.addAdjacentNode(node4)
node3.addAdjacentNode(node2)
node4.addAdjacentNode(node6)
node5.addAdjacentNode(node1)
node1.addAdjacentNode(node4)

# print(route_between_nodes(node1, node8))
print(route_between_nodes(node1, node9))