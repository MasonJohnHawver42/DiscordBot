from Commands import PrefixedCommand

#Example Command

class Repeat(PrefixedCommand.PrefixedCommand):
    def __init__(self, bot):
        super().__init__(bot, "repeat")

    async def execute(self, message):
        await message.channel.send(message.content)
