import discord
from bs4 import BeautifulSoup
import requests

token = "your_token"
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!help'))


@client.event
async def on_message(message):

    if message.content.find("$") != -1:
        try:
            crypto_coin = message.content.replace("$", "")
            url = requests.get(f'https://www.coindesk.com/price/{crypto_coin}').text
            soup = BeautifulSoup(url, 'lxml')
            name = soup.find('div', class_='coin-title').h2.text
            price = soup.find('div', class_='price-large').text
            change = soup.find('div', class_='percent-change-medium').text
            coin_name = soup.find('span', class_='coin-iso').text
            ath = soup.find('div', class_='price-small').text
            marketcap = soup.find('div', class_='price-medium').text
            print(price)
        except AttributeError:
            await message.channel.send("This Crypto currency doesn't exist.")



        embed = discord.Embed(title=name + " | " + coin_name, description="", colour=discord.Colour.gold())
        embed.add_field(name="Price", value=price, inline=False)
        embed.add_field(name="Price Change in 24h", value=change, inline=False)
        embed.add_field(name="Market Cap", value=marketcap, inline=False)
        embed.add_field(name="All Time High", value=ath, inline=False)
        embed.set_footer(text="Created by Perkzen#2079")
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/771284501522284594/800330704143253524/aug-1-header-pic.png")
        await message.channel.send(content=None, embed=embed)


    if message.content == "!help":
        embed = discord.Embed(title="BOT commands", description="", colour=discord.Colour.gold())
        embed.add_field(name="$CryptoValute", value="Lists all information about the cryptocurrency.", inline=False)
        embed.add_field(name="Examples", value="$bitcoin \n $bitcoin-cash \n  $ethereum \n $dogecoin", inline=False)
        embed.set_footer(text="Created by Perkzen#2079")
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/771284501522284594/800330704143253524/aug-1-header-pic.png")
        await message.channel.send(content=None, embed=embed)


client.run(token)
