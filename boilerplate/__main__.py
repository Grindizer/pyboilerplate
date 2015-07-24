#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import click

@click.command()
def main():
    click.echo("boilerplate main command line invoked.")


if __name__ == '__main__':
    main()