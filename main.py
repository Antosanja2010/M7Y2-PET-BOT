
import discord
from discord.ext import commands
from model import detect_pet





intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
 
@bot.command()
async def check(ctx):
    attachments = ctx.message.attachments
    if attachments:
        for attachment in attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'images/{file_name}')
            
            name = detect_pet(f'images/{file_name}')
            await ctx.send(f'На картинке изображено {name}')
            

            if name == 'Cats':
                await ctx.send('Это кот дружелюбный друг челоека в египте им поклонялись как богам да и сейчас нечего не изменилось...')

            if name == 'Lizards':
                await ctx.send('Это ящерица любого вида есть как маленькие и безобидные а есть как огромный варан с человека который живет на драконьем острове там он высший хищник то есть он там самый сильный! ')
            
            if name == 'Dogs':
                await ctx.send('Это собака есть очень много разных пород от маленькой чихуахуа до огромной немецкой овчарки собаки произошли от волков и самый близкий родственик волков но в тоже время собака это порода собаки хаски любит холод и бегать!')

            if name == 'Birds':
                await ctx.send('Это птицы произошла от динозавров птицы очень красивые умные и даже большие как пеликан или умные как вороны и попугаи учатся пению они от своих сародичей так что если в дестве птенца не будет сародичей он сам придумает свою песню!')


    else:   
        await ctx.send("Вы забыли загрузить картинку")

bot.run("MTI2OTYxNDQ4MjY0MTEyOTQ5Mg.GQ2ZXA.Kao1lEKRfrp8R3gN26DS0Qi0u_UWEO5-ilnE_0")