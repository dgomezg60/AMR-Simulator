from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.Grafos.Grafict.Draw_graph import graphy
from GUI.Grafos.Grafict.Graph import Graph, Node
from DB.StartDB import Graphs

def ServiceGrafos(frame):
    graph = Graph()
    global MapGrafict
    graph_data = Graphs()
    # Add vertices
    for node in graph_data.values():
      graph.add_node(Node(node['Node'],(node['Position'][0],node['Position'][1])))
    # Add edges
    for node in graph_data.values():
      for edge in node['Edge']:
        graph.add_edge(node['Node'],edge['neightbour'],edge['weight'])
    graphy_drawing = graphy()
    line_graph = FigureCanvasTkAgg(graphy_drawing.figure,frame)
    graphy_drawing.draw(graph_data)
    MapGrafict = graphy_drawing
    line_graph.get_tk_widget().pack()
    #graphy_drawing.move_point()

