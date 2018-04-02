# Mikey by beatbox1200, .addField("Wahh"), and Springbonnie Productions

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import aiohttp

bot = commands.Bot(command_prefix='M!')

@bot.event
async def on_ready():
    print ("BOOYAHKASHA!!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def brothers(ctx):
    await bot.say("I have 3 brothers, Leo, Raph, and Donnie.")

@bot.command(pass_context=True)
async def meow(ctx):
    await bot.say("Aww, Ice Cream Kitty, you so cute! :icecream: :cat: ")

@bot.command(pass_context=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await bot.addroles(member, role)
    await bot.say("{}, has got a BOOYAPROMOTION!".format(user.name))

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("Don't tell Leo I got into his Discord user lookup equipment... :zipper_mouth: :mask: :hushed:")
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def best_experience(ctx):
    await bot.say("The best experience for me, was when we all went to Transylvania, to stop the Savanti Romero, and Raph turned into a vampire! Haha!")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: {}, You boi, HAVE BEEN BOOYAKAKICKED!!".format(user.name))
    await bot.kick(user)

 bot.run(os.getenv('TOKEN'))
