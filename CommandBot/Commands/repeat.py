from Commands import command

#Example Command

class Repeat(command.Command):
    def __init__(self):
        super().__init__("repeat")

    async def execute(self, message):
        await message.channel.send(message.content)
