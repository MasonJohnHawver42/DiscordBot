class Command:
    def __init__(self, cmd = ""):
        self.cmd = cmd;

    async def __call__(self, message):
        print(message.content)
        if (message.content.split()[0] == self.cmd):
            await self.execute(message)

    async def execute(self, message):
        pass
