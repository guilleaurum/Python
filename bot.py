import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def contraseña(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def gato(ctx):
    await ctx.send('Adoro los gatos')
    await ctx.send('Me encantan los gatos')

@bot.command()
async def repite(ctx, times: int, content='Gatos'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def perro(ctx):
    await ctx.send('Solo quiero a los gatos')

@bot.command()
async def mem(ctx):
    with open('Meme\Imagen\006a00af-c8c5-46f6-b56f-794e17d1b485.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("Token")
