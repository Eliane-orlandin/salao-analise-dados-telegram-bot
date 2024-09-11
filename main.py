from src.telegramBot import TelegramBot
from src.driveBot import driveBot
from dotenv import load_dotenv
import os

#bot = TelegramBot()
#bot.start()
load_dotenv()

# Initialize the Drive Bot class
driveBot = driveBot()

# Get the data from the Google Drive
drive_data = driveBot.get_data()

# Print the data for demonstration purposes
print(f"Data retrieved: {drive_data}")
print(drive_data)
