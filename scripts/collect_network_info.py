import json
import csv
from scapy.all import ARP, Ether, srp


def scan_network(network_range: str):
    """Scan the given network range using ARP requests.

    Args:
        network_range: CIDR notation of network, e.g., "192.168.1.0/24".

    Returns:
        List of dictionaries with keys: ip, mac.
    """
    result = []
    # Create ARP request
    arp = ARP(pdst=network_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    answered, _ = srp(packet, timeout=2, verbose=False)

    for sent, received in answered:
        result.append({"ip": received.psrc, "mac": received.hwsrc})
    return result


def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def save_csv(data, path):
    if not data:
        return
    keys = data[0].keys()
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Network device scanner")
    parser.add_argument('--range', required=True, help='Network range in CIDR, e.g., 192.168.1.0/24')
    parser.add_argument('--output', required=True, help='Output file path (json or csv)')
    args = parser.parse_args()

    devices = scan_network(args.range)
    if args.output.endswith('.json'):
        save_json(devices, args.output)
    elif args.output.endswith('.csv'):
        save_csv(devices, args.output)
    else:
        raise ValueError('Output file must end with .json or .csv')

    print(f"Saved {len(devices)} devices to {args.output}")


if __name__ == '__main__':
    main()
