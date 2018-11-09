from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.accept()

        self.rooms = set()

    async def receive_json(self, content, **kwargs):
        command = content.get("command", None)
        try:
            if command == "json":
                await self.join_room(content["room"])
            elif command == "leave":
                await self.leave_room(content["room"])
            elif command == "send":
                await self.send_room(content["room"], content["message"])
        except Exception as err:
            await self.send_json({"error": err})

    async def disconnect(self, code):
        for room_id in list(self.rooms):
            try:
                await self.leave_room(room_id)
            except Exception:
                pass

    # async def join_room(self, room_id):
    #     room = await