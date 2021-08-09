from discord.ext import commands, tasks
import discord
import asyncio
import logging.handlers
import logging

class DMLog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        logger = logging.getLogger("discord")
        logger.setLevel(logging.INFO)
        self.queue = asyncio.Queue(loop=self.bot.loop)
        handler = logging.handlers.QueueHandler(self.queue)
        logger.addHandler(handler)

    @commands.Cog.listener()
    async def on_ready(self):
        self.owner = (await self.bot.application_info()).owner
        await self.bot.loop.create_task(self.send_log())

    async def send_log(self):
        msg = await self.queue.get()
        embed = {
            "title" : msg.name,
            "description" : msg.message
        }
        await self.owner.send(embed = discord.Embed.from_dict(embed))
        await self.bot.loop.create_task(self.send_log())

def setup(bot):
    bot.add_cog(DMLog(bot))

