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
    generate_random_ips,
)
from output import (
    OUTPUT_HTML,
    OUTPUT_JSON,
    get_current_output,
    output_html,
    output_json,
    output_text
)


@hug.cli()
@hug.get('/random_ips', output=hug.output_format.html)
@hug.get('/random_ips/json', output=hug.output_format.pretty_json)
@hug.get('/random_ips/{quantity}', output=hug.output_format.html)
@hug.get('/random_ips/{quantity}/json', output=hug.output_format.pretty_json)
def generate(response = None, quantity: hug.types.number = DEFAULT_QUANTITY):
    """
    Main script logic
    """
    output = get_current_output(response)
    ip_addresses = generate_random_ips(quantity)

    if output == OUTPUT_JSON:
        return output_json(ip_addresses)

    if output == OUTPUT_HTML:
        return output_html(ip_addresses)

    return output_text(ip_addresses)


if __name__ == '__main__':
    generate.interface.cli()
