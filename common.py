import re
from dotenv import load_dotenv
from os import getenv
from pathlib import Path


def get_auth(value):
    """
    Сначала пробуем выгрузить переменную окружения из файла auth.env,
    потом берет ее из переменной окружения (если файл отсутствует - игнорируется)
    """
    load_dotenv(Path(__file__).parent / "auth.env")
    var = getenv(value)
    if not var:
        raise Exception(f"Missing environment variable: {value}")
    return var


def parse_interface_description(interfaces):
    """
    Парсит description интерфейсов и возвращает словарь с информацией о них
    в виде {"Gi0/0": "Tatooine"...}
    """
    regex = re.compile(r"(Gi[0-9]/[0-9])\s+\S+\s+\S+\s+(\S+)", re.MULTILINE)
    interfaces = regex.findall(interfaces)
    return dict(interfaces)


def parse_vlan_brief(vlans):
    """
    Парсит VLANs и возвращает список кортежей с информацией о них в виде
    [('1', 'default', 'Gi0/2')]
    """
    regex = re.compile(r"(\d+)\s+(\S+)\s+\S+\s+((?:Gi[0-9]/[0-9](?:, )?)+)?", re.MULTILINE)
    vlans = regex.findall(vlans)
    return vlans


def prepare_data(data):
    """
    Подготавливает данные для вывода на страницу
    """
    # data["switch"], data["interfaces"], data["vlans"]
    for iface, description in data["interfaces"].items():
        for vlan in data["vlans"]:
            if iface in vlan[2]:
                current_vlan = vlan[0]
                break
        data["interfaces"][iface] = {
            "description": description,
            "current_vlan": current_vlan,
        }
    return data
