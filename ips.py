"""Generate Random IP addresses

This script will generate random IP addresses and get related network information.

Usage:
  ips [--quantity=<qty>]

Options:
  -h, --help        Show this help message
  --quantity=<qty>  Amount of IP addresses to generate [default: 5].
"""
from ipaddress import IPv4Address
from random import (
    getrandbits,
    randint,
)

import hug
from ipcalc import IP
from tabulate import tabulate


@hug.local()
def generate_random_ips(quantity: hug.types.number = 5):
    """
    Return a listo random IP addresses.

    Params:
        quantity (int): amount of IP to generate

    Returns:
        list: list of addresses and network information
              ["IP", "Network", "Netmask Decimal", "Netmask Bits", "Broadcast", "Host min", "Host max"]
    """
    ips = [
        # Headers
        ["IP", "Network", "Netmask Decimal", "Netmask Bits", "Broadcast", "Host min", "Host max"]
    ]

    for _ in range(quantity):
        # Random IP
        raw_ip = IPv4Address(getrandbits(32))
        # Random MASK
        raw_mask = randint(1, 32)

        # Build IP Network and store the related information
        ipv4 = IP(f"{raw_ip}/{raw_mask}")
        network = ipv4.guess_network()
        ips.append([
            ipv4,
            network.network(),
            network.netmask(),
            network.subnet(),
            network.broadcast(),
            network.host_first(),
            network.host_last()
        ])

    return ips


@hug.cli()
@hug.get('/random_ips', output=hug.output_format.text)
@hug.get('/random_ips/{quantity}', output=hug.output_format.text)
def generate(quantity: hug.types.number = 5):
    """
    Main script logic
    """
    ip_addresses = generate_random_ips(quantity)
    ips_table = tabulate(
        ip_addresses,
        headers="firstrow"
    )

    return ips_table


if __name__ == '__main__':
    generate.interface.cli()
