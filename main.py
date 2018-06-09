import constants
import discord
import logging

from discord.ext import commands

bot = commands.Bot(command_prefix='.',
                   description='A bot created for the EXID Discord server.',
                   case_insensitive=True)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')

@bot.event
async def on_member_join(member):
    guild = member.guild
    general_channel = guild.get_channel(constants.GENERAL_CHAN_ID)
    roles = guild.roles

    await general_channel.send("Welcome {} to the server! :soLDanceGif: Remember to check out {} and {}! LEGGO!"
        .format(member.mention,
        guild.get_channel(constants.WELCOME_CHAN_ID).mention,
        guild.get_channel(constants.PICK_UR_BIAS_CHAN_ID).mention))

    for role in roles:
        if role.id == constants.LEGGO_ROLE_ID:
            await member.add_roles(role)
            break

@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(constants.GENERAL_CHAN_ID)
    await channel.send("**{}** left the server! I hate you for this, can't you feel it? :JungSad:"
        .format(member.name))

@bot.command(name='solji',
             description='Posts a random Solji pic.',
             aliases=['soulg'],
             pass_context=True)
async def solji(context):
    await context.send('Solji!')

@bot.command(name='le',
             description='Posts a random LE pic.',
             aliases=['hyojin', 'elly'],
             pass_context=True)
async def le(context):
    await context.send('LE!')

@bot.command(name='hani',
             description='Posts a random Hani pic.',
             aliases=['heeyeon'],
             pass_context=True)
async def hani(context):
    await context.send('Hani!')

@bot.command(name='hyelin',
             description='Posts a random Hyelin pic.',
             aliases=['hyerin'],
             pass_context=True)
async def hyelin(context):
    await context.send('Hyelin!')

@bot.command(name='jeonghwa',
             description='Posts a random Jeonghwa pic.',
             aliases=['junghwa'],
             pass_context=True)
async def jeonghwa(context):
    await context.send('Jeonghwa!')

bot.run(constants.TOKEN)
