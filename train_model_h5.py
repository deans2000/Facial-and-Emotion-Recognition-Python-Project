import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.utils import to_categorical

# Step 1: Loading and Preprocess the FER2013 Dataset
# Note: The FER2013 dataset CSV file is needed. It can be downloaded from Kaggle or other sources.

data = pd.read_csv('fer2013.csv')

# Extracting pixels and labels
pixels = data['pixels'].tolist()
labels = data['emotion']

# Converting pixels to numpy array
pixels = [np.fromstring(pixel, dtype=int, sep=' ').reshape((48, 48, 1)) for pixel in pixels]
pixels = np.stack(pixels, axis=0)

# Convert labels to one-hot encoding
labels = to_categorical(labels, num_classes=7)

# Normalizing pixel values
pixels = pixels / 255.0

# Step 2: Defining the CNN Model Architecture
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(48, 48, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(7, activation='softmax')
])

# Step 3: Compiling the Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 4: Training the Model
model.fit(pixels, labels, epochs=10, batch_size=32, validation_split=0.2)

# Step 5: Saving the Trained Model
model.save('emotion_recognition_model.h5')
