import subprocess

import click

@click.command()
@click.argument('path', default='backend')

def cli(path):
    """
    Run a test coverage report
    Args:
        path (str): test coverage path
        :return: Subprocess call result
    """

    cmd = 'py.test --cov-report term-missing --cov {0}'.format(path)

    return subprocess.call(cmd, shell=True)