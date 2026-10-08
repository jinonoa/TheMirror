import numpy as np
import mediapipe as mp

def detecter_visage(image):
    image_mp = mp.Image(image_format = mp.ImageFormat.SRGB, data = np.array(image))
    model_path = 'model/blaze_face_short_range.tflite'
    faceDetector = mp.tasks.vision.FaceDetector 
    with faceDetector.create_from_model_path(model_path) as detector:
        resultat = detector.detect(image_mp)
        if resultat.detections:
            visage = resultat.detections[0]
            x = visage.bounding_box.origin_x
            y = visage.bounding_box.origin_y
            largeur = visage.bounding_box.width
            hauteur = visage.bounding_box.height
            return x, y, largeur, hauteur
        else:
            return None