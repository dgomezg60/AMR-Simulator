import asyncio
from threading import Thread
import websockets
import json

class Server(object):
    __instance = None

    async def authenticate(self,FirstMessage,client):
        message = json.loads(FirstMessage)
        if message['Token'] == "59":
            authenticated = True
            self.ClientAuthorised[message['ID']] = client
            #print('Client {} authenticated'.format(message['ID']))
        else:
            authenticated = False
        if authenticated:

            return True
        else:
            return False

    async def disconect(self,client):
        await client.close()
        print(f'Client disconected {client.id}')
        try:
            _ = self.ClientAuthorised.pop(list(self.ClientAuthorised.keys())[list(self.ClientAuthorised.values()).index(client)])
        except ValueError:
            pass

    ##-------------------------------------------------------------------Server listen----------------------------------------------------------------------------------------------
    ##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def read_message(self,client):
        text = await client.recv()
        message = json.loads(text)
        print("ID:{}, Position: {}".format(message['IDRobot'],message['Position']))

    async def server_handler_listen(self,client):
        authenticated = False
        auth_message = await client.recv()
        authenticated = await self.authenticate(auth_message,client)
        if authenticated:
            try:
                print(f'Client conected {client.id} to Listening Server')
                while True:
                    await self.read_message(client)
            except websockets.exceptions.ConnectionClosed:
                print('Server listening')
                await self.disconect(client)
        else:
            await client.close()

    ##-------------------------------------------------------------------Server send----------------------------------------------------------------------------------------------
    ##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def send_message(self,Id):
        
        try:
            client = self.ClientAuthorised[f'{Id}']
            struct = r'{{"IDRobot":"{}","Position":[10,20,60]}}'
            message = struct.format(Id)
            print('Envio mensaje a {} mensaje:{}'.format(client,message))
            await client.send(message)
        except KeyError:
            print(f'Cliend with ID {Id} doesnt exist')
        except websockets.exceptions.ConnectionClosedOK:
            print(f'Client with ID {Id} disconnect')

    async def server_handler_send(self,client):
        authenticated = False
        auth_message = await client.recv()
        authenticated = await self.authenticate(auth_message,client)  
        if authenticated:
            print(f'Client conected {client.id} to Sender Server')
            await asyncio.Event().wait()
        else:
            await client.close()

    ##------------------------------------------------------------------- Main ----------------------------------------------------------------------------------------------
    ##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def obj(self):
        await self.server.wait_closed()

    def between_callback(self):
        asyncio.run(self.obj)

    async def start_server(self):
        ListeningServer = await websockets.serve(self.server_handler_listen, 'localhost', self.Ports[1])
        print(f'Listening server turn on, at localhost:{self.Ports[1]}')
        self.server = await websockets.serve(self.server_handler_send, 'localhost', self.Ports[0])
        print(f'Sending server turn on, at localhost:{self.Ports[0]}')
        
        await ListeningServer.wait_closed()
        _thread = Thread(target=self.between_callback)
        _thread.start()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Server,cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if(self.__initialized): return
        self.__initialized = True
        self.ClientAuthorised = {}
        self.Ports = [8768,8769]
        try:
            asyncio.run(self.start_server())
        except KeyboardInterrupt:
            print('\nServer turn off')
        except TimeoutError:
            print('\nDisconect out of time')


def main():
    ServerObj = Server()
    
if __name__ == '__main__':
    ServerObj = Server()