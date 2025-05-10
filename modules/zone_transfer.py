# zone_transfer.py
import dns.resolver
import dns.query
import dns.zone

def attempt_zone_transfer(domain):
    results = []
    try:
        ns = dns.resolver.resolve(domain, 'NS')
        for server in ns:
            try:
                z = dns.zone.from_xfr(dns.query.xfr(server.to_text(), domain))
                for name, node in z.nodes.items():
                    results.append(f"{name}.{domain} -> {z[name].to_text(name)}")
            except:
                continue
    except:
        pass
    return results