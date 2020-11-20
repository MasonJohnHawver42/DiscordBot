
# Command Bot
Commnand bot is a Discord bot that has a list of Commands it will execute when asked.
The Command Bot is initialsed by the config file; the config determines what commands are included in the bot and where the bot opperates.

# Commands
Commands are made up of two parts:
 - their call function : determines if the data should be executed on
 - their execute function : determines what todo with that data (ie store it, reply, etc)

To create a command immplement the Command class and store it in a file within the Commands folder.
  
# Config
The config file contains two things:
 - the token : this is the token for the discord api
 - a list of commands : the list contains strings that denote which implementations of the Command class should be included in the bot
    - The strigns that denote the command follow this format: [file name].[command class name] . ( make sure the file is in the Commands folder )
        - For an example look at the conjig.json file
