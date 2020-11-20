import discord

class CommandBot(discord.Client):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.commands = []

        for command in config["commands"]:
            componets = command.split('.')
            module = getattr(__import__("Commands." + componets[0]), componets[0])
            cmd_class = getattr(module, componets[1])
            self.commands.append(cmd_class(self))

    def add_command(self, command):
        self.commands.append(command)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        for command in self.commands:
            await command.call(message)

    def execute(self):
        self.run(self.config["token"])
