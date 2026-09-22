import discord
from discord.ext import commands

from pipeline import run_pipeline

# from apscheduler.schedulers.asyncio import AsyncIOScheduler  # TODO: uncomment when wiring up scheduling


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        # TODO: wire up automatic scheduled runs once manual !check works well.
        # Example shape (posts to a fixed channel on a schedule instead of on-demand):
        #
        # self.scheduler = AsyncIOScheduler()
        # self.scheduler.add_job(self.scheduled_check, "interval", hours=1)
        # self.scheduler.start()
        #
        # async def scheduled_check(self):
        #     channel = self.bot.get_channel(YOUR_CHANNEL_ID)  # TODO: per-server channel mapping
        #     new_items = run_pipeline()
        #     for item in new_items:
        #         await channel.send(embed=self._build_embed(item))

    @commands.command(name="check")
    async def check(self, ctx: commands.Context):
        """Manually trigger a pipeline run and post any new items."""
        await ctx.send("Checking for new items...")

        new_items = run_pipeline()

        if not new_items:
            await ctx.send("No new items found.")
            return

        for item in new_items:
            await ctx.send(embed=self._build_embed(item))

    def _build_embed(self, item) -> discord.Embed:
        embed = discord.Embed(title=item.title, url=item.url)
        embed.set_footer(text=item.source)
        return embed


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
