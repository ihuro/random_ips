import hug
from tabulate import tabulate

OUTPUT_JSON = "json"
OUTPUT_HTML = "html"
OUTPUT_TEXT = "text"

SUPPORTED_OUTPUTS = [
    OUTPUT_JSON,
    OUTPUT_HTML,
    OUTPUT_TEXT,
]


def get_current_output(response):
    content_type = response.content_type if response else ""

    if content_type == hug.output_format.json.content_type:
        return OUTPUT_JSON

    if content_type == hug.output_format.html.content_type:
        return OUTPUT_HTML

    return OUTPUT_TEXT


def output_json(ips):
    """Returns a dict to output the IP Addresses as JSON"""
    headers = ips[0]
    ips = ips[1:]
    return [dict(zip(headers, map(str, items))) for items in ips]


def output_tabulate(ips, format=OUTPUT_TEXT):
    return tabulate(
        ips,
        headers="firstrow",
        tablefmt=format,
    )


def output_html(ips):
    return output_tabulate(ips, OUTPUT_HTML)


def output_text(ips):
    return output_tabulate(ips)