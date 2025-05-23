import re
from os import getenv
from pathlib import Path

from dotenv import load_dotenv


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
    в виде {"Gi0/0": "Tatooine", "Gi0/1": "Coruscant"...}
    """
    regex = re.compile(r"(Gi[0-9]/[0-9])\s+\S+\s+\S+\s+(\S+)", re.MULTILINE)
    interfaces = regex.findall(interfaces)
    return dict(interfaces)


def parse_vlan_brief(vlans):
    """
    Парсит VLANs и возвращает список кортежей с информацией о них в виде
    [("10", "management", "Gi1/3"), ("30", "luke_skywalker", "Gi0/1, Gi0/3")...]
    """
    regex = re.compile(
        r"(\d+)\s+(\S+)\s+\S+\s+((?:Gi[0-9]/[0-9](?:, )?)+)?", re.MULTILINE
    )
    vlans = regex.findall(vlans)
    return vlans


def prepare_data(data):
    """
    Подготавливает данные для вывода на страницу
    """
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
