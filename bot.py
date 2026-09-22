import discord
from discord.ext import commands

from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id: {bot.user.id})")


async def load_cogs():
    await bot.load_extension("cogs.commands")


async def main():
    async with bot:
        await load_cogs()
        # DISCORD_TOKEN is used here to log the bot in — see config.py / .env
        await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
