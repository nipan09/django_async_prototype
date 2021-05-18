import json
from channels.generic.websocket import WebsocketConsumer

class ChatRoomConsumer(WebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_router']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name
            self.channel_name
        )
        
    def disconnect(self, close_code):
        pass