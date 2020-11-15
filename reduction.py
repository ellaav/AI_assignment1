import networkx as nx
from Gready_Agent import *
from Graph import *
from a_star_alg import *
from Problem import *

def reduct(graph,sorce):

    reducted_graph=nx.Graph()
    reducted_graph.add_node(sorce,P=0)
    for i in graph.nodes:
        if graph.nodes[i]["P"]>0 and i!=sorce:
            reducted_graph.add_node(i,P=graph.nodes[i]["P"])

    for i in reducted_graph.nodes:
        Dijkstra(graph,i)
        for j in reducted_graph.nodes:

            if j>i:
                reducted_graph.add_edge(i,j,weight=graph.nodes[j]["dist"])

    return reducted_graph




#graph should be a copy
def H_tag(state,graph):
       # print_graph(state.Graph)
       #  num_of_p = number_of_people_in_the_graph(state.Graph)-state.Graph.nodes[state.Node]["P"]
        num_of_p=len(state.Nodes_W_P)
        if num_of_p == 0 or (num_of_p==1 and state.Node==state.Nodes_W_P[0]):
            return 0
        Dijkstra(graph, state.Node)
        min_w = float('inf')
        for i in state.Nodes_W_P:
            if i!=state.Node and min_w > graph.nodes[i]["dist"]:
                min_w = graph.nodes[i]["dist"]



        # print("the heuristic result is: ", min_w)

        return min_w

def restore_original_path(path,map):
    original_p=[path[0]]

    for i in range(0,len(path)-1):
        original_p=original_p+map[(path[i],path[i+1])]

    return original_p


# g=make_graph("graph.txt")
# gr=reduct(g,1)
# # print_graph(gr)
# # drawing_graph(gr)
#
def make_map(graph, sorce):
    map= {}

    reducted_graph = nx.Graph()
    reducted_graph.add_node(sorce, P=0)
    for i in graph.nodes:
        if graph.nodes[i]["P"] > 0 and i != sorce:
            reducted_graph.add_node(i, P=graph.nodes[i]["P"])

    for i in reducted_graph.nodes:
        Dijkstra(graph, i)
        for j in reducted_graph.nodes:


            tmp_path = []
            tmp_node=j
            while tmp_node!=i:
                tmp_path.insert(0,tmp_node)
                tmp_node=graph.nodes[tmp_node]["prev"]
            map[(i,j)] = tmp_path

    return map

def like_main(graph):
    graph = make_graph(graph)
    map = make_map(graph, 1)
    # print("map= ", map)
    small_G = reduct(graph, 1)
    # drawing_graph(small_G)
    problem = Problem(small_G, 1, 0)

    heuristic = H_tag
    somef = f
   # graph2 = small_G.copy()
    sol = A_Star(problem, heuristic, somef)
    print("solution small graph= ", restore_original_path(restore_path(sol), map))

like_main("random_graph.txt")
# graph = make_graph("graph.txt")
# map=make_map(graph,1)
# print("map= ",map)
# small_G=reduct(graph,1)
# # drawing_graph(small_G)
# problem = Problem(small_G,1,0)
#
# heuristic = H_tag
# somef = f
# graph2=small_G.copy()
# sol=A_Star(problem,heuristic,somef)
# print("solution small graph= ",restore_original_path(restore_path(sol),map))
# problem2 = Problem(graph,1,0)
# sol1=A_Star(problem2,heuristic,somef)
# print("solution= ",restore_path(sol1))
# # drawing_graph(graph2)

# graph3=graph.copy()
# sol2=A_Star(problem2,heuristic,somef)
# print("solution= ",restore_path(sol2))
# drawing_graph(graph3)