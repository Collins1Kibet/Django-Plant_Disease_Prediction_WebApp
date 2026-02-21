from django.shortcuts import render
from .models import UploadImage
from .forms import UploadImageForm
from .serializers import UploadImageSerializer
from PIL import Image
import tensorflow as tf
import numpy as np

from rest_framework import viewsets
from rest_framework.response import Response


# --- REST API ViewSet ---
class UploadImageViewset(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer


# --- Loading Model ---
def load_model():
    model_path = r'C:\Users\HP\Desktop\Data Analytics + Science\Web Dev\Django Plant Disease Prediction\plant_disease_classification_model.h5'
    model = tf.keras.models.load_model(model_path)
    return model


# --- Preprocessing Image ---
def load_and_preprocess_image(image_path, target_size=(256, 256)):
    image = Image.open(image_path)
    image = image.resize(target_size)
    image_array = np.asarray(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = image_array.astype('float32') / 255.0
    return image_array


# --- Prediction ---
def predict_image(model, image_path):
    preprocessed_image = load_and_preprocess_image(image_path)
    prediction = model.predict(preprocessed_image)
    return prediction



def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()

            model = load_model()
            prediction = predict_image(model, uploaded_image.image.path)

            
            predicted_class_index = int(np.argmax(prediction, axis=1)[0])
            class_names = ['Healthy', 'Rust', 'Blight', 'Mildew']  
            result = class_names[predicted_class_index]

            return render(request, 'upload.html', {
                'form': form,
                'prediction': result,
                'image': uploaded_image
            })
    else:
        form = UploadImageForm()

    return render(request, 'upload.html', {'form': form})


"""
def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()

            # Load model and make prediction
            model = load_model()
            prediction = predict_image(model, uploaded_image.image.path)

            # Handle single output (binary classification)
            score = float(prediction[0][0])  # Extract scalar
            result = 'Uninfected' if score > 0.5 else 'Infected'

            return render(request, 'upload.html', {
                'form': form,
                'prediction': result,
                'image': uploaded_image
            })
    else:
        form = UploadImageForm()

    return render(request, 'upload.html', {'form': form})
"""