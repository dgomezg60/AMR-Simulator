import asyncio
from threading import Thread
from time import sleep 
import websockets
import json

class client():
    def __init__(self,Identify):
        self.Id = Identify

    async def obj(self,client):
        await  self.__SendAuthenticationMessage(client)

    def between_callback(self,Obj):
        asyncio.run(self.obj(Obj))

    async def connected(self,Token):   
        try:
            self.__clientListener = await websockets.connect(f'ws://localhost:8768')
            self.__clientSender = await websockets.connect(f'ws://localhost:8769')
            self.token = Token
            ThreadListener = Thread(target= self.between_callback, args= (self.__clientListener,))
            ThreadSender = Thread(target= self.between_callback, args= (self.__clientSender,))
            ThreadListener.start()
            ThreadSender.start()
        except websockets.exceptions.ConnectionClosedError:
            print("\nConnection Error")
        except KeyboardInterrupt:
            print("\nDisconnect")

    async def __SendAuthenticationMessage(self,client):
        struct = r'{{"Token":"{}","ID":"{}"}}'
        FirstMessage = struct.format(self.token,self.Id)
        await client.send(FirstMessage)

    #async def SendParameters(self,Position,Speed,Blocked,Queued,Status,ErrorStatus,BatteryLevel):
    async def SendParameters(self):
        struct = r'{{"IDRobot":"{}","Position":[0,0,0],"Speed":50,"Blocked":true,"Queued":true,"Status":"Enty","ErrorStatus":0,"BatteryLevel":20}}'
        #struct  = r'{{"IDRobot":"{}","Position":"{}","Speed":"{}","Blocked":"{}","Queued":"{}","Status":"{}","ErrorStatus":"{}","BatteryLevel":"{}"}}'
        #message = struct.format(self.Id,Position,Speed,Blocked,Queued,Status,ErrorStatus,BatteryLevel)
        message = struct.format(self.Id)
        await self.__clientSender.send(message)
        sleep(1)
        await self.SendParameters()

    async def ListeningServer(self):
            print(self.__clientListener)
            Order = await self.__clientListener.recv()
            self.message = json.loads(Order)
            print("ID:{}, Position: {}".format(self.message['IDRobot'],self.message['Position']))
            await self.ListeningServer()

async def main(id,token):
    Amr = client(id)
    await Amr.connected(token)
    try:
        await Amr.ListeningServer()
        print('Dejo de escuchar')
        #await Amr.SendParameters()
    except KeyboardInterrupt:
        print('Disconnect')

if __name__ == '__main__':
    asyncio.run(main(0,'59'))


