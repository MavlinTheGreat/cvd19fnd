import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import nii2png
import os


def neural_pred(gz_path):
    SIZE = 224

    def resize_image(img):
        img = tf.cast(img, tf.float32)
        img = tf.image.resize(img, (SIZE, SIZE))
        img = img / 255.0
        return img
    
    model = load_model("keras_model.h5")
    print("loaded")
    nii2png.convert(gz_path)
    fold = gz_path.split('/')[-1] + "_folder"
    fileseses = os.listdir(fold)
    pr_zdr = 0
    pr_bol = 0
    for f in fileseses:  
        img = load_img(fold + "/" + f) # tensorflow: загрузка изображения
        img_array = img_to_array(img) # tensorflow: превращение изображения в массив
        img_resized = resize_image(img_array) # 
        img_expended = np.expand_dims(img_resized, axis=0)
        prediction = model.predict(img_expended)
        pr_zdr += prediction[0][0]
        pr_bol += prediction[0][1]
        #pred_label = 'БОЛЕН' if prediction[0][0] < prediction[0][1] else 'ЗДОРОВ'
    if pr_bol >= pr_zdr:
        return 1
    return 0
