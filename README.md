# Telegram to Discord Message Relay Bot
=====================================

This project is a bot that relays messages from a Telegram channel to a Discord webhook. It uses the Python library `Telethon` to connect to Telegram and the `requests` module to send messages to Discord.

* * * * *

Steps for Configuration and Usage
---------------------------------

### 1\. Clone this project

Download or clone this project to your local directory.

### 2\. Install dependencies

Make sure Python is installed, then install the required libraries with the following command:

```
pip install telethon requests
```

### 3\. Get your Telegram API credentials

-   Log in to your Telegram account at <https://my.telegram.org/apps>.

-   Create a new application or select an existing one.

-   Note down the following two values:

    -   **API ID**

    -   **API Hash**

### 4\. Get the link or ID of the target channel

-   If you are using an invitation link, copy it and paste it into the `target_channel` variable in the script.

-   **Example:** For a link like `https://t.me/examplechannel`, use `'examplechannel'` in the `target_channel` variable.

### 5\. Create a Discord Webhook

-   Log in to your Discord server.

-   Go to the settings of the channel where you want to receive messages.

-   Under the **Integrations** tab, create a webhook.

-   Copy the URL of your webhook and replace it in the `DISCORD_WEBHOOK_URL` variable.

### 6\. Configure the script variables

Replace the values in the script with your personal and secure information:

-   `api_id`: Replace with the API ID you obtained.

-   `api_hash`: Replace with the API Hash you obtained.

-   `phone_number`: Enter the phone number associated with your Telegram account.\
    ⚠️ **Don't forget to replace** `**+33**` **with your country code.** For example:

    -   France: `+33`

    -   Belgium: `+32`

    -   Canada: `+1`

-   `target_channel`: Enter the ID or username of the target Telegram channel.

-   `DISCORD_WEBHOOK_URL`: Enter your Discord webhook URL.

**Example:**

```
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = '+33xxxxxxxxx'  # Replace +33 with your country code
target_channel = 'examplechannel'
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/xxxx/yyyy"
```

### 7\. Run the script

Start the bot by running the Python script:

```
python script.py
```

### 8\. Secure your data

-   Never share sensitive information (like `api_id`, `api_hash`, or `DISCORD_WEBHOOK_URL`) publicly.

-   Use environment variables for enhanced security if you plan to deploy this project.

* * * * *
