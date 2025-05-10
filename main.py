# main.py
# Entry point for DNS Penetration Pro Toolkit

from modules import dns_enumeration, zone_transfer, subdomain_bruteforce, reverse_lookup
import json, csv, logging

logging.basicConfig(filename='output/scan.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def export_results(results, domain):
    with open(f"output/results.json", "w") as jf:
        json.dump(results, jf, indent=4)
    with open(f"output/results.csv", "w") as cf:
        writer = csv.writer(cf)
        writer.writerow(["Type", "Value"])
        for key, values in results.items():
            for v in values:
                writer.writerow([key, v])

def main():
    domain = input("Enter target domain: ").strip()
    cidr = input("Enter CIDR range (optional): ").strip()
    wordlist = "data/subdomains.txt"

    results = {}
    results["dns_records"] = dns_enumeration.resolve_records(domain)
    results["zone_transfer"] = zone_transfer.attempt_zone_transfer(domain)
    results["subdomains"] = subdomain_bruteforce.brute_force(domain, wordlist)

    if cidr:
        results["reverse_lookup"] = reverse_lookup.lookup_range(cidr)

    export_results(results, domain)
    print("Scan complete. Results saved to output/")

if __name__ == "__main__":
    main()