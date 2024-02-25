def floyd(distance):
 """
 A simple implementation of Floyd's algorithm
 """
 for intermediate, start_node,end_node\
 in itertools.product\
 (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):

     # Assume that if start_node and end_node are the same
     # then the distance would be zero
     if start_node == end_node:
         distance[start_node][end_node] = 0
         continue

     #return all possible paths and find the minimum
     distance[start_node][end_node] = min(distance[start_node][end_node],
                   distance[start_node][intermediate] + distance[intermediate][end_node] )
 #Any value that have sys.maxsize has no path
 print (distance)

