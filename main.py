import discord
from discord.ext import commands
from dotenv import load_dotenv
from WeatherFetch import message_reply
import os

load_dotenv()

BOT_TOKEN = os.getenv('TOKEN')

description = """
A bot that pulls weather data from a weather API, and from the results,
recommends the clothes for someone planning to take a vacation.
"""

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="?", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if message.author.bot:
        return  # Do not reply to other bots

    await message.reply(embed=message_reply(message))

if __name__ == '__main__':
    bot.run(BOT_TOKEN)
