from typing import Any
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from .model_utils import load_prep, make_prediction_3
from .model_loader import load_model_fruit, load_model_leaf, load_classes_fruit, load_classes_leaf


# Load the models and classes during server startup
fruit_model = load_model_fruit()
leaf_models = {
    'Apple': load_model_leaf('Apple'),
    'Bell_Pepper': load_model_leaf('Bell_Pepper'),
    'Broad_Bean': load_model_leaf('Broad_Bean'),
    'Corn_Maize': load_model_leaf('Corn_Maize'),
    'Eggplant': load_model_leaf('Eggplant'),
    'Grape' : load_model_leaf('Grape'),
    'Mango' : load_model_leaf('Mango'),
    'Orange' : load_model_leaf('Orange'),
    'Peach' : load_model_leaf('Peach'),
    'Potato' : load_model_leaf('Potato'),
    'Tomato' : load_model_leaf('Tomato')
    # Add other leaf models here
}

fruit_classes = load_classes_fruit()
leaf_classes = {
    'Apple': load_classes_leaf('Apple'),
    'Bell_Pepper': load_classes_leaf('Bell_Pepper'),
    'Broad_Bean': load_classes_leaf('Broad_Bean'),
    'Corn_Maize': load_classes_leaf('Corn_Maize'),
    'Eggplant': load_classes_leaf('Eggplant'),
    'Grape' : load_classes_leaf('Grape'),
    'Mango' : load_classes_leaf('Mango'),
    'Orange' : load_classes_leaf('Orange'),
    'Peach' : load_classes_leaf('Peach'),
    'Potato' : load_classes_leaf('Potato'),
    'Tomato' : load_classes_leaf('Tomato')
    # Add other leaf classes here
}

class FileView(APIView):

    def post(self, request, *args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != settings.API_KEY:
            raise AuthenticationFailed('Invalid API key')
        
        from .serializers import FileSerializer  # Import the serializer here
        global fruit_model, leaf_models, fruit_classes, leaf_classes

        try:
            file_serializer = FileSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()

                dic_res = {
                    'result_0': {},
                    'result_1': {},
                    'result_2': {}
                }
                sub_res = {}
                path = file_serializer.data['file'][1:]

                if file_serializer.data['type'] == 'fruit':  # Check if the user wants fruits
                    image = load_prep(path)
                    model = fruit_model
                    classes = fruit_classes
                    prediction = make_prediction_3(model=model, classes=classes, image=image)

                    # result
                    for i, elem in enumerate(prediction):
                        result = elem.split(sep="___")
                        sub_res["Name"] = result[0].title()
                        sub_res["Condition"] = result[1].title()
                        sub_res["Type"] = result[2].title()
                        dic_res[f"result_{i}"].update(sub_res)

                elif file_serializer.data['type'] == 'leaf':  # Check if the user wants leaves
                    image = load_prep(path)
                    model = leaf_models[file_serializer.data['name'].title()]
                    classes = leaf_classes[file_serializer.data['name'].title()]
                    prediction = make_prediction_3(model=model, classes=classes, image=image)

                    # result
                    for i, elem in enumerate(prediction):
                        result = elem.split(sep="___")
                        sub_res["Name"] = result[0].title()
                        sub_res["Condition"] = result[1].title()
                        sub_res["Type"] = file_serializer.data['type'].title()
                        dic_res[f"result_{i}"].update(sub_res)
                else:
                    return Response("Type is not valid", status=status.HTTP_400_BAD_REQUEST)

                img_url = file_serializer.data['file']

                dic_res["image_url"] = img_url

                return Response(dic_res, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
