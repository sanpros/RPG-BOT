import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from bot_message import BotMessage
from channel_id import ChannelId


print("Lancement du bot...")
load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
channel_id = ChannelId()
bot_message = BotMessage()


@bot.event
async def on_ready():
    print(bot_message.start_bot_msg(bot.user.name))
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash syncronisées: {len(synced)}")
    except Exception as e:
        print(e)


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    content = message.content.lower()

    # récupère l'objet channel pour faire un get_general.send("dans un channel choisis")
    get_general = bot.get_channel(channel_id.GENERAL_ID)
    get_test_rpg_bot = bot.get_channel(channel_id.TEST_RPG_BOT_ID)
    get_test_msg_channel = bot.get_channel(channel_id.TEST_MSG_CHANNEL)

    if content == "bonjour":
        await message.channel.send("Comment tu va ?")

    if content == "test mp":
        await message.author.send("test mp")

    if content == "test msg channel":
        if message.channel.id == channel_id.TEST_MSG_CHANNEL:
            await message.channel.send(bot_message.test_msg_channel)

    if content.startswith("!bienvenue"):
        if message.mentions:
            pseudo = message.mentions[0].display_name
            await message.channel.send(bot_message.welcome_msg(pseudo))
        else:
            await message.channel.send(bot_message.welcome_msg_failed)

    if content.startswith("!clear"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = int(content.split()[1])
                await message.channel.purge(limit=amount + 1)
            except (IndexError, ValueError):
                await message.channel.send(bot_message.clear_msg, delete_after=7.5)
        else:
            await message.channel.send(bot_message.clear_msg_failed, delete_after=7.5)


@bot.tree.command(name="commands", description="Tester les embeds")
async def commands(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Test Titre",
        description="Description de l'embed",
        color=discord.Color.blue()
        )
    embed.add_field(name="Commands", value=bot_message.all_commands_msg, inline=False)
    await interaction.response.send_message(embed=embed)


    # if content == "!commands":
    #     await message.channel.send(bot_message.all_commands_msg)


@bot.tree.command(name="test", description="Tester les embeds")
async def test(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Test Titre",
        description="Description de l'embed",
        color=discord.Color.blue()
        )
    embed.add_field(name="Python", value="Apprendre le python en s'amusant", inline=False)
    embed.add_field(name="C", value="Apprendre le C en s'amusant", inline=False)
    embed.set_footer(text="Pied de page")
    embed.set_image(url="https://share.google/3dd4mgoChEYP3S97q")
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="warnguy", description="Alerter une personne")
async def warnguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message("Alerte envoyé !", delete_after=5)
    await member.send("Tu as reçu une alerte!")


@bot.tree.command(name="banguy", description="Alerter une personne")
async def banguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message("Ban envoyé !", delete_after=5)
    await member.ban(reason="Random ban!")
    await member.send("Tu as été banni")


@bot.tree.command(name="emoji", description="Affiche ce site d'émoji")
async def emoji(interraction: discord.Interaction):
    await interraction.response.send_message(bot_message.emoji_url)


bot.run(os.getenv('DISCORD_TOKEN'))
