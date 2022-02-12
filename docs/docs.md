* [Examples](#example)
    * [Minimal example](#min-example)
    * [Send image](#send-image)
    * [Send gif](#send-gif)
    * [Send sticker](#send-sticker)
    * [Send embed](#send-embed)


# Min example <a id=min-example>

```py
from edamino import Bot, Context

bot = Bot('email', 'password', 'prefix')


@bot.command('ping')
async def on_ping(ctx: Context):
    await ctx.reply('Pong!')


bot.start()
```

# Send image <a id=send-image>

```py
from edamino import Bot, Context
from edamino.api import File

bot = Bot('email', 'password', 'prefix')


@bot.command('image')
async def on_image(ctx: Context):
    image = File.load('path_to_file')
    await ctx.send_image(image)

    # You can also upload an image asynchronously
    
    image = await File.async_load('path_to_file')
    await ctx.send_image(image)
    
    # You can also download yourself

    with open('path_to_file', 'rb') as file:
        image = file.read()

    await ctx.send_image(image)
    
    # You can even download an image from the internet
    
    image = await ctx.download_from_link('link_to_image')
    await ctx.send_image(image)

bot.start()
```

# Send sticker <a id=send-sticker>

```py
from edamino import Bot, Context

bot = Bot('email', 'password', 'prefix')


@bot.command('sticker')
async def on_gif(ctx: Context):
    await ctx.send_sticker('sticker id')
    
bot.start()
```

# Send embed <a id=send-embed>

```py
from edamino import Bot, Context
from edamino.api import Embed

bot = Bot('email', 'password', 'prefix')


@bot.command('embed')
async def on_embed(ctx: Context):
    await ctx.send_sticker('sticker id')
    embed = Embed(
        title=ctx.msg.author.nickname, 
        object_type=0, 
        object_id=ctx.msg.author.uid,
        content="lalala"
    )
    await ctx.send(embed=embed)
bot.start()
```