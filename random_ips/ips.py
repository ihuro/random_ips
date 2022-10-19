from ipaddress import IPv4Address
from random import (
    getrandbits,
    randint,
)

import hug
from ipcalc import IP

DEFAULT_QUANTITY = 5
MAX_QUANTITY = 50


@hug.local()
def generate_random_ips(quantity: hug.types.number = DEFAULT_QUANTITY):
    """
    Return a list of random IP addresses.

    Params:
        quantity (int): amount of IP to generate

    Returns:
        list: list of addresses and network information
              ["IP", "Network", "Netmask Decimal", "Netmask Bits", "Broadcast", "Host min", "Host max"]
    """
    ips = [
        # Headers
        [
            "IP",
            "Network",
            "Netmask Decimal",
            "Netmask Bits",
            "Broadcast",
            "Host min",
            "Host max",
        ]
    ]

    for _ in range(quantity):
        # Random IP
        raw_ip = IP("0.0.0.0")
        while str(raw_ip).startswith("0"):
            raw_ip = IPv4Address(getrandbits(32))

        # Random MASK
        raw_mask = randint(1, 32)

        # Build IP Network and store the related information
        ipv4 = IP(f"{raw_ip}/{raw_mask}")
        network = ipv4.guess_network()
        ips.append(
            [
                f"{ipv4}",
                f"{network.network()}",
                f"{network.netmask()}",
                f"/{network.subnet()}",
                f"{network.broadcast()}",
                f"{network.host_first()}",
                f"{network.host_last()}",
            ]
        )

    return ips
