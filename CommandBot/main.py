from CommandBot import *
import json
import sys

if __name__ == "__main__":

    with open(sys.argv[1]) as file:
        config = json.load(file)

    client = CommandBot(config)
    client.execute()
