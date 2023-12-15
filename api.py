import uuid
from datetime import datetime

import dill
import fastapi
import pandas as pd
from fastapi.responses import JSONResponse
from sklearn.ensemble import RandomForestClassifier

service_desc = "API for demonstrating a machine learning model"
app = fastapi.FastAPI(description=service_desc)

with open("model.bin", mode="rb") as f:
    model: RandomForestClassifier = dill.load(f)

responses = {
    "SUCCESS": {
        "status": "SUCCESS_DETERMINING_FLOWER",
        "message": "Successfully determined the type of flower",
    },
    "ERROR": {
        "status": "ERROR_RETRIEVING_DATA",
        "message": "There was an error retrieving data to determine the type of flower",
    },
}


@app.get("/get_flower")
def get_flower(
    sepal_length: str, sepal_width: str, petal_length: str, petal_width: str
):
    """Determines the type of flower."""

    sepal_length = float(sepal_length)
    sepal_width = float(sepal_width)
    petal_length = float(petal_length)
    petal_width = float(petal_width)

    try:
        X = pd.DataFrame(
            {
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width,
            },
            index=[0],
        )

        pred = model.predict(X=X)[0]

        data = {
            "id": uuid.uuid4().hex,
            "flower": pred,
            **X.to_dict(orient="records")[0],
            "created_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        }

        payload = {"data": data, **responses.get("SUCCESS")}

        return JSONResponse(content=payload, status_code=200)

    except Exception as e:
        print(e)
        data = {"flower": None}
        payload = {"data": data, **responses.get("ERROR")}

        return JSONResponse(content=payload, status_code=400)
