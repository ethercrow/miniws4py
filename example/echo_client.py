# -*- coding: utf-8 -*-
from miniws4py.client import WebSocketBaseClient

class EchoClient(WebSocketBaseClient):
    def opened(self):
        def data_provider():
            for i in range(1, 200, 25):
                yield "#" * i
                
        self.send(data_provider())

        for i in range(0, 200, 25):
            print(i)
            self.send("*" * i)

    def closed(self, code, reason):
        print(("Closed down", code, reason))

    def received_message(self, m):
        print("=> %d %s" % (len(m), str(m)))
        if len(m) == 175:
            self.close(reason='Bye bye')

if __name__ == '__main__':
    try:
        ws = EchoClient('ws://echo.websocket.org')
        ws.daemon = False
        ws.connect()
        ws.run()
    except KeyboardInterrupt:
        ws.close()
