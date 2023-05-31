# model_loader.py

from tensorflow import keras
import tensorflow as tf
import numpy as np

def load_model_fruit():
    return keras.models.load_model('assets/PlantAI_Model_Fruit_EfficientNetB0.h5')

def load_model_leaf(model_name):
    return keras.models.load_model(f'Models/{model_name}___Leaf.h5')

def load_classes_fruit():
    with open('assets/classes.txt', 'r') as f:
        class_names = f.read().splitlines()
    return class_names

def load_classes_leaf(classes_name):
    with open(f'Classes/{classes_name}___Classes.txt', 'r') as f:
        class_names = f.read().splitlines()
    return class_names
