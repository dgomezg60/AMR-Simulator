from Algorithm.a_star import AStar
from DB.SQLLite import DB
from WebsocketServer.Server import Server
import asyncio


def LockForPath(IDRobot,EndPoint):
    db = DB()
    db.Connect()
    Amr = db.Find('AMR',f'IDAMR={IDRobot}')
    try:
        from GUI.Grafos.main import MapGraph
    except:
        quit()
    # Algorithm = AStar(MapGraph,Amr[0][2],EndPoint)
    # Path,PathLenght = Algorithm.search()
    ServerObj = Server()
    asyncio.run(ServerObj.send_message(0,EndPoint))
