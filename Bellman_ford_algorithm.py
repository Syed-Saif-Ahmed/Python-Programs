inf = 99999

graph = {}
vertices_no = 0
d = []
p = []

def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print(v,"Already exist!!")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []
def add_edge(v1,v2,e):
    global graph
    if v1 not in graph:
        print(v1,"does not exist!!")
    elif v2 not in graph:
        print(v2,"does not exist!!")
    else:
        temp = [v2,e]
        graph[v1].append(temp)
def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex,"-->",edges[0],"weight ::",edges[1])

def bellman_ford_algo(graph,start):
    for vertex in graph:
        d.append(inf)
        p.append(None)
    d[start] = 0

    for vertex in graph:
        for edges in graph[vertex]:
            if d[edges[0]] > d[vertex] + edges[1]:
                d[edges[0]] = d[vertex] + edges[1]
                p[edges[0]] = vertex
    for vertex in graph:
        for edges in graph[vertex]:
            if d[edges[0]] > d[vertex] + edges[1]:
                return False
    
    print("\ndistance = ",d)
    print("previous = ",p)
    
def making_graph_adj_list():
    n = int(input("Enter the number of vertices ::"))
    print()
    for i in range(n):
        add_vertex(int(input("Enter the vertex ::")))
    print()
    n = int(input("Enter the number of edges ::"))
    print()
    for i in range(n):
        e1 = int(input("Enter start vertex :"))
        e2 = int(input("Enter end vertex :"))
        w = int(input("Enter edge weight :"))
        print()
        add_edge(e1,e2,w)
    print_graph()
print()
making_graph_adj_list()
print()
bellman_ford_algo(graph,0)

print(graph)
