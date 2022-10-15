import discord
import config
import random
import os
from contextlib import redirect_stdout
import io
import traceback
import textwrap
import datetime

from discord.ext import commands
from discord.ext.commands import clean_content


prefixlist = ['bread ', 'Bread ' 'b! ']

intents = discord.Intents.all()
intents.members = True 
client = commands.Bot(command_prefix=prefixlist, case_insensitive=True, intents=intents)

#starting shizziwizzie
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    channel = client.get_channel(825512698858307644)
    newmember = discord.Embed(
        title="Client Started",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Colour.green())
    newmember.add_field(
        name='User', value=str(client.user), inline=False)
    newmember.add_field(
        name='User ID', value=str(client.user.id), inline=False)
    newmember.set_thumbnail(url=client.user.avatar_url)

    await channel.send(embed=newmember)

#commands

#Pong!
@client.command(name='Ping')
async def ping(ctx):
  ping = discord.Embed(
    color = discord.Colour.green()
  )
  
  ping.add_field(name='Client Latency', value=f'```{(round(client.latency * 1000))}ms```')

  await ctx.send(embed=ping)


# ;)
@client.command(name='long',aliases=['baguette'])
async def long(ctx):
  breadcommand = discord.Embed(
    color = discord.Colour.green()
  )
  
  baguetteimg = [
    'https://upload.wikimedia.org/wikipedia/commons/f/f5/Baguettes_-_stonesoup.jpg','https://www.thespruceeats.com/thmb/kEnr3XkQOF9dV8d7b70vBtH2BXo=/3733x2800/smart/filters:no_upscale()/baguette-recipe-four-hour-bread-stangenbrot-1446523-hero-01-d5ff7ca4d8ab46b48fb4c2406bb83fde.jpg','https://www.ilovecooking.ie/wp-content/uploads/2020/01/rsz_patrick_baguettes_-final_online_hr-7344_1-scaled.jpg','https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/B10F0941-3518-440D-A69F-72EFF5F7826B/Derivates/E46B8240-C5D3-4CD4-A322-4A90FB1C851A.jpg','https://bakingamoment.com/wp-content/uploads/2019/01/IMG_2536-best-french-baguette-recipe.jpg','https://thecookstreat.com/wp-content/uploads/2019/02/FrenchBaguettes8-480x270.jpg','https://tasteofartisan.com/wp-content/uploads/2019/05/French-baguette-recipe-4.jpg','https://www.rockrecipes.com/wp-content/uploads/2010/09/DSC0529-2.jpg','https://redstaryeast.com/wp-content/uploads/2018/02/French-Baguette-72-dpi-800w.jpg','https://assets.vogue.com/photos/5c5c849abfd5ff2d9c5c53c6/master/w_2560%2Cc_limit/00-story-baguette-instagram.jpg'
  ]

  breadcommand.set_image(url=random.choice(baguetteimg))

  await ctx.send(embed=breadcommand)

# bricks for some reason? i cannot for the life of me remember why
@client.command(name='brick')
async def brick(ctx):
  breadcommand = discord.Embed(
    color = discord.Colour.green()
  )
  
  baguetteimg = [
    'http://mobileimages.lowes.com/product/converted/693092/693092000005.jpg','https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Brick.jpg/1200px-Brick.jpg','https://images-na.ssl-images-amazon.com/images/I/81klKQNXNpL._AC_SL1500_.jpg','https://images.stockx.com/products/streetwear/Supreme-Brick-Brick.jpg?fit=fill&bg=FFFFFF&w=300&h=214&auto=format,compress&q=90&dpr=2&trim=color&updated_at=1603481985','https://i1.wp.com/civilblog.org/wp-content/uploads/2015/02/How-to-check-brick-quality-on-site.jpg?resize=640%2C359&ssl=1','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAPTDC7bji16crRI1-4YVdrl0mOysKxwMZNA&usqp=CAU','https://brickhunter.ams3.digitaloceanspaces.com/production/Cortex/blog/iG0ZraQogY2bTvdRZngTlagoPnUwCpmvRuXjApHG.jpeg'
  ]

  breadcommand.set_image(url=random.choice(baguetteimg))

  await ctx.send(embed=breadcommand)

#also a simpscanner #yolo
@client.command(aliases=['simp'])
@commands.cooldown(1, 20, commands.BucketType.user)
async def simpcanner(ctx,* ,user: clean_content=None):
    """Measure someones amount of simp-ness"""

    if not user:
        user = ctx.author.name
    simpness = random.randint(0,100)
    if simpness <= 33:
        simpStatus = random.choice(["Hardly a simp", 
                                    "They know the meaning of simp", 
                                    '"Only simps sometimes"', 
                                    "simp-ish", 
                                    "No simping bro",  
                                    "Take a walk, non simp"])
        simpColor = 0xFFC0CB
    elif 33 < simpness < 66:
        simpStatus = random.choice(["Possible a simp", 
                                    "My simp-sensor is picking something up", 
                                    "Has probably looked at belle delphine", 
                                    "simp-ish", 
                                    "Looking a bit simpish if you ask me", 
                                    "lol half  s i m p", 
                                    "safely in between for now"])
        simpColor = 0xFF69B4
    else:
        simpStatus = random.choice(["LOL YOU SIMPIN XDDD FUNNY", 
                                    "SIMP ALERT", 
                                    "MY SIMP-SENSOR IS OFF THE CHARTS", 
                                    "STINKY SIMP", 
                                    "BIG SIMPER", 
                                    "THE SIMPS ARE HERE", 
                                    "HELLA SIMPIN"])
        simpColor = 0xFF00FF
    emb = discord.Embed(description=f"Simp-ness for **{user}**", color=simpColor)
    emb.add_field(name="Simp-ness:", value=f"{simpness}% simp")
    emb.add_field(name="Comment:", value=f"{simpStatus} 😩")
    emb.set_author(name="Simp-Scanner™")
    await ctx.reply(embed=emb)

ownerID = [301150214985613313]

#error handler
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        error = discord.Embed(
            title="That is not a command!",
            color=discord.Color.red(),
            description="Please see `bread help` for the commands!"
        )
        await ctx.send(embed=error, delete_after=30)
      
#runs raw code from discord chat
@client.command(hidden=True, aliases=["e"])
async def eval(ctx, *, body: str):
    raw = False
    """Evaluates a code"""

    env = {
        'client': client,
        'ctx': ctx,
        'channel': ctx.message.channel,
        'author': ctx.message.author,
        'guild': ctx.message.guild,
        'message': ctx.message,
    }
    if ctx.message.author.id in ownerID:
        env.update(globals())

        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    if raw:
                        rawembed=discord.Embed(color=discord.Colour.green())
                        rawembed.add_field(name='Input',value=f'```{ctx.message.content}```',inline=False)
                        rawembed.add_field(name='Output',value=f'```{value}```',inline=False)
                        await ctx.send(f"{value}",embed=rawembed)
                    else:
                        elseembed=discord.Embed(color=discord.Colour.green())
                        elseembed.add_field(name='**Input**',value=f'```{ctx.message.content}```',inline=False)
                        elseembed.add_field(name='**Output**',value=f'```py\n{value}\n```',inline=False)
                        await ctx.send(embed=elseembed)
            else:
                pass

#run app, see config.py
client.run(config.TOKEN)