# Facial and Emotion Recognition | Python Project

## Project Description

This project implements a facial recognition system combined with an emotion recognition system using Python. It employs a Convolutional Neural Network (CNN) to detect faces and classify emotions based on various facial characteristics, such as eyes, lips, and eyebrows. The model is trained using the FER2013 dataset to recognize seven emotions: neutrality, happiness, surprise, fear, sadness, anger, and disgust. Additionally, it leverages FaunaDB to manage a database of users, storing their names and associated face images. The project also includes a simple graphical user interface (GUI) for adding and deleting users, as well as running the facial and emotion recognition process in real time using a webcam.

## Requirements

- **Python 3.11.x** is required to run this project.

## Setup Instructions

Follow these steps to set up and run the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/deans2000/Facial-and-Emotion-Recognition-Python-Project.git
    cd Facial-and-Emotion-Recognition-Python-Project
    ```

2. Create a virtual environment:
    ```bash
    python -m venv myvenv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        myvenv\Scripts\Activate
        ```
    - On macOS/Linux:
        ```bash
        source myvenv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Download the FER2013 dataset (fer2023.csv) from Kaggle and place it in the root directory of the project:
    - Download link: [FER2013 Dataset](https://www.kaggle.com/datasets/nicolejyt/facialexpressionrecognition)

6. Train the emotion recognition model:
    ```bash
    python train_model_h5.py
    ```
    This will create the `emotion_recognition_model.h5` file in the root directory.

7. Set up FaunaDB:
    - Create a FaunaDB database to store the users.
    - Add two columns: one for the user's name and one for the associated image (e.g., `john.jpg`).
    - Generate a secret key from FaunaDB and replace the placeholder `your secret code here` in the code with your actual secret key.

8. Add images to the root folder:
    - Save an image of yourself in the root directory and name it following the pattern (e.g., `john.jpg`).

## Running the Project

1. To add users to the FaunaDB:
    - Run the GUI:
        ```bash
        python gui.py
        ```
    - Press the **Add User** button, input the name of the user and the name of their associated image (e.g., `john.jpg`).

2. To delete users:
    - Use the **Delete User** button, input the name of the user to be removed from the database.

3. To run the facial and emotion recognition:
    - Press the **Run Code** button to start the recognition process.
    - Ensure you have a functional webcam, and the system will detect faces and display the recognized user's name along with their emotion.

## Features

- **Facial Recognition**: Recognizes the identity of individuals stored in FaunaDB.
- **Emotion Recognition**: Detects basic emotions such as happiness, sadness, surprise, etc.
- **Graphical User Interface**: Provides an easy-to-use interface with buttons to add, delete, and run the facial and emotion recognition system.
