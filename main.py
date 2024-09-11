from src.telegramBot import TelegramBot
from src.data.driveBot import driveBot
from dotenv import load_dotenv
import os

load_dotenv()


bot = TelegramBot()
bot.start()




