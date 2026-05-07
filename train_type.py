import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# SETTINGS
IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 15

# PATH (KEEP THIS EXACT)
train_dir = "C:/Anemia_Detection_Project/dataset_type/train"
val_dir   = "C:/Anemia_Detection_Project/dataset_type/validation"

# ✅ DATA AUGMENTATION (IMPORTANT FOR REAL MODEL)
train_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

val_gen = ImageDataGenerator(rescale=1./255)

train_data = train_gen.flow_from_directory(
    train_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

val_data = val_gen.flow_from_directory(
    val_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# ✅ IMPROVED MODEL (ANTI-OVERFITTING)
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
    layers.MaxPooling2D(),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),   # 🔥 IMPORTANT
    layers.Dense(3, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# TRAIN
model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

# SAVE
model.save("type_model.h5")

print("✅ REAL TYPE MODEL TRAINED")