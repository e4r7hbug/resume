#!/usr/bin/env python
import json
import os

import dateutil.parser
import jinja2

import click

HOST_PATH = os.getcwd()


def _date_format(date):
    """Format ISO date into Month YEAR."""
    parsed = dateutil.parser.parse(date)
    return parsed.strftime('%B %Y')


@click.command()
@click.option('-o', '--output',
              type=click.File('wb'),
              default='test.html',
              help='Output filename')
@click.option('-r', '--resume',
              type=click.File('rb'),
              default='resume.json',
              help='JSON resume file')
@click.option('-t', '--template',
              default='resume.j2',
              help='Jinja2 template file')
def main(output, resume, template):
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader([HOST_PATH]))

    environment.filters['date'] = _date_format

    template = environment.get_template(template)

    output.write(template.render(json.loads(resume.read())))


if __name__ == '__main__':
    main()
