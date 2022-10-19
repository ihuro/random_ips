"""Generate Random IP addresses

This script will generate random IP addresses and get related network information.

Usage:
  api [--quantity=<qty>]

Options:
  -h, --help        Show this help message
  --quantity=<qty>  Amount of IP addresses to generate [default: 5].
"""
import hug

from ips import (
    DEFAULT_QUANTITY,
    MAX_QUANTITY,
    generate_random_ips,
)
from output import get_request_output


@hug.cli()
@hug.get("/random_ips", output=hug.output_format.html)
@hug.get("/random_ips/json", output=hug.output_format.pretty_json)
@hug.get("/random_ips/{quantity}", output=hug.output_format.html)
@hug.get("/random_ips/{quantity}/json", output=hug.output_format.pretty_json)
def generate(
    response=None, quantity: hug.types.in_range(0, MAX_QUANTITY) = DEFAULT_QUANTITY
):
    """
    Main script logic
    """
    ip_addresses = generate_random_ips(quantity)
    output = get_request_output(response)
    return output(ip_addresses)


if __name__ == "__main__":
    generate.interface.cli()
