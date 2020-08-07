import subprocess

import click

@click.command()
@click.option('--skip-init/--no-skip-init', default=True,
            help='Skip __init__.py files?')
@click.argument('path', default='backend')

def cli(skip_init, path):
    """
    Run a test coverage report
    Args:
        path (str): test coverage path
        :return: Subprocess call result
    """
    flake8_flag_skip = ''

    if skip_init:
        flake8_flag_skip = ' --exclude __init__.py'


    cmd = 'flake8 {0}{1}'.format(path, skip_init)

    return subprocess.call(cmd, shell=True)