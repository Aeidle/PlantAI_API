# model_loader.py

from tensorflow import keras
import tensorflow as tf
import numpy as np

def load_model_fruit():
    try:
        return keras.models.load_model('Models/PlantAI_Model_Fruit_EfficientNetB0.h5')
    except Exception as e:
        print("Error loading fruit model:", str(e))
        return None

def load_model_leaf(model_name):
    try:
        return keras.models.load_model(f'Models/{model_name}___Leaf.h5')
    except Exception as e:
        print("Error loading leaf model:", str(e))
        return None

def load_classes_fruit():
    try:
        with open('Classes/Classes.txt', 'r') as f:
            class_names = f.read().splitlines()
        return class_names
    except Exception as e:
        print("Error loading fruit classes:", str(e))
        return None

def load_classes_leaf(classes_name):
    try:
        with open(f'Classes/{classes_name}___Classes.txt', 'r') as f:
            class_names = f.read().splitlines()
        return class_names
    except Exception as e:
        print("Error loading leaf classes:", str(e))
        return None
