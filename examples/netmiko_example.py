from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "cisco-sw",
    "username": "cisco",
    "password": "cisco",
}

connection = ConnectHandler(**device)
output = connection.send_command("show version")
print(output)
connection.disconnect()
# Или через менеджер контекста
with ConnectHandler(**device) as connection:
    output = connection.send_command("show version")
    print(output)
