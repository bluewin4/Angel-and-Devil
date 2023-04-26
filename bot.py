import discord
from discord.ext import commands
import openai
import language_model
# Set up bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

# Load your API key from an environment variable or secret management service
openai.api_key = "your_openai_api_key_here"

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command(name="setgoal")
async def set_goal(ctx, *, goal):
    await ctx.send(f"Goal set: {goal}")

@bot.command(name="changegoal")
async def change_goal(ctx, *, new_goal):
    await ctx.send(f"Goal changed to: {new_goal}")

if __name__ == "__main__":
    # Load your discord token from an environment variable or secret management service
    discord_token = "your_discord_token_here"
    bot.run(discord_token)