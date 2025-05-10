# reverse_lookup.py
import ipaddress
import socket

def lookup_range(cidr):
    results = []
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        for ip in net.hosts():
            try:
                name, _, _ = socket.gethostbyaddr(str(ip))
                results.append(f"{ip} -> {name}")
            except:
                continue
    except:
        pass
    return results