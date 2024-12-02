import os
import shutil
import requests
import json
from dotenv import load_dotenv

# Specify the path to your .env file
load_dotenv(dotenv_path='./.env')

def send_notification(message):
    webhook_url = os.getenv('MATTERMOST_WEBHOOK_URL')

    if not webhook_url:
        print("Error: MATTERMOST_WEBHOOK_URL environment variable is not set.")
        return

    payload = {
        "text": message
    }

    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            print('Notification sent successfully!')
        else:
            print(f'Failed to send notification: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'Error sending notification: {e}')

def check_disk_usage(threshold=50):
    total, used, free = shutil.disk_usage("/")


    used_percentage = (used / total) * 100

    print(f'Disk Usage: {used_percentage:.2f}%')

    if used_percentage > threshold:
        message = f'Alert: Disk usage is at {used_percentage:.2f}%, which exceeds the {threshold}% threshold.'
        send_notification(message)

def main():
    check_disk_usage()

if __name__ == '__main__':
    main()
