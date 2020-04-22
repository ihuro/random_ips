"""Generate Random IP addresses

This script will generate random IP addresses and get related network information.

Usage:
  ips [--quantity=<qty>]

Options:
  -h, --help        Show this help message
  --quantity=<qty>  Amount of IP addresses to generate [default: 5].
"""
from schema import (
    Schema,
    SchemaError,
    Use,
)
from docopt import docopt
from tabulate import tabulate

from ips import generate_random_ips


def main():
    """
    Main script logic
    """
    args = docopt(__doc__, version="Random IP addresses generator 1.0")

    schema = Schema({
        '--quantity': Use(int, error='--quantity=<qty> must be integer')
    })

    try:
        args = schema.validate(args)
    except SchemaError as exc:
        exit(exc)

    quantity = args.get('--quantity')
    ip_addresses = generate_random_ips(quantity)
    ips_table = tabulate(
        ip_addresses,
        headers="firstrow"
    )

    print(ips_table)


if __name__ == '__main__':
    main()
