class Graph:
	def __init__(self, gdict=None):
		if gdict is None:
			gdict = {}
		self.gdict = gdict
	
	def getVertex(self):
		return list(self.gdict.keys())
	
	def getEdges(self):
		edges = []
		for v in self.gdict:  # ✅ iterasi semua vertex
			for e in self.gdict[v]:  # tetangga dari v
				# Gunakan tuple terurut agar edge (a,b) dan (b,a) dianggap sama
				edge = tuple(sorted([v, e]))
				if edge not in edges:
					edges.append(edge)
		return edges


# Definisi graph
graph_data = {
	"a": ["b", "c"],
	"b": ["a", "d"],
	"c": ["a", "d"],
	"d": ["e"],
	"e": ["d"]
}

g = Graph(graph_data)
print("Vertices:", g.getVertex())
print("Edges:   ", g.getEdges())