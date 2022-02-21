import discord
from discord.ext import commands
from utils.config import *
import traceback


class Extras(commands.Cog, name="Stuff for funzies"):
    def __init__(self, client):
        self.bot = client


def setup(client):
    client.add_cog(Extras(client))
