import networkx as nx
import matplotlib.pyplot as plt
from Graph import make_graph , drawing_graph , print_graph
from Gready_Agent import *
from Saboteur import *
from Human_Agent import *

## to split the code o diffrent
#from .Graph import make_graph , print_graph
# make sure that the function changes the graph       
def Running_Enviorment(agent1 ,agent2 ,agent3):
    while(agent1.Terminate == False or agent2.Terminate == False or agent3.Terminate == False):
        agent1.Do_Turn()
        agent2.Do_Turn()
        agent3.Do_Turn()
#
# g = make_graph("graph.txt")
# g2 = g.copy()
# man = Human_Agent(g,1)
# greadyagent = Gready_Agent(g,1)
# thesabotuer = Sabotuer(g,1,5)
# h = Running_Enviorment
# h(greadyagent,man,thesabotuer)
# drawing_graph(g)
#saboteur(g,1,1)
#gready(g,1)
#Dijkstra(g2,1)
#print(g.adj[1], g.nodes[1])
#print(g.nodes.data())
#print(g.edges.data())
#print_graph(g)
#human(g , 1)
#print_graph(g)

##--------- Testing an agent
#while(count <20):
#     count+=1
#     if(thesabotuer.Turns_To_Wait_At_Start ==0):
#         thesabotuer.Do_Turn()
#     else:
#         print("gready need to wait: ", thesabotuer.Turns_To_Wait_At_Start , "turns")
#         thesabotuer.Turns_To_Wait_At_Start-=1    
## ----------------------

# ------ test what the fuction of the graph -------
# for edge in g.adj[1]:     
#             print("Edge:", edge, "\n")
#             print("Nodes:" , g.nodes[edge] , "\n")
#             print("Nodes:" , g.edges[1,edge] , "\n")
g = make_graph("graph.txt")
