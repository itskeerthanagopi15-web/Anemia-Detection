import tensorflow as tf

# -------- EYE MODEL --------
eye_model = tf.keras.models.load_model("eye_model.h5")

converter_eye = tf.lite.TFLiteConverter.from_keras_model(eye_model)
converter_eye.optimizations = [tf.lite.Optimize.DEFAULT]

eye_tflite = converter_eye.convert()

with open("eye_model.tflite", "wb") as f:
    f.write(eye_tflite)

print("Eye model converted!")


# -------- PALM MODEL --------
palm_model = tf.keras.models.load_model("palm_model.h5")

converter_palm = tf.lite.TFLiteConverter.from_keras_model(palm_model)

palm_tflite = converter_palm.convert()

with open("palm_model.tflite", "wb") as f:
    f.write(palm_tflite)

print("Palm model converted!")


# -------- NAIL MODEL --------
nail_model = tf.keras.models.load_model("nail_model.h5")

converter_nail = tf.lite.TFLiteConverter.from_keras_model(nail_model)

nail_tflite = converter_nail.convert()

with open("nail_model.tflite", "wb") as f:
    f.write(nail_tflite)

print("Nail model converted!")

print("All models converted successfully!")