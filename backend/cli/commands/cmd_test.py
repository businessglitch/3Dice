import subprocess
import os
import click

@click.command()
@click.argument('path', default=os.path.join('backend','tests'))

def cli(path):
    """
    Run a test coverage report
    Args:
        path (str): test coverage path
        :return: Subprocess call result
    """

    cmd = 'py.test {0}'.format(path)

    return subprocess.call(cmd, shell=True)