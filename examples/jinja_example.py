from jinja2 import Template

template = """
{% for interface in interfaces %}
interface {{ interface.name }}
 description {{ interface.description }}
 ip address {{ interface.ip_address }} {{ interface.subnet_mask }}
 no shutdown
{% endfor %}
"""

interfaces = [
    {
        "name": "FastEthernet1/1",
        "description": "Development",
        "ip_address": "192.168.1.1",
        "subnet_mask": "255.255.255.0",
    },
    {
        "name": "FastEthernet1/2",
        "description": "Sales",
        "ip_address": "192.168.2.1",
        "subnet_mask": "255.255.255.0",
    },
]

j2 = Template(template)
print(j2.render(interfaces=interfaces))
