class Graph:
    def __init__(self,graph_dict=None):
        if graph_dict is None:
            graph_dict={}
        self.__graph_dict=graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self,vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex]=[]
            return

    def add_edge(self,edge):
        edge=set(edge)
        (vertex1,vertex2)=tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1]=[vertex2]

    def __generate_edges(self):
        edges=[]
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour,vertex} not in edges:
                    edges.append({neighbour,vertex})
        return edges

    def find_path(self,start_vertex,end_vertex,path=None):
        if path==None:
            path=[]
        graph=self.__graph_dict
        path=path+[start_vertex]
        if start_vertex==end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path=self.find_path(vertex,end_vertex,path)
                if extended_path:
                    return extended_path
        return None



def main():
    g={'a':['d'],'b':['c'],'c':['b','c','d','e'],'d':['a','c'],'e':['c'],'f':[]}
    graph=Graph(g)
    print("Vertices of graph: ")
    print(graph.vertices())
    print("Edges of graph: ")
    print(graph.edges())
    print("Add vertex: ")
    graph.add_vertex('z')
    print("Vertices of the graph: ")
    print(graph.vertices())
    print("Add an edge: ")
    graph.add_edge({'a','z'})
    print("Vertices of the graph: ")
    print(graph.vertices())
    print("Edges of the graph: ")
    print(graph.edges())
    print("Adding an edge 'x','y' in the graph with new vertices:")
    graph.add_edge({'x','y'})
    print("Vertices of graph: ")
    print(graph.vertices())
    print("Edges of graph: ")
    print(graph.edges())
    print("PATH from vertex 'a' to vertex 'b': ")
    print(graph.find_path('a','b'))
    print("PATH from vertex 'a' to vertex 'f': ")
    print(graph.find_path('a','f'))
    print("PATH from vertex 'c' to vertex 'c': ")
    print(graph.find_path('c','c'))



main()
