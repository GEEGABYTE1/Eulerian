from graph import Graph 
from vertex import Vertex 




# Graph 

zero = Vertex(0)
one = Vertex(1)
two = Vertex(2)
three = Vertex(3)
four = Vertex(4)
five = Vertex(5)

g1 = Graph()
g1.add_vertex(zero)
g1.add_vertex(one)
g1.add_vertex(two)
g1.add_vertex(three)
g1.add_vertex(four)
#g1.add_vertex(five)

g1.add_edge(one, zero)
g1.add_edge(zero, two)
g1.add_edge(two, one)
g1.add_edge(zero, three)
g1.add_edge(three, four)
#g1.add_edge(one, three)


# Second Graph 

zero_two = Vertex(0)
one_two = Vertex(1)
two_two = Vertex(2)
three_two = Vertex(3)
four_two = Vertex(4)
five_two = Vertex(5)

g2 = Graph()
g2.add_vertex(zero_two)
g2.add_vertex(one_two)
g2.add_vertex(two_two)
g2.add_vertex(three_two)
g2.add_vertex(four_two)


