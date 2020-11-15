from Graph import print_graph , drawing_graph


class Human_Agent(object):

    def __init__(self,graph,node):
        self.Score = 0
        self.Graph = graph
        self.State = node
        self.Turn_To_Wait = 0
        self.Terminate = False
    
    def Do_Turn(self):
        if self.Terminate == False:
            print_graph(self.Graph)
            if(self.Turn_To_Wait ==0):
                print("the state is: " ,self.State)
                action =  input("enter next move:")
                if action != "terminate":
                    action = int(action)
                    self.Turn_To_Wait = print(self.Graph.adj[self.State][action]["weight"])
                    self.Turn_To_Wait = int(self.Graph.adj[self.State][action]["weight"])
                    self.State = action
                    people = self.Graph.nodes[action]["P"]
                    print("the numer of people pepole:" , people)
                    if(people> 0):
                        self.Score += people
                        self.Graph.nodes[action]["P"]= 0
                    drawing_graph(self.Graph)
                    print("the new state is: " ,self.State)
                else:
                    self.Terminate = True
            else:
                self.Turn_To_Wait-=1
                print("still have ", self.Turn_To_Wait , " turns to wait")
        else:
            print("The Human Agent is TERMINATED")


def human(graph,node):
    score = 0
    action = ""
    state = node
    print_graph(graph)
    print("the state is: " ,state)
    action =  input("enter next move:")
    while (action != "terminate"):
        action = int(action)
        state = action
        people = graph.nodes[action]["P"]
        print("the pepolr:" , people)
        if(people> 0):
            score += people
            graph.nodes[action]["P"]= 0
        print_graph(graph)
        print("the state is: " ,state)
        action =  input("enter next move:")
