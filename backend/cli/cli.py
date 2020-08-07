import os
import click

cmd_folder = os.path.join(os.path.dirname(__file__), 'commands')
cmd_prefix = 'cmd_'

@click.command()
@click.option('--skip-init/--no-skip-init', default=True,
            help='Skip __init__.py files?')
@click.argument('path', default='backend')


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        """
        Obtain list of all the available commands

        Args:
            ctx (object): Click context
            :return: List of sorted commands
        """

        commands = []

        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith(cmd_prefix):
                commands.append(filename[4:-3])

        commmands.sort()

        return commands
    
    def get_commands(self, ctx, name):

        """
        Get a specific command by looking up the module

        Args:
            ctx (object): Click context
            name (str): Command name

            :return: Module's cli function

        """

        ns = {}

        filename = os.path.join(cmd_folder,cmd_prefix + name + '.py')

        with open(filename) as f:
            code = compile(f.read(), filename, 'exec')
            eval(code, ns, ns)

        return ns['cli']

@click.command(cli=CLI)
def cli():
    """
    Commands to help manage the project
    """
    pass
