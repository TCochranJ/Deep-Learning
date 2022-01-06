import os
import numpy as np
import pandas as pd
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array


app = Flask(__name__)

def get_model():
    global model
    model = load_model('FruitModel.h5')
    print("Model Loaded.")

def load_images(img_path):
    img = image.load_img(img_path, target_size = (100,100))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis = 0)
    img_tensor /= 255.
    
    return img_tensor

def prediction(img_path):
    new_image = load_images(img_path)
    
    pred = model.predict(new_image)
        
    labels = np.array(pred)
    labels[labels >= 0.6] = 1
    labels[labels < 0.6] = 0
    
    final = np.array(labels)    

    result = np.where(final == 1)
    
    listOfCoordinates= list(zip(result[0], result[1]))
    for cord in listOfCoordinates:
        print(cord)

    if cord == (0, 0):
        result = "Red Apple"
    elif cord == (0, 1):
        result = "Green Apple"
    elif cord == (0, 2):
        result = "Apricot"
    elif cord == (0, 3):
        result = "Avocado"
    elif cord == (0, 4):
        result = "Banana"
    elif cord == (0, 5):
        result = "Blueberry"
    elif cord == (0, 6):
        result = "Cactus Fruit"
    elif cord == (0, 7):
        result = "Cantaloupe"
    elif cord == (0, 8):
        result = "Cherry"
    elif cord == (0, 9):
        result = "Clementine"
    elif cord == (0, 10):
        result = "Corn"
    elif cord == (0, 11):
        result = "Cucumber Ripe"
    elif cord == (0, 12):
        result = "Grape Blue"
    elif cord == (0, 13):
        result = "Kiwi"
    elif cord == (0, 14):
        result = "Lemon"
    elif cord == (0, 15):
        result = "Lime"
    elif cord == (0, 16):
        result = "Mango"
    elif cord == (0, 17):
        result = "Onion White"
    elif cord == (0, 18):
        result = "Orange"
    elif cord == (0, 19):
        result = "Papaya"
    elif cord == (0, 20):
        result = "Passion Fruit"
    elif cord == (0, 21):
        result = "Peach"
    elif cord == (0, 22):
        result = "Pear"
    elif cord == (0, 23):
        result = "Pepper Green"
    elif cord == (0, 24):
        result = "Pepper Red"
    elif cord == (0, 25):
        result = "Pineapple"
    elif cord == (0, 26):
        result = "Plum"
    elif cord == (0, 27):
        result = "Pomegranate"
    elif cord == (0, 28):
        result = "Potato Red"
    elif cord == (0, 29):
        result = "Raspberry"
    elif cord == (0, 30):
        result = "Strawberry"
    elif cord == (0, 31):
        result = "Tomato"
    elif cord == (0, 32):
        result = "Watermelon"
    else:
        result = "Image could not be classified."

    return result

get_model()

@app.route("/", methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join(r'/Users/cochran/Desktop/478_Final/static', filename)
        file.save(file_path)
        print(filename)
        product = prediction(file_path)
        print(product)
        
    return render_template('predict.html', product = product, user_image = file_path)

if __name__ == "__main__":
	app.debug = True
	app.run()
