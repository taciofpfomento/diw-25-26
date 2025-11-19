from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/{adjetivo}")
def read_root(adjetivo: str):
    index = f"""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prueba API</title>
  <link rel="stylesheet" href="css/style.css">
</head>

<body>
  HOLA MUNDO {adjetivo}
</body>

</html>
"""

    return HTMLResponse(index)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
