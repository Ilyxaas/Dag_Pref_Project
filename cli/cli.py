import click
from my_prefect_project import tasks
from my_dagster_project import assets

default_path_in = '/Users/ilya/HomeWork/pythonProject10/data/original.csv'
default_path_out = '/Users/ilya/HomeWork/pythonProject10/data/norm.csv'


@click.command()
@click.option('--tool', default='prefect', help='prefect/dagster.')
@click.option('--file_in', default=default_path_in, help='Original csv.')
@click.option('--file_out', default=default_path_out, help='csv with domain names.')
def cli(tool, file_in, file_out):
    if (tool == 'prefect'):
        tasks.my_flow(file_in, file_out)
    elif (tool == 'dagster'):
        assets.fix_path(file_in, file_out)
        assets.run_assets()


if __name__ == '__main__':
    cli()
