# Domain monitor discord bot

This Discord bot is designed to monitor your Discord channel for messages containing links to any specified domains. When such a message is detected, it will promptly notify all channel members. Additionally, you have the option to receive notifications for verification purposes or any other reasons you may have.

The bot will also issue alerts in cases where a user attempts to modify or delete their own message or tamper with the alert message itself.

### Important Note
Please be aware that this bot was created as a joke, and its design and functionality reflect this intent.

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

    

