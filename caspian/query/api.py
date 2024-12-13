from fastapi import FastAPI
from typing import Union


def app(scheduler: str = None):
    """Build and return an App instance for the query API

    Args:
        scheduler (str, optional): IP Address of the persistant scheduler to run on. Defaults to None.

    Returns:
        FastAPI: the FastAPI app to run
    """
    app = FastAPI()

    # Here we go

    # TODO: list locations in the datalake

    # TODO: Describe Each Location within the datalake

    # TODO: Provide Basic Queries within the datalake

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

    return app
