import face_recognition
import cv2
from keras.models import load_model
import numpy as np
from faunadb import query as q
from faunadb.client import FaunaClient

# Loading the emotion recognition model
emotion_model = load_model('emotion_recognition_model.h5')


def initialize_camera():
    cap = cv2.VideoCapture(0)
    # Setting desired properties for the camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Setting width to 640 pixels
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Setting height to 480 pixels
    cap.set(cv2.CAP_PROP_FPS, 30)  # Setting frame rate to 30 frames per second

    return cap


def get_user_details():
    client = FaunaClient(secret="enter your secret code")

    indexdata = client.query(
        q.map_(
            lambda ref: q.get(ref),
            q.paginate(q.match(q.index('userii')))
        )
    )

    user_details = [entry['data'] for entry in indexdata['data']]

    known_face_encodings = []
    known_face_names = []

    for user_detail in user_details:
        user_image = user_detail.get("image")
        user_name = user_detail.get("name")

        user_face_encodings = face_recognition.face_encodings(face_recognition.load_image_file(user_image))[0]
        known_face_encodings.append(user_face_encodings)
        known_face_names.append(user_name)

    return known_face_encodings, known_face_names


def get_emotion_name(emotion_label):
    emotion_mapping = {
        0: "Angry",
        1: "Disgust",
        2: "Fear",
        3: "Happy",
        4: "Sad",
        5: "Surprise",
        6: "Neutral"
    }
    return emotion_mapping.get(emotion_label, "Unknown")


def process_frame(frame, known_face_encodings, known_face_names):
    # Resizing the frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for i, face_encoding in enumerate(face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if any(matches):
            best_match_index = np.argmin(face_recognition.face_distance(known_face_encodings, face_encoding))
            name = known_face_names[best_match_index]

        # Scaling the face locations back to the original frame size
        top, right, bottom, left = [coordinate * 4 for coordinate in face_locations[i]]

        # Extracting the face region for emotion prediction
        face_img = frame[top:bottom, left:right]
        face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
        face_img = cv2.resize(face_img, (48, 48))
        face_img = np.expand_dims(face_img, axis=0)
        face_img = face_img / 255.0

        emotion_probs = emotion_model.predict(face_img)
        emotion_label = np.argmax(emotion_probs)
        emotion_name = get_emotion_name(emotion_label)

        # Drawing bounding box and text on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, f'Name: {name}', (left, bottom + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, f'Emotion: {emotion_name}', (left, bottom + 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()


def main():
    cap = initialize_camera()
    known_face_encodings, known_face_names = get_user_details()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        process_frame(frame, known_face_encodings, known_face_names)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    release_camera(cap)


if __name__ == "__main__":
    main()