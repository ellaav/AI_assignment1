from Gready_Agent import Dijkstra , number_of_people_in_the_graph
from Problem import State , Problem
import numpy as np
from Graph import make_graph , drawing_graph

scale=15

def h(state):
    num_of_p=number_of_people_in_the_graph(state.Graph)
    Dijkstra(state.Graph,state.Node)
    count_path=0
    for i in state.Graph.nodes:
        if i != state.Node and state.Graph.nodes[i]["P"]>0:
            count_path+=state.Graph.nodes[i]["dist"]
    num =(num_of_p-state.Graph.nodes[state.Node]["P"])*scale+count_path
    # print("the heuristic result is: ", num)
    if num_of_p == 0:
        return 0
    return (num_of_p-state.Graph.nodes[state.Node]["P"])*scale+count_path

def g(node):
    pass

def f(h,state,graph):
    # print("h(",state.Node,")=",h(state,graph))
    # print("g(", state.Node, ")=", state.g)
    return state.g + h(state,graph)

def Expand(state,graph):
    nighbores = []
    for i in list(graph.adj[state.Node]):
        #print("the i is: " , i)
        newnode = State(i,graph,state,state.g+graph.edges[state.Node,i]["weight"])
        # if newnode.Graph.nodes[i]["P"] > 0:
        #     newnode.Graph.nodes[i]["P"] = 0

       # newnode.Graph.nodes[i]["g(node)"] =  node.Graph.nodes[node.Node]["g(node)"] + newnode.Graph.edges[node.Node,i]["weight"]
        #print("the new node in Expand is: ", node.Node)
       # drawing_graph(node.Graph)
        nighbores.append(newnode)
    return nighbores

def collect_P(state):
    if state.Node in state.Nodes_W_P:
        state.Nodes_W_P.remove(state.Node)

def A_Star(problem, h,f):
    OPEN = [problem.Initial_State]
    CLOSE = []
    count=0
    while(True):
        if len(OPEN) == 0:
            return "failure"
        else:
            state = OPEN.pop(0)
            collect_P(state)
            # print("open.len:",len(OPEN))
            count+=1
            if count%10==0:
                print("loop num: ",count)
            # print("the new A* State is: ", state.Node)
            #drawing_graph(state.Graph)
            if problem.Goal_Test(state, h):
                # print("finish at state= ",state.Node)
                # print("count:", count)
                return state
            if not in_close(CLOSE,state):    ## there is a problem with the node state
                CLOSE.insert(0, state)
                expandarray = Expand(state,problem.Graph)
                OPEN = OPEN + expandarray
                Sort_By_F(f,OPEN,h,problem.Graph)



#put in open[0] the state with minimum f(s)

def Sort_By_F(f,open,h,graph):
    newstate = open.pop()
    minimun = f(h,newstate,graph)
    for i in open:
        heuristic = f(h,i,graph)
        if heuristic < minimun:
            minimun = heuristic
            open.insert(0,newstate)
            newstate = i
            open.remove(i)
    # print("minimum Heuristic",minimun)
    open.insert(0, newstate)

       
def restore_path(state):
    path=[state.Node]
    while state.Prev!=None:
        path.insert(0,state.Prev.Node)
        state=state.Prev


    return path

def in_close(close,state):
    for s in close:
        if s.Node==state.Node and s.Nodes_W_P==state.Nodes_W_P and s.g<=state.g:
            return True
    return False

# graph = make_graph("graph.txt")
# problem = Problem(graph,1,0)
# heuristic = h
# somef = f
# graph2=graph.copy()
# sol=A_Star(problem,heuristic,somef)
# print("solution= ",restore_path(sol))
# drawing_graph(graph2)
