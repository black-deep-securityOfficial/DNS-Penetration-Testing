# dns_enumeration.py
import dns.resolver

def resolve_records(domain):
    records = {}
    types = ['A', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
    for rtype in types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [r.to_text() for r in answers]
        except:
            records[rtype] = []
    return records