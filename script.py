from telethon import TelegramClient, events
import requests

# Configuration Telegram
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = 'your_phone_number'
target_channel = 'your_target_channel'

# Configuration Discord Webhook
DISCORD_WEBHOOK_URL = "your_webhook_url"

def send_to_discord(content):
    embed = {
        "embeds": [
            {
                "description": content,
                "color": 5814783
            }
        ]
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=embed)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'envoi sur Discord : {e}")

async def handler(event):
    try:
        message = event.message.message
        if message:
            print(f"Nouveau message : {message}")
            send_to_discord(message)
    except Exception as e:
        print(f"Erreur lors du traitement du message : {e}")

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("Client Telegram démarré. Résolution du canal...")
    try:
        target_channel_entity = await client.get_entity(target_channel)
        print(f"Canal trouvé : {target_channel_entity.title}")
        client.add_event_handler(handler, events.NewMessage(chats=target_channel_entity))
        print("En attente des messages...")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Erreur lors de la résolution du canal : {e}")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
