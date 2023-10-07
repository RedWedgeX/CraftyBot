import nextcord
from nextcord.ext import commands
from utils.config import *
import traceback


class Extras(commands.Cog, name="Stuff for funzies"):
    def __init__(self, client):
        self.bot = client

    @commands.command(name='events')
    async def events(self, ctx):
        await ctx.send("Events!")
        async for event in ctx.guild.fetch_scheduled_events(with_users=True):
            u = event.fetch_users(with_member=True)
            print(f"Scheduled users:")
            print(event.users)

    @commands.command(hidden=True)
    @commands.has_any_role(staff)
    async def enable(self, ctx):
        async with ctx.typing():
            self.bot.cgpt_enabled = True
            await ctx.send("CraftGPT Enabled")

    @commands.command(hidden=True)
    @commands.has_any_role(staff)
    async def disable(self, ctx):
        async with ctx.typing():
            self.bot.cgpt_enabled = False
            await ctx.send("CraftGPT Disabled")


def setup(client):
    client.add_cog(Extras(client))
