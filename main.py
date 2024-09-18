import discord
from discord.ext import commands
from discord import app_commands
import random

id_do_servidor = discord.Object(id=673361670894125089) # Id do servidor SULDOES

class MeuClient(discord.Client):
    def __init__(self,*,intents:discord.Intents):
        super().__init__(intents=intents,aplication_id=1285963925694709904)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=id_do_servidor)
        await self.tree.sync(guild=id_do_servidor)
    
client = MeuClient(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Bot Online!')

# COMMANDS

@client.tree.command()
async def ola(interaction: discord.Interaction):
    await interaction.response.send_message("Olá Ricardo Lima ")

@client.tree.command()
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Titulo legal do Embed",
        description="Descrição completa",
        colour=14707394,
    )

    embed.set_author(name="Autor", icon_url="https://www.google.com/imgres?q=roronoa%20zoro%20one%20zoro%20com%20haki&imgurl=https%3A%2F%2Fwww.dexerto.com%2Fcdn-image%2Fwp-content%2Fuploads%2F2024%2F07%2F05%2Fone-piece-zoro.jpg%3Fwidth%3D3840%26quality%3D60%26format%3Dauto&imgrefurl=https%3A%2F%2Fwww.dexerto.com%2Fanime%2Fone-piece-clears-one-misconception-about-zoro-2809668%2F&docid=DPgBauuDwUMmUM&tbnid=Zkdnca4uwlVsTM&vet=12ahUKEwjW9Zawgc2IAxXRppUCHTbMPN8QM3oECGgQAA..i&w=1600&h=900&hcb=2&ved=2ahUKEwjW9Zawgc2IAxXRppUCHTbMPN8QM3oECGgQAA")
    embed.set_thumbnail(url="https://www.google.com/imgres?q=roronoa%20zoro%20one%20zoro%20com%20haki&imgurl=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FF6dk8lXWkAAaEWy.jpg%3Alarge&imgrefurl=https%3A%2F%2Ftwitter.com%2FOnePieceNewsASL%2Fstatus%2F1704441977830314085&docid=S-JOrd_RZ_W8aM&tbnid=xQzM2AxOOlc-zM&vet=12ahUKEwjW9Zawgc2IAxXRppUCHTbMPN8QM3oECB8QAA..i&w=1600&h=900&hcb=2&ved=2ahUKEwjW9Zawgc2IAxXRppUCHTbMPN8QM3oECB8QAA")
    embed.set_image(url="https://www.google.com/imgres?q=roronoa%20zoro%20one%20zoro%20com%20haki&imgurl=https%3A%2F%2Fuploads.jovemnerd.com.br%2Fwp-content%2Fuploads%2F2024%2F02%2Fzoro_one_piece__122h6r.jpg%3Fims%3D1210x544%2Ffilters%3Aquality(75)&imgrefurl=https%3A%2F%2Fjovemnerd.com.br%2Fnoticias%2Fanimes-e-mangas%2Ftudo-sobre-zoro-one-piece-historia-poderes-e-mais&docid=sVGJRl6i21a84M&tbnid=92wyH0YM-ZJ77M&vet=12ahUKEwjW9Zawgc2IAxXRppUCHTbMPN8QM3oECGcQAA..i&w=1210&h=544&hcb=2&ved=2ahUKEwjW9Zawgc2IAxXRppUCHTbMPN8QM3oECGcQAA")
    embed.set_footer(text="Esse é o Footer")
    embed.add_field(name="Nome 1", value="Campo 1",inline=False)
    embed.add_field(name="Nome 2", value="Campo 2",inline=False)
    embed.add_field(name="Nome 3", value="Campo 3",inline=False)
    await interaction.response.send_message(embed=embed)

@client.tree.command()
async def dado(interaction: discord.Interaction):
    numero = random.randint(1,6)
    
    await interaction.response.send_message(f"Voce rolou o dado e caiu no {numero} !!!")

@client.tree.command()
async def usuario(interaction: discord.Interaction,usuario: discord.User):
    
    await interaction.response.send_message(
      usuario.name
    )

client.run("MTI4NTk2MzkyNTY5NDcwOTkwNA.GUI8RH.eoc8gxFEKj3ZydzbGehmzZupMK_TjJv2HFX358")
