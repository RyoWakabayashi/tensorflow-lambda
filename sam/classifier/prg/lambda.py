# coding: utf-8

"""
メインモジュール
"""

import base64
import json
import logging
import traceback
from datetime import datetime
from io import BytesIO

import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import (
    decode_predictions,
    preprocess_input,
)
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

MODEL_PATH = "/opt/ml/model/model.h5"
model = load_model(MODEL_PATH, compile=False)


def lambda_handler(event, context):
    """画像分類応答"""

    try:

        begin_time = datetime.now()

        img = Image.open(BytesIO(base64.b64decode(event["body"])))
        img = img.resize((224, 224))
        img = img_to_array(img)
        img = img[tf.newaxis, ...]
        img = preprocess_input(img)

        predictions = model.predict(img)
        predictions = decode_predictions(predictions, top=3)
        predictions = list(
            map(
                lambda prediction: {
                    "class": prediction[1],
                    "score": float(prediction[2]),
                },
                predictions[0],
            )
        )
        predictions = list(
            filter(
                lambda prediction: prediction["score"] > 0.3,
                predictions,
            )
        )

        logger.info("Elapsed time: %s", datetime.now() - begin_time)

        return {
            "statusCode": 200,
            "body": json.dumps({"success": True, "predictions": predictions}),
        }

    except Exception:  # pylint: disable=broad-except
        traceback.print_exc()
        return {
            "statusCode": 500,
            "body": json.dumps({"success": False}),
        }
