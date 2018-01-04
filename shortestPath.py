#!/usr/bin/env python3

####################################################################################
############################# shortestPath.py #####################################
# Python 3.3
# Version: 1.0
# Author: Nicolas Chen

# Description: Dijkstra's algorithm
# This is an algorithm for finding the shortest paths between nodes in a graph,
# which may represent, for example, road networks.
####################################################################################


def get_parents(parent, departure, child, path):
    if child == departure:
        return [departure] + path
    else:
        return (get_parents(parent, departure, parent[child], [child] + path))


def shortest_path(graph, vertex, end, visited, dist, parent, departure):
    """
	Gets recursively the shortest path between the departure and end of Dijkstra's algorithm    	
	visited is the list
	dist and parent are dictionaries    
    graph: the studied graph                                                                
    vertex: current vertex studied                   
    end: end of the path                                            
    visited: list of the vertex already visited 	
	dist: best distance between the departure and the vertices of the graph
	parent: dictionary of current parents from vertices corresponding to the best paths
	departure: departure node
	returns the tuple (length of the shortest path , list of the vertices for the shortest path)
    """
	
    # if we reach the end, we display the distance and the parents
    if vertex == end:
        return dist[end], get_parents(parent, departure, end, [])
    # if it is the first visit, it means that the current vertex is the departure: we set dist[vertex] to 0
    if len(visited) == 0:
        dist[vertex] = 0
    # we go through the neighboor nodes not visited
    for neighboor in graph[vertex]:
        if neighboor not in visited:
            # the distance is either the distance computed before or infinity
            dist_neighboor = dist.get(neighboor, float('inf'))
            # computation of the new distance passing by the vertex
            new_dist = dist[vertex] + graph[vertex][neighboor]
            # if it is a shortest path, then we make the changes
            if new_dist < dist_neighboor:
                dist[neighboor] = new_dist
                parent[neighboor] = vertex
    visited.append(vertex)
    # we are looking for the vertex not visited the nearest to the departure
    no_visited = dict((node, dist.get(node, float('inf'))) for node in graph if node not in visited)
    nearest_node = min(no_visited, key=no_visited.get)
    # we apply recursively by taking as a new node the nearest vertex
    return shortest_path(graph, nearest_node, end, visited, dist, parent, departure)


def recursive_dijkstra(graph, start, end):
    return shortest_path(graph, start, end, [], {}, {}, start)


def main():
    graph1 = {'a': {'d': 1, 'g': 2},
              'b': {'a': 1},
              'c': {'b': 1, 'f': 1, 'g': 2},
              'd': {'g': 4, 's': 8},
              'e': {'a': 6, 'b': 2, 'c': 1},
              'f': {'d': 2, 's': 9},
              'g': {'f': 2},
              's': {}
              }

    length1, vertices_path1 = recursive_dijkstra(graph1, 'e', 's')
    print "The shortest path for the graph1 is: ", vertices_path1, " with a length of:", length1

    graph2 = {'a': {'d': 8, 'e': 6, 'b' : 1},
          'b': {'e' : 8, 'c' : 5},
          'c': {'e' : 9, 'g' : 2},
          'd': {'e': 2, 'f': 6},
          'e': {'f': 2, 'g' : 5},
          'f': {'h' : 4},
          'g': {'h' : 2},
          'h': {}
    }
	
    length2,vertices_path2 = recursive_dijkstra(graph2,'a','h')
    print "The shortest path for the graph2 is: ", vertices_path2, " with a length of:", length2

if __name__ == "__main__":
    main()