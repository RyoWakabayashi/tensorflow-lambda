# coding: utf-8

import os

from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2

os.makedirs("sam/classifier/models", exist_ok=True)

model = MobileNetV2(weights="imagenet")
model.save("sam/classifier/models/model.h5", include_optimizer=False)
