import tkinter as tk
from tkinter import ttk
from DB.SQLLite import DB
from GUI.Grafos.main import ServiceGrafos
from Algorithm.backend import LockForPath

#--------------------------------------------------------------------------Clases de ventana---------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ventana():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.attributes('-zoomed',True) #Defino que la pantalla principal ocupe toda la pantalla al ejecutar el programa
        self.ventana.minsize(1300,700)
        tk.Wm.wm_title(self.ventana,"SGA AMR") #Pongo el texto de la parte superior
        self.icon = tk.PhotoImage(file= 'GUI/Sources/logo_LM.png')
        self.ventana.iconphoto(False,self.icon)

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
        self.Db = DB()
        self.Db.Connect()
        self.frame = pantalla()
        self.frame.abrir(self.screen)
        self.__componentes()

    def __UpdateInf(self,*args):
        Id = self.__ComboBoxId.get()
        AMRInfo = self.Db.Find('AMR',f'IDAMR={Id}')[0]
        self.__EntryBattery.delete(0,tk.END)
        self.__EntryPosition.delete(0,tk.END)
        self.__EntryPath.delete(0,tk.END)
        self.__EntryStatus.delete(0,tk.END)

        self.__EntryBattery.insert(0,str(AMRInfo[3]))
        self.__EntryPosition.insert(0,str(AMRInfo[2]))
        self.__EntryPath.insert(0,str(AMRInfo[4]))
        self.__EntryStatus.insert(0,str(AMRInfo[1]))

    def __UpdateList(self,Widget):
        Id= self.Db.ReadColum('AMR','IDAMR')
        Widget['values'] = Id

    def __InformationFrame(self):
        self.__FrameInf = tk.Frame(self.__OptionFrame,bg='grey')
        self.__DecorativeInf = tk.LabelFrame(self.__FrameInf,labelanchor= 'n',text= 'Information', bd= 5)
        self.__LabelId = tk.Label(self.__FrameInf,text='ID:',font=("Arial",18))
        self.__LabelStatus = tk.Label(self.__FrameInf,text='Status:',font=("Arial",18))
        self.__LabelBattery = tk.Label(self.__FrameInf,text='Battery:',font=("Arial",18))
        self.__LabelPosition = tk.Label(self.__FrameInf,text= 'Position:',font=("Arial",18))
        self.__LabelPath = tk.Label(self.__FrameInf,text= 'Path:',font=("Arial",18))
        Id= self.Db.ReadColum('AMR','IDAMR')
        self.__ComboBoxId = ttk.Combobox(self.__FrameInf,font=("Arial",18),values=Id,postcommand= lambda:self.__UpdateList(self.__ComboBoxId))
        self.__ComboBoxId.bind("<<ComboboxSelected>>",self.__UpdateInf)
        self.__EntryStatus = tk.Entry(self.__FrameInf)
        self.__EntryBattery = tk.Entry(self.__FrameInf)
        self.__EntryPosition = tk.Entry(self.__FrameInf)
        self.__EntryPath = tk.Entry(self.__FrameInf)

        self.__LabelId.place(relx= 0.05,rely=0.1)
        self.__LabelStatus.place(relx= 0.05,rely=0.25)
        self.__LabelBattery.place(relx= 0.05,rely=0.40)
        self.__LabelPosition.place(relx= 0.05,rely=0.55)
        self.__LabelPath.place(relx= 0.05,rely=0.70)

        self.__ComboBoxId.place(relx= 0.3,rely=0.1,relheight=0.15,relwidth=0.5)
        self.__EntryStatus.place(relx= 0.3,rely=0.25,relheight=0.15,relwidth=0.5)
        self.__EntryBattery.place(relx= 0.3,rely=0.40,relheight=0.15,relwidth=0.5)
        self.__EntryPosition.place(relx= 0.3,rely=0.55,relheight=0.15,relwidth=0.5)
        self.__EntryPath.place(relx= 0.3,rely=0.70,relheight=0.15,relwidth=0.5)

        self.__DecorativeInf.place(relx=0,rely=0,relheight= 0.99,relwidth=1)
        self.__FrameInf.place(relx= 0.69,rely=0.05,relheight=0.9, relwidth= 0.3)

    def __GoTo(self):
        FinisPoint = self.__Destininy.get()
        AMR = self.__AmrID.get()
        if FinisPoint == '' or AMR == '':
            self.frame.pop_up('Complete all the parameters')
        else:
            LockForPath(AMR,FinisPoint)

    def __ControllerComponents(self):
        self.__OptionFrame = tk.Frame(self.frame.frame,bg='grey')
        self.__DecorativeFrame = tk.LabelFrame(self.__OptionFrame, text= 'Controller',bd= 6)
        self.__Label1 = tk.Label(self.__OptionFrame,text='ID AMR',font=("Arial",18))
        self.__Label2 = tk.Label(self.__OptionFrame,text= 'Destiny',font=("Arial",18))
        self.__ButtonSet = tk.Button(self.__OptionFrame,text= 'Set Position',font=("Arial",18),command= self.__GoTo)
        Id= self.Db.ReadColum('AMR','IDAMR')
        self.__AmrID = ttk.Combobox(self.__OptionFrame,font=("Arial",18),values=Id,postcommand= lambda: self.__UpdateList(self.__AmrID))
        self.__Destininy = tk.Entry(self.__OptionFrame,font=("Arial",18))

        self.__Label1.place(relx= 0.001,rely=0.15,relheight= 0.3,relwidth=0.3)
        self.__Label2.place(relx= 0.25,rely=0.15,relheight= 0.3,relwidth=0.3)
        self.__ButtonSet.place(relx= 0.55,rely=0.4,relheight= 0.15,relwidth=0.1)

        self.__AmrID.place(relx= 0.05,rely=0.4,relheight= 0.15,relwidth=0.2)
        self.__Destininy.place(relx= 0.3,rely=0.4,relheight= 0.15,relwidth=0.2)

        self.__OptionFrame.place(rely=0.7,relheight=0.3, relwidth= 1)
        self.__DecorativeFrame.place(relx=0,rely=0,relheight= 0.99,relwidth=1)
        self.__InformationFrame()

    def __componentes(self):
        self.__GrafoFrame = tk.Frame(self.frame.frame,bg= 'white')
        self.__ControllerComponents()
        self.__GrafoFrame.place(rely=0,relheight= 0.7, relwidth= 1)
        ServiceGrafos( self.__GrafoFrame)
        
