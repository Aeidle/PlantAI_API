from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

import tensorflow as tf
from tensorflow import keras
import numpy as np
import json


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()

            dic_res = {}
            sub_res = {}
            path = file_serializer.data['file']
            path_mqad = path[1:]
            
            # load the fruits model
            def load_model_fruit():
                return keras.models.load_model('assets/plantai_model_adil.h5')
            # load the leafs model
            def load_model_leaf(model_name):
                return keras.models.load_model(f'Models/{model_name}___Leaf.h5')
            # load the fruit classes
            def load_classes_fruit():
                with open('assets/classes.txt', 'r') as f:
                    class_names = f.read().splitlines()
                return class_names
            # load the leaf classes
            def load_classes_leaf(classes_name):
                with open(f'Classes/{classes_name}___Classes.txt', 'r') as f:
                    class_names = f.read().splitlines()
                return class_names
            # load the image and preprocess it
            def load_prep(img_path):
                img = tf.io.read_file(img_path)
                img = tf.image.decode_image(img)
                img = tf.image.resize(img, size=(224, 224))
                return img
            
            # Make predictions  
            def make_prediction(model, image, classes):
                pred = model.predict(tf.expand_dims(image, axis=0))
                pred_idx = np.argmax(pred)
                predicted_value = classes[pred_idx]
                return predicted_value
            
            # Make prediction but 3 results
            def make_prediction_3(model, image, classes):
                pred = model.predict(tf.expand_dims(image, axis=0))
                pred_idx = np.argsort(pred)[0][-3:]
                predicted_value = [classes[i] for i in pred_idx]
                return predicted_value
            
            
            if file_serializer.data['type'] == 'fruit': # Check if the user wants fruits
                image = load_prep(path_mqad)
                model = load_model_fruit()
                classes = load_classes_fruit()
                prediction = make_prediction_3(model=model, classes=classes, image=image)
                print(prediction)
                
                # result
                for i, elem in enumerate(prediction):
                    result = elem.split(sep="___")
                    sub_res["Name"] = result[0].title()
                    sub_res["Condition"] = result[1].title()
                    sub_res["Type"] = result[2].title()
                    dic_res[f"result_{i}"] = sub_res
                
            elif file_serializer.data['type'] == 'leaf': # Check if the user wants leaves
                image = load_prep(path_mqad)
                model = load_model_leaf(model_name=file_serializer.data['name'].title())
                classes = load_classes_leaf(classes_name=file_serializer.data['name'].title())
                prediction = make_prediction_3(model=model, classes=classes, image=image)
                
                # result
                for i, elem in enumerate(prediction):
                    result = elem.split(sep="___")
                    sub_res["Name"] = result[0].title()
                    sub_res["Condition"] = result[1].title()
                    sub_res["Type"] = file_serializer.data['type'].title()
                    dic_res[f"result_{i}"] = sub_res
            else:
                return Response("Type is not valid", status=status.HTTP_400_BAD_REQUEST)
            
        
            img_url = file_serializer.data['file']
            
            dic_res["image_url"] = img_url
            
            return Response(dic_res, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
