import requests
import dotenv
import os


#Loads file containing the environment variables with secrets
dotenv.load_dotenv()

url = "https://discord.com/api/v10/applications/784584686965227562/commands"

json = {
    "name": "help",
    "type": 1,
    "description": "Post help for a specific command",
    "options": [
        {
            "name": "command",
            "description": "the command you need help with",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "joinQueue",
                    "value": "queue"
                },
                {
                    "name": "leaveQueue",
                    "value": "leave"
                }
            ]
        }
    ]
}

headers = {
    "Authorization": "Bot Nzg0NTg0Njg2OTY1MjI3NTYy.GdYBYR.4mz5bdfQcJmoZh2lnOmIkVzKK5Xd3NoOCjco8k"
}

r = requests.post(url, headers=headers, json=json)
print("Finished")