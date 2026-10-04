from fastapi import FastAPI

from sneppx_hub.index import ModelIndex

app = FastAPI(title="sneppx-hub")
index = ModelIndex()


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/v1/models")
def list_models():
    return {"models": index.list()}


@app.post("/v1/models")
def add(name: str, uri: str, signed: bool = True):
    return index.add(name, uri, signed=signed)


def create_app():
    return app
