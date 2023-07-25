import matplotlib.pyplot as plt
import time
 
class graphy():
    def __init__(self):
        #plt.ion()
        self.figure,self.ax = plt.subplots(figsize=(10,10))
        self.ax.axis('off')


    def draw(self,graph):
        self.__add_nodes__(graph)

    def __find_pos__(self,neightbour,nodes):
        for node in nodes.values():
            if node['Node'] == neightbour:
                return node['Position']
        return []

    def __increase__(self,pos_in,pos_fin):
        dx = pos_fin[0]-pos_in[0]
        dy = pos_fin[1]-pos_in[1]
        if dx == 0:
            if dy < 0:
                dy = dy +0.05
            else:
                dy = dy - 0.05
        if dy == 0:
            if dx < 0:
                dx = dx +0.05
            else:
                dx = dx - 0.05
        return dx,dy

    def __middle__(self,pos_in,pos_fin):
        napla_x = (pos_fin[0]-pos_in[0])/2
        napla_y = (pos_fin[1]-pos_in[1])/2
        if napla_x == 0:
            napla_x = napla_x +0.03
        if napla_y == 0:
            napla_y = napla_y +0.03
        mid_x = pos_in[0]+napla_x
        mid_y = pos_in[1]+napla_y
        return [mid_x,mid_y]

    def __add_edge__(self,pos_in,Edges,nodes):
        for edge in Edges:
            pos_fin = self.__find_pos__(edge['neightbour'],nodes)
            if pos_fin:
                dx,dy = self.__increase__(pos_in,pos_fin)
                #plt.arrow(pos_in[0],pos_in[1],dx,dy,width=.01)
                #pos_text = self.__middle__(pos_in,pos_fin)
                #plt.text(pos_text[0],pos_text[1],'{}'.format(edge['weight']))
            else:
                print('Error')

    def __add_nodes__(self,nodes):
        for node in nodes.values():
            self.ax.plot(node['Position'][0],node['Position'][1],marker = "o",color = 'black')
            #plt.text(node['Position'][0]+0.03,node['Position'][1]+0.03,node['Node'])
            if node['Edge'] != []:
                self.__add_edge__(node['Position'],node['Edge'],nodes)
    
    def move_point(self):
        y = 0
        while True:
            self.figure.canvas.draw()
            self.figure.canvas.flush_events()
            time.sleep(2)

    def NewAGVFigure(self,position):
        Vehicle, = self.ax.plot(position[0],position[1],marker = 'o', color = 'red')
        return Vehicle


