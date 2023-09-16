import discord
import re
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

domains = os.getenv('DOMAINS')
thread_name = os.getenv('THREAD_NAME')
your_user_id = int(os.getenv('YOUR_USER_ID') or 0)
token = os.getenv('TOKEN')

def is_url_from_domain(message):
    words = message.split()

    for word in words:
        # Check if the word is a valid URL
        parsed_url = urlparse(word)
        if parsed_url.netloc:
            # Extract the domain from the URL
            url_domain = parsed_url.netloc
            # Check if the domain matches any of the specified domains
            if any(part in url_domain for part in (domains or [])):
                return True

    # Return False if no matching URL is found
    return False

# Create or find a thread channel when the bot joins a server
async def create_or_find_thread(guild):
    existing_thread = discord.utils.get(guild.text_channels, name=thread_name)
    if not existing_thread:
        existing_thread = await guild.create_text_channel(name=thread_name)
    return existing_thread

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
# Create or find a thread channel when the bot joins a server
async def on_guild_join(guild):
    await create_or_find_thread(guild)

# Delete the thread channel when the bot leaves a server
@client.event
async def on_guild_remove(guild):
    existing_thread = discord.utils.get(guild.text_channels, name=thread_name)
    if existing_thread:
        try:
            await existing_thread.delete()
            print(f'Deleted thread "{thread_name}" in guild: {guild.name}')
        except discord.Forbidden:
            print(f'Bot does not have permission to delete thread "{thread_name}" in guild: {guild.name}')
        except discord.HTTPException as e:
            print(f'An error occurred while deleting thread "{thread_name}" in guild: {guild.name}\nError: {e}')

# Handle incoming messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    author = message.author.display_name
    tag_string = "@everyone"

    if is_url_from_domain(message.content):
        thread = await create_or_find_thread(message.guild)

        await thread.send(f'{author} jäit kiinni!: {message.content} \n\n {tag_string}\n')

        user = await client.fetch_user(your_user_id)
        if user:
            await user.send(f'{message.author.display_name} tried to delete a message in server "{message.guild.name}": {message.content}')


# Handle deleted messages
@client.event
async def on_message_delete(message):
    tag_string = "@everyone"
    author = message.author.display_name
    thread = await create_or_find_thread(message.guild)

    if message.author.bot:
        original_sender_name = message.content.split()[0]
        await thread.send(f'{original_sender_name} yritti poistaa sen viestin!: {message.content}')

    elif is_url_from_domain(message.content):
        await thread.send(f'{author} yritti poistaa sen viestin!: {message.content} \n\n {tag_string}\n')

    user = await client.fetch_user(your_user_id)
    if user:
        await user.send(f'{author} tried to delete message in server "{message.guild.name}": {message.content}')

# Handle edited messages
@client.event
async def on_message_edit(original_message, new_message):
    if new_message.id == original_message.id:
        return

    tag_string = "@everyone"
    author = new_message.author.display_name
    thread = await create_or_find_thread(new_message.guild)

    if not thread:
        thread = await new_message.guild.create_text_channel(thread_name)

    if new_message.author.bot:
        original_sender_name = original_message.content.split()[0]
        await thread.send(f'{original_sender_name} yritti muokata sen viestiä!: {original_message.content}')
    elif is_url_from_domain(original_message.content):
        await thread.send(f'{author} yritti muokata sen viestiä!: {original_message.content} \n\n{tag_string}')

    user = await client.fetch_user(your_user_id)
    if user:
        await user.send(f'{new_message.author.display_name} tried to edit old message the in server "{new_message.guild.name}": {original_message.content}')

if token:
    client.run(token)
else:
    print("No token found.")

