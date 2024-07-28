import os

import discord
from dotenv import load_dotenv

import helpers

# START HERE: Instantiate Discord bot object
# Next go to the main method: `if __name__ == "__main__":`
discord_bot: discord.Bot = discord.Bot()


# ========== Lifecycle Events ==========
# Discord bot first goes to the `on_ready` method
@discord_bot.event  # Decorator that waits for events to happen in Discord
async def on_ready():
    print(f"Starting up the bot: {discord_bot.user}")


# ========== BOT COMMANDS ==========
@discord_bot.command(name="roll", description="Roll 1 or more dice")
async def roll(context: discord.ApplicationContext,
               dice_roll: discord.Option(str, description="Value of die to roll. e.g.: 1d3, 1d9, 2d21"),
               whisper: discord.Option(bool, description="Whisper the result to the user", default=False, choices=[True, False]),
               dm: discord.Option(bool, description="Direct message the user AND output to the channel", default=False,
                                  choices=[True, False])):
    """Perform the dice roll for the user. Invoked by the user when they type `/roll <d4, d12, or d20>`

    Args:
        context (discord.ApplicationContext): The discord application context. Represents the context in which a command is being invoked und
        dice_roll (discord.Option(str)): The user's input of die to roll. E.g. 1d3, 1d9, 2d21
        dm (discord.Option(bool)): Direct message the user AND output to the channel if they choose this option
        whisper (discord.Option(bool)): Whisper the result to the user if they choose this option
    """

    # Just a debug statement to see the value we've gotten the user
    print(f"Rolling arbitrary dice value: {dice_roll}")

    # Validate that user input is a valid dice roll
    if not helpers.is_valid_roll(dice_roll):
        await context.respond(f"Sorry, {dice_roll} is not supported. Please try a different roll")

    # Remove extra spaces and lowercase everything
    dice_roll = dice_roll.strip().casefold()

    # Perform the user's roll: /roll 2d10 -> [10, 8]
    roll_result: list[int] = helpers.roll_dice(dice_roll)

    # Calculate the sum of the dice roll: /roll 2d10 -> [10, 8] -> 18
    roll_sum = sum(roll_result)

    # The response message to send to the user
    response_msg = f"[{dice_roll}] = {roll_result} = {roll_sum}"

    # DM the user if they requested it
    if dm:
        calling_user = context.author
        try:
            await calling_user.send(response_msg)
        except discord.Forbidden:
            # If the user has DMs disabled, let them know
            await context.respond("I'm unable to DM you. Please check your privacy settings and try again", ephemeral=True)

    # Actually send the response message to the user in the channel
    await context.respond(response_msg, ephemeral=whisper)


# Create a simple testing command, so we that know the bot is alive and well
# Command name is the function name if not specified in the command decorator
@discord_bot.command(description="Returns a message stating the bot is alive")
async def ping(context: discord.ApplicationContext):
    """Sends the bot's latency. Invoked by the user when they type `/ping`

    Args:
        context (discord.ApplicationContext): The discord application context. Represents the context in which a command is being invoked und
    """
    response: str = """Pong!
    Howdy I'm alive! Start trying to roll dice with `/roll <VALUE_OF_DICE>` e.g. /roll 1d20"""

    # Send the response message to the user
    await context.respond(response)


# ========== END BOT COMMANDS ==========


# ========== MAIN METHOD ==========
if __name__ == "__main__":
    # Read in Environment variables from .env file
    load_dotenv()

    # Get DISCORD_TOKEN secret from environment variable
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    # Pass Discord bot token to bot and run the bot
    discord_bot.run(DISCORD_TOKEN)
