import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    GROUP = 'lobby'

    async def connect(self):
        await self.channel_layer.group_add(self.GROUP, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.GROUP, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Send to ALL clients in the group
        await self.channel_layer.group_send(self.GROUP, {
            'type': 'chat.message',
            'message': data['message'],
        })

    async def chat_message(self, event):
        await self.send(json.dumps({'message': event['message']}))