#!/usr/bin/env python
import json
import os
import pprint

import dateutil.parser
import jinja2

HOST_PATH = os.getcwd()
TEMPLATE_FILE = 'resume.j2'
JSON_RESUME = os.path.join(HOST_PATH, 'resume.json')
HTML_OUTPUT_FILE = os.path.join(HOST_PATH, 'test.html')


def _date_format(date):
    """Format ISO date into Month YEAR."""
    parsed = dateutil.parser.parse(date)
    return parsed.strftime('%B %Y')


def main():
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader([HOST_PATH]))

    environment.filters['date'] = _date_format

    template = environment.get_template(TEMPLATE_FILE)

    with open(JSON_RESUME) as json_handle:
        with open(HTML_OUTPUT_FILE, 'w') as output_handle:
            output_handle.write(
                template.render(json.loads(json_handle.read())))


if __name__ == '__main__':
    main()
