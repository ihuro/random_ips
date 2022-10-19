from enum import Enum
from pathlib import Path

import hug
from tabulate import tabulate


class Output(str, Enum):
    JSON = "json"
    HTML = "html"
    TEXT = "text"


def output_json(ips):
    """Returns a dict to output the IP Addresses as JSON"""
    headers = ips[0]
    ips = ips[1:]
    return [dict(zip(headers, map(str, items))) for items in ips]


def output_tabulate(ips, format=Output.TEXT):
    return tabulate(
        ips,
        headers="firstrow",
        tablefmt=format,
    )


def _get_html_template():
    filename = 'table.html'
    tempalte_path = Path(filename)
    if not tempalte_path.exists():
        tempalte_path = Path(f"random_ips/{filename}")

    if tempalte_path.is_file():
        return tempalte_path.read_text()

    raise Exception(f"Cannot find HTML template file: {filename}")


def output_html(ips):
    table = (
        output_tabulate(ips, Output.HTML)
        .replace(
            "<table>", "<table class='table table-striped table-bordered table-hover'>"
        )
        .replace("<thead>", "<thead class='table-dark'>")
    )
    template = _get_html_template()
    return template.replace("{{ table }}", table)


def output_text(ips):
    return output_tabulate(ips)


MAP_OUTPUT_FUNCTION = {
    Output.JSON: output_json,
    Output.HTML: output_html,
    Output.TEXT: output_text,
}

MAP_HUG_CONTENT_TYPE_TO_OUTPUT = {
    hug.output_format.json.content_type: Output.JSON,
    hug.output_format.html.content_type: Output.HTML,
}


def get_request_output(response):
    content_type = response.content_type if response else ""

    output = MAP_HUG_CONTENT_TYPE_TO_OUTPUT.get(content_type, Output.TEXT)

    return MAP_OUTPUT_FUNCTION.get(output, output_text)
