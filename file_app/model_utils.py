from tensorflow import keras
import tensorflow as tf
import numpy as np

def load_model_fruit():
    try:
        print(f"loading model PlantAI_Model_Fruit_EfficientNetB0.h5")
        return keras.models.load_model('assets/PlantAI_Model_Fruit_EfficientNetB0.h5')
    except Exception as e:
        raise Exception("Failed to load fruit model: " + str(e))

def load_model_leaf(model_name):
    try:
        print(f"loading model {model_name}___Leaf.h5")
        return keras.models.load_model(f'Models/{model_name}___Leaf.h5')
    except Exception as e:
        raise Exception("Failed to load leaf model: " + str(e))

def load_classes_fruit():
    try:
        print(f"loading fruit classes")
        with open('assets/classes.txt', 'r') as f:
            class_names = f.read().splitlines()
        return class_names
    except Exception as e:
        raise Exception("Failed to load fruit classes: " + str(e))

def load_classes_leaf(classes_name):
    try:
        print(f"loading classe {classes_name}___Leaf.h5")
        with open(f'Classes/{classes_name}___Classes.txt', 'r') as f:
            class_names = f.read().splitlines()
        return class_names
    except Exception as e:
        raise Exception("Failed to load leaf classes: " + str(e))

def load_prep(img_path):
    try:
        print(f"loading image")
        img = tf.io.read_file(img_path)
        img = tf.image.decode_image(img)
        img = tf.image.resize(img, size=(224, 224))
        return img
    except Exception as e:
        raise Exception("Failed to load and preprocess image: " + str(e))


def make_prediction(model, image, classes):
    try:
        print(f"making prediction")
        pred = model.predict(tf.expand_dims(image, axis=0))
        pred_idx = np.argmax(pred)
        predicted_value = classes[pred_idx]
        return predicted_value
    except Exception as e:
        raise Exception("Failed to make prediction: " + str(e))


def make_prediction_3(model, image, classes):
    try:
        print(f"making prediction")
        pred = model.predict(tf.expand_dims(image, axis=0))
        pred_idx = np.argsort(-pred)[0][:3]
        predicted_value = [classes[i] for i in pred_idx]
        return predicted_value
    except Exception as e:
        raise Exception("Failed to make top 3 predictions: " + str(e))
