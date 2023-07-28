from time import sleep
from GUI.OpenGUI import open
from threading import Thread 
from WebsocketClient.Individual import origin
from WebsocketServer.Server import main
import subprocess

def EnableServer():
    # Crear un nuevo proceso para la consola de registros
    cmd_proceso = subprocess.Popen('gnome-terminal -- python3 WebsocketServer/Server.py',shell=True)

def EnableClient():
    
    cmd_proceso = subprocess.run('bash -c "conda deactivate; python -V"', shell=True)



if __name__ == '__main__':
    Server = Thread(target=main)
    GUI = Thread(target= open)
    AMR = Thread(target= origin)

    
    Server.start()
    GUI.start()
    sleep(0.5)
    AMR.start()