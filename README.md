Plant Disease Prediction System

This project is a Django-based web application for predicting plant diseases from leaf images using a Convolutional Neural Network (CNN) model.

It allows users to upload plant leaf images and receive real-time disease predictions powered by a trained deep learning model.

## Features

User-friendly interface to upload plant leaf images

- Real-time plant disease prediction

- Deep Learning model built using TensorFlow/Keras

- Image preprocessing and normalization before prediction

- Displays predicted disease class with confidence score

- Clean and responsive web interface

## Model Building and Training

- The CNN model was built, trained, and evaluated using Jupyter Notebook (located in the Notebook folder).

- Model Development Steps:

- Data preprocessing and image augmentation

- CNN architecture design

- Model training and validation

- Performance evaluation (Accuracy & Loss metrics)

Model saving for deployment (.h5 / .keras file)

The trained model is loaded in the Django backend for real-time inference.
