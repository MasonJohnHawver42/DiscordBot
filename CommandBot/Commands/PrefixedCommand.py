from Commands import Command

class PrefixedCommand(Command.Command):
    def __init__(self, prefix = "cmd" ):
        self.prefix = prefix

    async def call(self, message):
        if (message.content.split()[0] == self.prefix):
            await self.execute(message)
