import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'MTE2MDk4MTA3Nzc1NDY0MjU5Mg.GWYj0Q.0gTHDckb-NgWMgGf-21AJnN9WEFW_JJqnDxS3c'
GUILD_ID = '1160986809778569266'

# Define your intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Use !help to see available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument. Use !create_channel <channel_name>.")
    else:
        print(f"An error occurred: {error}")

@bot.command(name='create_channel', help='Create a text channel')
async def create_channel(ctx, channel_name):
    try:
        guild = bot.get_guild(int(GUILD_ID))

        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if existing_channel:
            await ctx.send(f'Channel "{channel_name}" already exists!')
        else:
            new_channel = await guild.create_text_channel(channel_name)
            await ctx.send(f'Channel "{channel_name}" created! ID: {new_channel.id}')

    except discord.Forbidden:
        await ctx.send("I don't have the required permissions to create a channel.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")

# Run the bot with the token
bot.run(TOKEN)
