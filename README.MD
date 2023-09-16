# Domain monitor discord bot

## Description

This is a simple discord bot that monitors your discord channel for messages that contains any links to the given domains. It alerts everyone on the channel if the message contains a link to any of the specified domains. Optionally, you can also send messages to you for proof or whatever.

It also alerts if the user tries to edit or delete their own message, or if they try to tinker with the alert message itself. 

### Note
This bot was made as a joke and I dont think it has any practical use cases.

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python packages by running:

   ```shell
   pip install -r requirements.txt

3. Set up a Discord bot and get its token. You can follow Discord's official guide for creating a bot and obtaining the token.

4. Create a .env file in the project directory and add the following environment variables:

   ```shell
    DOMAINS=["foo.com", "bar.com"]
    THREAD_NAME=thread_name_for_the_bot
    YOUR_USER_ID=your_discord_user_id
    TOKEN=your_discord_bot_token

## Usage

1. Run the bot by executing:

   ```python
   python discord_bot.py

The bot will log in and start monitoring your Discord server.

2. Customize the bot's behavior by adjusting the environment variables and code as needed.

    

