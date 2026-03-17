"""Task Manager CLI — entry point."""

import click


@click.group()
def cli():
    """A simple CLI task manager."""
    pass


if __name__ == "__main__":
    cli()
