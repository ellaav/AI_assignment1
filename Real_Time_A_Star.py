from Graph import drawing_graph
from Gready_Agent import Dijkstra , number_of_people_in_the_graph
from Problem import State
import time


scale = 5

def h(state):
    num_of_p=number_of_people_in_the_graph(state.Graph)
    Dijkstra(state.Graph,state.Node)
    count_path=0
    for i in state.Graph.nodes:
        if i != state.Node and state.Graph.nodes[i]["P"]>0:
            count_path+=state.Graph.nodes[i]["dist"]
    num =(num_of_p-state.Graph.nodes[state.Node]["P"])*scale+count_path
   # print("the heuristic result is: ", num)
    return (num_of_p-state.Graph.nodes[state.Node]["P"])*scale+count_path

def g(node):
    pass

def f(h,state):
    # g = state.Graph.nodes[state.Node]["g(node)"]
    # print("the g function is:" , g)
    # print("the heuristic function is:" , h(state))
    return state.Graph.nodes[state.Node]["g(node)"] + h(state)

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

def Real_Time_A_Star(problem, h,f, timelimit):
    OPEN = [problem.Initial_State]
    CLOSE = []
    starttime = time.time()
    timelimit = starttime + timelimit
    while(True):
        thetime = time.time()
        if len(OPEN) == 0:
            return "failure"
        else:
            state = OPEN.pop(0)
            if problem.Goal_Test(state, h): 
                return state
            if thetime >= timelimit:
                return state
            if not state in CLOSE:    ## there is a problem with the node state
                expandarray = Expand(state)
                print("FINISH EXPAND")
                OPEN = OPEN + expandarray
                Sort_By_F(f,OPEN,h)
                #print("THe size of open is: " ,len(OPEN))
                for i in OPEN:
                    print("The node in open is: ", i.Node , "The Heuristic of i in the open arr is: ", f(h,i))
                print ("THE first State in OPEN is: ", "and the node is: ", OPEN[0].Node, "and his Heuristic is: ", f(h,OPEN[0]))
                drawing_graph(OPEN[0].Graph)
                

def Sort_By_F(f,open,h):
    newstate = open.pop(0)
    minimun = f(h,newstate)
    for i in open:
        heuristic = f(h,i)
        if heuristic < minimun:
            print ("the node with the min heuristic is: ", i.Node, "and his heuristic is: " ,f(h,i)) 
            minimun = heuristic
            open.insert(0,newstate)
            newstate = i
            open.remove(i)
    print ("the node with the min heuristic is That Go in Open is: ", newstate.Node, "and his heuristic is: " ,f(h,newstate)) 
    open.insert(0, newstate)


