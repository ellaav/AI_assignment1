from Graph import drawing_graph

class Sabotuer(object):

    def __init__(self,graph,node,v_no_ops):
        self.State = node
        self.Graph = graph
        self.Turns_To_Wait_At_Start = v_no_ops
        self.Terminate = False

    def Do_Turn(self):
        if(self.Terminate == False):
            if self.Turns_To_Wait_At_Start == 0:
                print( "the start state is: " , self.State)
                # Chose_Lightest is a function that returns the lightest edge from all the neighbores of the state
                edge = self.Chose_Lightest()
                self.Graph.remove_edge(self.State, edge)
                drawing_graph(self.Graph)
                self.State = self.Chose_Lightest()
                if(self.State == 0):
                    self.Terminate == True
                else:
                    print("move to state: " , self.State)
            else:
                self.Turns_To_Wait_At_Start -=1
        else:
            print("Sabotuer is TERMINATED")


    def Chose_Lightest(self):
        min_weight = float('inf')
        chosen_edge = 0
        # print("the neibores: " ,graph.adj[state])
        for i in self.Graph.adj[self.State]:
            if self.Graph.edges[self.State, i]["weight"] < min_weight:
                min_weight = self.Graph.edges[self.State, i]["weight"]
                chosen_edge = i
                print("the min weight: ", min_weight)
                print("the chosen edge: ", chosen_edge)
        return chosen_edge



def saboteur(graph,start,v_no_ops):
    state = start
    print( "the state is: " , state)
    size =  len(list(graph.adj[state]))
    while size > 0:
       # Chose_Lightest is a function that returns the lightest edge from all the neighbores of the state
       edge = Chose_Lightest(graph, state)
       graph.remove_edge(state, edge)
       drawing_graph(graph)
       state = Chose_Lightest(graph, state)
       if( state == 0):
           break
       print(state)
       print(list(graph.adj[state]))
       size = len(list(graph.adj[state]))


def Chose_Lightest(graph , state):
    min_weight = float('inf')
    chosen_edge = 0
    print("the neibores: " ,graph.adj[state])
    for i in graph.adj[state]:
        if graph.edges[state, i]["weight"] < min_weight:
            min_weight = graph.edges[state, i]["weight"]
            chosen_edge = i
            print("the min weight: ", min_weight)
            print("the chosen edge: ", chosen_edge)
    return chosen_edge