import tkinter as tk
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox

from GUI.Grafos.main import ServiceGrafos

#--------------------------------------------------------------------------Clases de ventana---------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ventana():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.state('zoomed') #Defino que la pantalla principal ocupe toda la pantalla al ejecutar el programa
        tk.Wm.wm_title(self.ventana,"SGA AMR") #Pongo el texto de la parte superior
        self.icon = tk.PhotoImage(file= 'GUI/Sources/logo_LM.png')
        self.ventana.iconphoto(False,self.icon)

class pantalla():
    def __init__(self):
        pass

    def abrir(self,contenedor,bgc):
        self.frame = tk.Frame(contenedor,bg = bgc)
        self.frame.pack(fill = tk.BOTH, expand = True) #Coloco el frame en toda la pantalla

    def cierra(self):
        self.frame.destroy()

    def pop_up(self,texto):
        aviso = tk.Frame(self.frame)
        aviso.config(relief='sunken',bd=5)
        label = tk.Label(aviso,text='{}'.format(texto),font=("Verdana",15))
        boton = tk.Button(aviso,text='Aceptar',command= lambda: aviso.destroy(),font=("Arial",15))
        label.place(relx=0.01, rely=0.2,relheight=0.2,relwidth=1)
        boton.place(relx=0.3, rely=0.6,relheight=0.3,relwidth=0.4)
        aviso.place(relx=0.4, rely=0.35,relheight=0.15,relwidth=0.25)

class pantalla():
    def __init__(self):
        pass

    def abrir(self,contenedor):
        self.frame = tk.Frame(contenedor,bg = 'grey')
        self.frame.pack(fill = tk.BOTH, expand = True) #Coloco el frame en toda la pantalla

    def cierra(self):
        self.frame.destroy()

    def pop_up(self,texto):
        aviso = tk.Frame(self.frame)
        aviso.config(relief='sunken',bd=5)
        label = tk.Label(aviso,text='{}'.format(texto),font=("Verdana",15))
        boton = tk.Button(aviso,text='Aceptar',command= lambda: aviso.destroy(),font=("Arial",15))
        label.place(relx=0.01, rely=0.2,relheight=0.2,relwidth=1)
        boton.place(relx=0.3, rely=0.6,relheight=0.3,relwidth=0.4)
        aviso.place(relx=0.4, rely=0.35,relheight=0.15,relwidth=0.25)

    def open_loading(self):
        self.aviso = tk.Frame(self.frame)
        self.aviso.config(relief='sunken',bd=5)
        label = tk.Label(self.aviso,text='{}'.format('Cargando....'),font=("Verdana",15))
        label.place(relx=0.01, rely=0.2,relheight=0.2,relwidth=1)
        self.aviso.place(relx=0.4, rely=0.35,relheight=0.15,relwidth=0.25)
    
    def close_loading(self):
        self.aviso.destroy()

class GUI():
    def __init__(self,pll):
        self.screen = pll.ventana
        self.frame = pantalla()
        self.frame.abrir(self.screen)
        self.__componentes()

    def __ControllerComponents(self):
        self.OptionFrame = tk.Frame(self.frame.frame,bg='grey')
        self.DecorativeFrame = tk.LabelFrame(self.OptionFrame, text= 'Controller',bd= 6)
        self.Label1 = tk.Label(self.OptionFrame,text='ID AMR',font=("Arial",18))
        self.Label2 = tk.Label(self.OptionFrame,text= 'Destiny',font=("Arial",18))
        self.ButtonSet = tk.Button(self.OptionFrame,text= 'Set Position',font=("Arial",18))
        self.AmrID = ttk.Combobox(self.OptionFrame,font=("Arial",18))
        self.Destininy = tk.Entry(self.OptionFrame,font=("Arial",18))

        self.Label1.place(relx= 0.001,rely=0.15,relheight= 0.3,relwidth=0.3)
        self.Label2.place(relx= 0.25,rely=0.15,relheight= 0.3,relwidth=0.3)
        self.ButtonSet.place(relx= 0.55,rely=0.4,relheight= 0.15,relwidth=0.1)

        self.AmrID.place(relx= 0.05,rely=0.4,relheight= 0.15,relwidth=0.2)
        self.Destininy.place(relx= 0.3,rely=0.4,relheight= 0.15,relwidth=0.2)

        self.OptionFrame.place(rely=0.7,relheight=0.3, relwidth= 1)
        self.DecorativeFrame.place(relx=0,rely=0,relheight= 0.99,relwidth=1)

    def __componentes(self):
        self.GrafoFrame = tk.Frame(self.frame.frame,bg= 'white')
        self.__ControllerComponents()
        self.GrafoFrame.place(rely=0,relheight= 0.7, relwidth= 1)
        ServiceGrafos( self.GrafoFrame)
        
