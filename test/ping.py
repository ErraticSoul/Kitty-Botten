import config

from edamino import Bot, Context, logger

bot = Bot(email=config.EMAIL, password=config.PASSWORD, prefix="/")


@bot.on_ready
async def on_ready():
    logger.info('Ready.')


@bot.command("clear")
async def clear(ctx: Context):
    await ctx.send('...', message_type=109)


@bot.command('ping')
async def echo(ctx: Context):
    await ctx.reply('Pong!')


if __name__ == '__main__':
    bot.start()
