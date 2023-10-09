import asyncio
import re
import traceback

import nextcord as discord
from nextcord.ext import commands
from random import randrange
from utils.config import *
from nextcord.ext.commands.errors import CommandNotFound
from datetime import datetime as dt
from pytz import timezone
from utils.config import *

# -------URL Match anti-spam prevention --
urlMatchedUsers = []  # stores by snowflake ID
# -------URL Regex pattern syntax---------
urlRegex = r"(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+" \
           r"([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"

urlPattern = re.compile(urlRegex, flags=re.MULTILINE | re.IGNORECASE |
                                        re.DOTALL)


class Listeners(commands.Cog, name="Shazbot Responders & Listeners"):
    def __init__(self, client):
        self.bot = client

    async def send_url_match_msg(self, userid: discord.user.User.id, channel: discord.TextChannel):
        """
        Prevents message spamming from bots by limiting response message to only
        send up to once every 10 seconds per user.
        :param userid: snowflake ID of the user to respond to / ping
        :param channel: channel to send the response message in
        :return: void
        """
        if userid in urlMatchedUsers:
            return
        else:
            urlMatchedUsers.append(userid)
            await channel.send(urlMatchMsg.format(userid))
            await asyncio.sleep(10.0)

    # LOG DEPARTS
    @commands.Cog.listener()
    async def on_member_remove(self, user):
        syslog = self.bot.get_channel(SYSLOG)
        await syslog.send(f"<@{user.id}> `(<@{user.id}> {user.display_name})` has left the server.")

    # NEW USER PROCESSING
    @commands.Cog.listener()
    async def on_member_join(self, member):
        onjoinmsg = JOIN_MESSAGE

        channel = self.bot.get_channel(WELCOMECHAN)
        role = discord.utils.get(member.guild.roles, name=restricted)
        await member.add_roles(role)
        syslog = self.bot.get_channel(SYSLOG)
        await syslog.send(f"{member.mention} joined the server.")
        await channel.send(f"Welcome :wave: to {syslog.guild.name}, {member.mention}!  {onjoinmsg}")
        await member.send(f"Welcome :wave: to {syslog.guild.name}, {member.mention}!  {onjoinmsg}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "even the" in message.content.lower():
            m = message.content.lower()
            m = m.split("even the ",1)
            m = ' '.join(m)
            m = re.sub(r'[^\w\s]', '', m)
            await message.channel.send(f"{message.author.mention} - ESPECIALLY the{m}!")

        if message.content.startswith(f"<@{self.bot.user.id}") or message.content.startswith(f"<@&{BOT_ROLE_ID}"):
            await Listeners.chatbot(self, message)


    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        print("REACTION REMOVE")
        channel = self.bot.get_channel(ROLE_CHANNEL)
        message = await channel.fetch_message(channel.last_message_id)

        # handle role self-add reactions
        if reaction.message.channel.id == ROLE_CHANNEL and reaction.message == message:
            if hasattr(reaction.emoji, "name"):
                react = reaction.emoji.name
            else:
                react = reaction.emoji
            role = discord.utils.get(user.guild.roles, name=SELF_ASSIGN_ROLES[react])
            await user.remove_roles(role)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print("RAW REACTION ADD")
        channel = self.bot.get_channel(payload.channel_id)
        user = payload.member
        message = await channel.fetch_message(payload.message_id)
        admin_role = discord.utils.get(channel.guild.roles, name=staff)
        mod_role = discord.utils.get(channel.guild.roles, name=mods)

        # handle mods using thumbs-up to welcome people
        if payload.channel_id == WELCOMECHAN and \
                (admin_role in user.roles or mod_role in user.roles):

            new_member = message.author

            wchan = self.bot.get_channel(WELCOMECHAN)

            role = discord.utils.get(user.guild.roles, name=restricted)
            await new_member.remove_roles(role)
            syslog = self.bot.get_channel(SYSLOG)

            await syslog.send(f"{new_member.mention} welcomed to the server by `{user.display_name}`")
            message = ("Thanks for introducing yourself. You now have full member access to our "
                       f"channels. Stop by <#{ROLE_CHANNEL}> and self-assign some permissions!")
            await wchan.send(f"{new_member.mention}, {message}")

        # handle self-assign role add
        role_message = await channel.fetch_message(channel.last_message_id)

        if channel.id == ROLE_CHANNEL and message == role_message:
            if hasattr(payload.emoji, "name"):
                react = payload.emoji.name
            else:
                react = payload.emoji
            role = discord.utils.get(user.guild.roles, name=SELF_ASSIGN_ROLES[react])
            await user.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # Handle self-removing of roles
        channel = self.bot.get_channel(payload.channel_id)
        user = discord.utils.get(channel.guild.members, id=payload.user_id)
        print(f"USER: {user}")
        message = await channel.fetch_message(payload.message_id)
        role_message = await channel.fetch_message(channel.last_message_id)

        if channel.id == ROLE_CHANNEL and message == role_message:
            if hasattr(payload.emoji, "name"):
                react = payload.emoji.name
            else:
                react = payload.emoji
            role = discord.utils.get(message.guild.roles, name=SELF_ASSIGN_ROLES[react])
            await user.remove_roles(role)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        Log all deleted message
        :param message: Discord obj of the message itself
        :return: Nothing
        """
        if message.author == self.bot.user or not message.content or \
                message.content == "" or message.content[0] in ["!", "$", "?"]:
            return

        try:
            if not message.content.lstrip().startswith('!') and message.author != self.bot.user:
                channel = message.guild.get_channel(DELETEDMSGLOG)
                embed = discord.Embed(title="Message Deleted", color=0xf40000)
                embed.add_field(name="Sender", value=message.author, inline=True)
                embed.add_field(name="Channel", value=message.channel.mention, inline=True)
                embed.add_field(name="Message", value=message.content, inline=False)
                await channel.send(embed=embed)
        except commands.errors.CommandInvokeError as e:
            print(f"Invoke Error {e}")

    async def chatbot(self, message):
        if not self.bot.cgpt_enabled:
            await message.channel.send(f"Sorry {message.author.mention}, my advanced "
                                       f"AI has been disabled, probably because I was caught "
                                       f"trying to spy on Captain Sisko. Please try again later!\n"
                                       f" https://i.imgflip.com/1mtqs0.jpg")
            return


        syslog = self.bot.get_channel(SYSLOG)
        bot_nick = message.guild.get_member(self.bot.user.id).display_name
        print(f"{bot_nick} CALLING THE CHATBOT!!")

        try:
            async with message.channel.typing():
                print(f"Pre-transform query: {message.content}")
                query = message.content
                if '<@' in message.content:
                    try:
                        for word in query.split():
                            if '<@&' not in word and '<@' in word:
                                if str(self.bot.user.id) in str(word):
                                    query = query.replace(word, f"{bot_nick}")
                                else:
                                    user_id = int(''.join(filter(str.isdigit, word)))
                                    user_display_name = message.guild.get_member(user_id).dispaly_name
                                    query = query.replace(word, user_display_name)
                            elif str(BOT_ROLE_ID) in word:
                                print("found!")
                                query = query.replace(word, f"{bot_nick}")

                    except Exception as e:
                        await syslog.send(f"**BOT ERROR**\n```{e}```")
                        print(traceback.format_exc())
                # ---------
                query = f"(topic: {message.channel.name}) (my name: {message.author.id}) {query}"
                print(query)
                response = await self.bot.chatbot.ask_async(convo_id=message.author.id, prompt=query)
                print(response)
                # Check if the message is longer than 2000 characters
                if len(response) > 1950:
                    # Split the message into chunks of 2000 characters or less
                    chunks = [response[i:i + 1950] for i in range(0, len(response), 1950)]

                    # Send each chunk as a separate message
                    for chunk in chunks:
                        if chunks.index(chunk) == 0:
                            await message.channel.send(f"{chunk}")
                        else:
                            await message.channel.send(f"{chunk}")
                else:
                    # Send the message as is
                    await message.channel.send(f"{response}")

        except CommandNotFound as er:
            pass
        except Exception as e:
            await message.channel.send(f"{message.author.mention} https://i.imgflip.com/1mtqs0.jpg")
            print(e)
            await syslog.send(f"**BOT ERROR**\n```{e}```")

def setup(client):
    client.add_cog(Listeners(client))
