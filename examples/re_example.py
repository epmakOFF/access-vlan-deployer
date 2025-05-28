import re

data = """
          Mac Address Table
-------------------------------------------
(*)  - Security Entry     (M)  - MLAG Entry
(MO) - MLAG Output Entry  (MI) - MLAG Input Entry
(E)  - EVPN Entry         (EO) - EVPN Output Entry
(EI) - EVPN Input Entry   
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
100     e49d.73cf.f270    dynamic     eth-0-46
100     882f.6419.5f00    dynamic     eth-0-28
100     882f.641b.0000    dynamic     eth-0-30
100     5c17.8334.0ecc    dynamic     eth-0-38
100     5c17.8334.01e8    dynamic     eth-0-37
"""

for line in data.split("\n"):
    if mac_address := re.search(r"(\w{4}\.?){3}", line):
        # Например: e49d.73cf.f270
        # \w{4} - 4 символа
        # \.? - 0 или 1 точка
        # (\w{4}\.?) - группировка для блока из 4 символов и опционально точки
        # {3} - 3 раза
        print(mac_address.group())
        
        