import click


@click.group()
def cli():
    """Task Manager CLI — manage your tasks from the terminal."""
    pass


if __name__ == "__main__":
    cli()
