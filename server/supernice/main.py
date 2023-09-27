#!/usr/bin/env python

from fastapi import FastAPI

from .infrastructure.apis.main import test

app = FastAPI()


@app.get("/")
def read_root():
    print(test)
    return {"Hello": "World"}
