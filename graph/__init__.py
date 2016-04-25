'''
Graph Class and methods
@auther Saurabh P Sabnis 
'''


class Edge:
    "Edge class stores weight and node associated with the edge"
    
    def __init__(self,start,end,weight):
        try:
            self.start = start
            self.end = end
            self.weight = int(weight)
        except ValueError:
            print "Only int for weight"
            exit()
    
    def __eq__(self,other):
        return self.start == other.start and self.end == other.end
    
    def __str__(self):
        return "edge Start:" + str(self.start) + " end:" + str(self.end) + " val: " + str(self.weight)
        
    
class Graph:
    '''Graph class which will store the graph in adjacency list format
    type of the graph can be directed or Not Directed graph'''
    def __init__(self,Gtype):
        try:
            self.graphEdges = []
            self.graphVtxs = {} 
            self.directed = Gtype
        except NameError:
            print "Wrong type : can be 'Directed' OR 'notDirected'"
            return None
    def isEdgePresent(self,e):
        for i in self.graphEdges:
            if e == i:
                return True
        return False
    
    def printAdjcList(self):
        "Print Graph in Adjacency list Format"
        print "Printing Graph: Adjacency List"
        for i in self.graphVtxs.keys():
            print "node:" + str(i) + " adj nodes:",
            for j in self.graphVtxs[i]:
                print j.end ,"(" +str(j.weight)+")   ",
            print
            
    def add_edge(self,v1,v2,val = 0):
        "Add edge to graph, return True if successful else return False if already present"
        if v1 not in self.graphVtxs:
            self.graphVtxs[v1] = []
        if v2 not in self.graphVtxs:
            self.graphVtxs[v2] = []
        if v1 == v2 and self.directed == False:
            print "Not allowed from {} to {}".format(v1,v2)
            return False
        e = Edge(v1,v2,val)
        if not self.isEdgePresent(e):
            self.graphEdges.append(e)
            self.graphVtxs[v1].append(e)
            if self.directed != True:
                e = Edge(v2,v1,val)
                self.graphEdges.append(e)
                self.graphVtxs[v2].append(e)
            return True
        else:
            print "edge present from {} to {}".format(v1,v2)
            return False
        
if __name__ == '__main__':           
    gr = Graph(True)
    gr.add_edge(5, 6)
    gr.add_edge(3, 6)
    gr.add_edge(1, 3)
    gr.add_edge(5, 4)
    gr.add_edge(5, 6)
    gr.add_edge(5, 2)
    gr.printAdjcList()

