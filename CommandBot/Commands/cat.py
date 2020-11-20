from Commands import PrefixedCommand

cat = ""
cat += "/\ /\ \n"
cat += "| 0 0 | \n"
cat += "__|   Y   |__ Meow!"

class Cat(PrefixedCommand.PrefixedCommand):
    def __init__(self, bot):
        super().__init__(bot, "cat")

    async def execute(self, message):
        await message.channel.send(cat);
