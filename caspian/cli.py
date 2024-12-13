# -*- coding: utf-8 -*-

import click
import logging
import uvicorn
from .query.api import app

from . import logger
from rich.logging import RichHandler

from caspian.warehouse import warehouse_factory


@click.group()
@click.option("-d", "--debug/--no-debug", default=False, help="Run with Debug Logging")
@click.option(
    "-s", "--scheduler", default="localhost:8786", help="Scheduler IP Address"
)
@click.option(
    "-w", "--warehouse", default=None, help="Location of the warehouse side of the datalake"
)
@click.pass_context
def cli(ctx, debug, scheduler, warehouse):
    """ Main Entry Point for Caspian Workflows

    Args:
        ctx (click.Context): Context to pass to other functions
        debug (bool): Whether to run Caspian with debug logging
        scheduler (str): IP Address of the dask scheduler to use
    """
    FORMAT = "%(message)s"
    level = logging.INFO
    if debug:
        level = logging.DEBUG
    logging.basicConfig(
        level=level,
        format=FORMAT,
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])],
    )
    ctx.obj["SCHEDULER"] = scheduler
    logger.info('Starting Caspian')

@cli.command()
@click.pass_context
@click.option('-h', '--host', default='0.0.0.0', help='Host Address of API Server')
@click.option('-p', '--port', default='6969', help='Host port of API Server')
def run_server(ctx, host, port):
    scheduler = ctx.obj['SCHEDULER']
    app_instance = app(scheduler)
    logger.info(f'Starting Caspian API at: {host}:{port} with scheduler: {scheduler}')
    uvicorn.run(app_instance, host=host, port=int(port))

@cli.command()
@click.pass_context
@click.option('-w', '--warehouse', default='sqlite:caspian_default.sqlite')
def setup_warehouse(ctx, warehouse):
    warehouse = warehouse_factory(warehouse)

    warehouse.initialize()


@cli.command()
def etl(): ...


@cli.command()
@click.argument("location")
def query(): ...


@cli.command()
@click.argument("location")
def declare(location): ...


@cli.command()
@click.argument("location")
def describe(location): ...


def main():
    cli(obj={})
    
if __name__ == "__main__":
    main()
