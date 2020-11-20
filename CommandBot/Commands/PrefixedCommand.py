from Commands import Command

class PrefixedCommand(Command.Command):
    def __init__(self, bot, prefix = "cmd" ):
        super().__init__(bot)
        self.prefix = prefix

    async def call(self, message):
        if message.author == self.bot.user:
            return
            
        if (message.content.split()[0] == self.prefix):
            await self.execute(message)
