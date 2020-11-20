from Commands import PrefixedCommand

#Example Command

class Repeat(PrefixedCommand.PrefixedCommand):
    def __init__(self):
        super().__init__("repeat")

    async def execute(self, message):
        await message.channel.send(message.content)
