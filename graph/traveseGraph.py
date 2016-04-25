
import graph

def bfs(g):
    "Print Breadth First Search of Given Graph"
    queue = []
    visited = dict()
    if not isinstance(g, graph.Graph):
        print "Given argument is not a graph"
        return
    else:
        print "BFS of given Graph: ",
        for i in g.graphVtxs.keys():
            if i not in visited:
                queue.append(i)
                while len(queue) != 0:
                    node = queue.pop(0)
                    if node not in visited:
                        print node,
                        visited[node] = True
                        for i in g.graphVtxs[node]:
                            queue.append(i.end)
        print
        
    
def dfs(g):
    "Print Depth first search for given graph"
    stack = []
    visited = dict()
    if not isinstance(g, graph.Graph):
        print "Given argument is not a graph"
        return 
    else:
        print "DFS of given graph: ",
        for i in g.graphVtxs.keys():
            if i not in visited:
                stack.append(i)
                while len(stack) != 0:
                    node = stack.pop()
                    if node not in visited:
                        print node,
                        visited[node] = True
                        for i in g.graphVtxs[node]:
                            stack.append(i.end)
    

if __name__ == '__main__':
    g = graph.Graph(False)
    g.add_edge('c', 'd', 3)
    g.add_edge('a', 'd', 5)
    g.add_edge('s', 'd', 6)
    g.add_edge('c', 'x', 7)
    g.add_edge('b', 'x', 8)
    g.add_edge('a', 'a', 1)
    g.add_edge('x', 'd', 7)
    g.add_edge('c', 'a', 8)
    g.add_edge('d', 'b', 10)
    g.add_edge('d', 's', 22)
    g.printAdjcList()
    bfs(g)
    dfs(g) 