import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# Replace with your actual bot token
TOKEN = "7233884875:AAFHFBmnC91oNSkMSjPyJ53v855NA9Sn4mc"

# Enable logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Log bot start
logger.info("🚀 AI Model Developed by Dhia Djelal - Test Version. The final project is coming soon.")

# Command handler for "/start"
@dp.message(Command("start"))
async def start_command(message: Message):
    logger.info(f"✅ Received /start command from {message.from_user.id}")
    await message.answer(
        "🤖 Hello! I am an AI model developed by Dhia Djelal. "
        "This is a test version, and the final project is coming soon! \n\n"
        "📊 **How It Works:** \n"
        "1️⃣ Upload an image 📸\n"
        "2️⃣ I analyze the objects in the image using **YOLOv8** 🖼️\n"
        "3️⃣ I generate audience targeting insights for Meta (Facebook) Ads 🎯\n"
        "4️⃣ You receive recommended **audience keywords**, **product categories**, and **target demographics** 🏷️\n\n"
        "📈 **Meta Ads Insights:**\n"
        "🔹 I use AI-based object detection to suggest the best advertising audience.\n"
        "🔹 Based on detected objects, I provide relevant interests, demographics, and ad targeting parameters.\n"
        "🔹 This helps you optimize Facebook Ads for **higher engagement and conversions**.\n\n"
        "🚀 Future updates will include automated ad placement on Meta Ads!"
    )

# Reply to any message
@dp.message()
async def reply_to_all_messages(message: Message):
    logger.info(f"💬 Received a message from {message.from_user.id}: {message.text}")
    await message.answer(
        "🤖 I'm an AI model developed by Dhia Djelal! \n"
        "🚀 This is a test version, and the final project is coming soon!\n\n"
        "📊 I analyze images for Facebook Ads targeting. Send me an image to try it out! 📸"
    )

# Main function
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Start the bot
if __name__ == "__main__":
    asyncio.run(main())
