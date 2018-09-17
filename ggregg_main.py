import discord
from discord.ext import commands
import random

with open('../secrets.txt') as f:
    authcode = f.read()[:-1]

grg = commands.Bot(command_prefix='!',
                discription='ggregg will(might)...(wont) tell you the weather',)

@grg.event
async def on_ready():
    print('logged as '+str(grg.user.name))
    print('id '+str(grg.user.id))
    print('-'*10)


@grg.command()
async def dotell(ctx):
    weather = random.randint(0,4)
    if weather == 1:    
        await ctx.send('sunny!  #gooutside')
    if weather == 2:
        await ctx.send('''clouds n' stuff''')
    if weather == 3:
        await ctx.send('v. windy #headforshelter')
    if weather == 4:
        await ctx.send('its raiiining #sticktogamin')
    if weather > 4 or weather < 1:
        await ctx.send('''i'm broken :( sorwyy''')


@grg.command()
async def info(ctx):
    embed = discord.Embed(title='ggregg', description='will..might tell weather',
                            color=0xeee657)
    embed.add_field(name='Author', value='third-meow')
    embed.add_field(name='Command', value='$dotell')
    embed.add_field(name='Server count', value=str(len(grg.guilds)))
 
    await ctx.send(embed=embed)


grg.run(authcode)
