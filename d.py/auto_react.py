import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="#")
channel_emojies = {}
TOKEN = ''

@bot.event
async def on_ready():
    print("Booted!")

@bot.group()
async def channel(ctx):
    if ctx.invoked_subcommand is None:
        await bot.reply('Invalid sub command passed...')

@channel.group(aliases=["autoreact"])
async def channel_autoreact_1(ctx):
    if ctx.invoked_subcommand is None:
        await bot.reply('Invalid sub command passed...')

@channel_autoreact_1(.command(name='add')
async def channel_autoreact_add_1(ctx, *, emo: discord.Emoji=None):
    if not emo:
        await ctx.reply('Invalid role(s)')
        return
    if isinstance(emo, discord.Emoji):
        emo = [emo]
    emojies = getattr(channel_emojies, ctx.guild.id, None)
    if not emojies:
        channel_emojies[ctx.author.id] = emo
    else:
        emojies.append(*emo)
    

@channel_autoreact_1(.command(name='remove')
async def channel_autoreact_remove_1(ctx, *, emo: discord.Emoji=None):
    if isinstance(emo, str):
        if emo.starswith('all'):
            channel_emojies[ctx.author.id] = []
    if not emo:
        await ctx.reply('Invalid role(s)')
        return
    if isinstance(emo, discord.Emoji):
        emo = [emo]
    emojies = getattr(channel_emojies, ctx.guild.id, None)
    if not emojies:
       pass
    else:
        emojies.remove(*emo)

@bot.event
async def on_message(message):
    if emojies := getattr(channel_emojies, ctx.message.id, None):
        for emoji in emojies:
        await message.add_reaction(emoji)

bot.run(TOKEN)
