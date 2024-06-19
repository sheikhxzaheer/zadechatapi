from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(
            text_data="helooloo"
        )
    
    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        message = text_data
        self.send(
            text_data=f"Message received: {message}"
        )
    