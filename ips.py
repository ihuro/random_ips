"""
Function to generate random IP addresses
"""
from ipaddress import IPv4Address
from random import (
    getrandbits,
    randint,
)

from ipcalc import IP


def generate_random_ips(quantity: int = 5) -> list:
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
