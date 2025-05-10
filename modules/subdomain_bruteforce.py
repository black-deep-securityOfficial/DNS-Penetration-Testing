# subdomain_bruteforce.py
import socket

def brute_force(domain, wordlist):
    found = []
    try:
        with open(wordlist, 'r') as f:
            for line in f:
                sub = line.strip()
                fqdn = f"{sub}.{domain}"
                try:
                    ip = socket.gethostbyname(fqdn)
                    found.append(f"{fqdn} -> {ip}")
                except:
                    continue
    except:
        pass
    return found