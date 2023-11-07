class Node:

	def __init__(self, value):
		self.value = value
		self.edges = []

	def append(self, edge):
		self.edges.append(edge)

class Edge:

	def __init__(self, source, target):
		self.source = source
		self.target = target

def build_graph(projects, dependencies):
	nodes = {}

	for dependency in dependencies:
		source, target = dependency

		if source not in nodes.keys():
			source_node = Node(source)
			nodes[source] = source_node
		else:
			source_node = nodes[source]

		if target not in nodes.keys():
			target_node = Node(target)
			nodes[target] = target_node
		else:
			target_node = nodes[target]

		edge = Edge(source_node, target_node)
		target_node.append(edge)
		source_node.append(edge)

	for project in projects:
		if project not in nodes.keys():
			nodes[project] = Node(project)

	return nodes

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

graph = build_graph(projects, dependencies)

for (project, node) in graph.items():
	print(node.value)

	for edge in node.edges:
		print((edge.source.value, edge.target.value))

print('-----------')

def find_source(node):
	'''
	Find the node that doesn't have incoming edge
	'''

	for edge in node.edges:
		if edge.target == node:
			return find_source(edge.source)
	return node

def remove_edges(root_node, graph):
	'''
	This function assumes the root_node has only outgoing
	edges and removes the edges from other nodes where
	the root_node is the source node
	'''

	for edge in root_node.edges:
		target_node = edge.target

		for edge_of_target in target_node.edges:
			if target_node == edge_of_target.target and root_node == edge_of_target.source:
				target_node.edges.remove(edge_of_target)


def build_order(projects, dependencies):
	graph = build_graph(projects, dependencies)
	result = []

	while len(projects) > 0:
		project = projects[0]
		node = graph[project]

		root_node = find_source(node)
		result.append(root_node.value)
		del graph[root_node.value]
		projects.remove(root_node.value)

		remove_edges(root_node, graph)

	return result

print(build_order(projects, dependencies))





