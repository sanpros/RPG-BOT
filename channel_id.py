import os
from dotenv import load_dotenv
load_dotenv()


class ChannelId:
    def __init__(self):
        self.GENERAL_ID = int(os.getenv('GENERAL_ID'))
        self.TEST_RPG_BOT_ID = int(os.getenv('TEST_RPG_BOT_ID'))
        self.TEST_MSG_CHANNEL = int(os.getenv('TEST_MSG_CHANNEL'))
