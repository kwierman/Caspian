# -*- coding: utf-8 -*-

import click
import logging
import uvicorn
from query.api import app
from dask.distributed import Client

from caspian import logger


@click.group()
def cli():
    logging.basicConfig(level=logging.INFO)

@cli.command()
@click.option('-d', '--debug/--no-debug', default=False, help='Run with Debug Logging')
@click.option('-s', '--scheduler', default='localhost:8786', help='Scheduler IP Address')
def run_server(debug, scheduler):
    """ Runs the API server for this instance of Caspian

    Args:
        debug (_type_): _description_
        scheduler (_type_): _description_
    """
    app_instance = app(scheduler)
    uvicorn.run(app_instance)

@cli.command()
def etl():
    ...
    
@cli.command('location', help='The Datalake location URI')
def query_server():
    ...

@cli.command()
@click.argument('location', help='The Datalake location URI')
def declare(location):
    ...

@cli.command()
@click.argument('location', help='The Datalake location URI')
def describe(location):
    ...

if __name__ == "__main__":
    cli()
