#!/usr/bin/env python
import json
import os

import click
import dateutil.parser
import jinja2


def _date_format(date):
    """Format ISO date into Month YEAR."""
    date_value = ''

    try:
        parsed = dateutil.parser.parse(date)
        date_value = parsed.strftime('%B %Y')
    except ValueError:
        date_value = date

    return date_value


@click.command()
@click.option('-o', '--output', type=click.File('wb'), default='test.html', show_default=True, help='Output filename')
@click.option(
    '-r', '--resume', type=click.File('rb'), default='resume.json', show_default=True, help='JSON resume file')
@click.option('-t', '--template', default='resume.j2', show_default=True, help='Jinja2 template file')
def main(output, resume, template):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

    environment.filters['date'] = _date_format

    template = environment.get_template(template)

    json_dict = json.loads(resume.read().decode())
    rendered = template.render(json_dict)
    output.write(rendered.encode())


if __name__ == '__main__':
    main()
