from Graph import drawing_graph
from Problem import State
from a_star_alg import *



def Expand(node):
    nighbores = []
    for i in list(node.Graph.adj[node.Node]):
        # print("the i is: " , i)
        newnode = State(i,node.Graph.copy())
        if newnode.Graph.nodes[i]["P"] > 0:
            newnode.Graph.nodes[i]["P"] = 0
        #drawing_graph(newnode.Graph)
        newnode.Graph.node[i]["g(node)"] =  node.Graph.node[node.Node]["g(node)"] + newnode.Graph.edges[node.Node,i]["weight"]
       # print("the new node in Expand is: ", newnode)
        nighbores.append(newnode)
    return nighbores


def Gready_Heuristic_Agent(problem,h):
    OPEN = [problem.Initial_State]
    CLOSE = []
    while(True):
        if len(OPEN) == 0:
            return "failure"
        else:
            state = OPEN.pop(0)
            if problem.Goal_Test(state, h): 
                return state
            if not state in CLOSE:    ## there is a problem with the node state
                expandarray = Expand(state)
                print("FINISH EXPAND")
                OPEN = OPEN + expandarray
                Sort_By_H(OPEN,h)
                #print("THe size of open is: " ,len(OPEN))
                for i in OPEN:
                    print("The node in open is: ", i.Node , "The Heuristic of i in the open arr is: ", f(h,i))
                print ("THE first State in OPEN is: ", "and the node is: ", OPEN[0].Node, "and his Heuristic is: ", f(h,OPEN[0]))
                drawing_graph(OPEN[0].Graph)


def Sort_By_H(open,h):
    newstate = open.pop(0)
    minimun = h(newstate)
    for i in open:
        heuristic = h(i)
        if heuristic < minimun:
            print ("the node with the min heuristic is: ", i.Node, "and his heuristic is: " ,f(h,i)) 
            minimun = heuristic
            open.insert(0,newstate)
            newstate = i
            open.remove(i)
    print ("the node with the min heuristic is That Go in Open is: ", newstate.Node, "and his heuristic is: " ,f(h,newstate)) 
    open.insert(0, newstate)




graph = make_graph("graph.txt")
problem = Problem(graph,1,0)
heuristic = h

graph2=graph.copy()
sol=Gready_Heuristic_Agent(problem,heuristic)
print("solution= ",restore_path(sol))
drawing_graph(graph2)
