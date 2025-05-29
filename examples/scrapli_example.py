from scrapli import Scrapli

device = {
    "host": "cisco-sw",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "platform": "cisco_iosxe",
    "transport": "paramiko",
}

conn = Scrapli(**device)
conn.open()
response = conn.send_command("show interface description")
print(response.result)
conn.close()
# Или через менеджер контекста
with Scrapli(**device) as conn:
    response = conn.send_command("show interface description")
    print(response.result)
