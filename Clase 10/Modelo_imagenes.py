import tensorflow as tf
import tensorflow_hub as hub #descargar modelos
import numpy as np #arrays
import cv2 #leer y dibujar sobre la imagen
import matplotlib.pyplot as plt

detector = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2") #descarga el modelo

coco_labels = {
    1: 'person',
    2: 'bicycle',
    3: 'car',
    4: 'motorcycle',
    5: 'airplane',
    6: 'bus',
    7: 'train',
    8: 'truck',
    9: 'boat',
    10: 'traffic light',
    11: 'fire hydrant',
    13: 'stop sign',
    14: 'parking meter',
    15: 'bench',
    16: 'bird',
    17: 'cat',
    18: 'dog',
    19: 'horse',
    20: 'sheep',
    21: 'cow',
    22: 'elephant',
    23: 'bear',
    24: 'zebra',
    25: 'giraffe',
    27: 'backpack',
    28: 'umbrella',
    31: 'handbag',
    32: 'tie',
    33: 'suitcase',
    34: 'frisbee',
    35: 'skis',
    36: 'snowboard',
    37: 'sports ball',
    38: 'kite',
    39: 'baseball bat',
    40: 'baseball glove',
    41: 'skateboard',
    42: 'surfboard',
    43: 'tennis racket',
    44: 'bottle',
    46: 'wine glass',
    47: 'cup',
    48: 'fork',
    49: 'knife',
    50: 'spoon',
    51: 'bowl',
    52: 'banana',
    53: 'apple',
    54: 'sandwich',
    55: 'orange',
    56: 'broccoli',
    57: 'carrot',
    58: 'hot dog',
    59: 'pizza',
    60: 'donut',
    61: 'cake',
    62: 'chair',
    63: 'couch',
    64: 'potted plant',
    65: 'bed',
    67: 'dining table',
    70: 'toilet',
    72: 'tv',
    73: 'laptop',
    74: 'mouse',
    75: 'remote',
    76: 'keyboard',
    77: 'cell phone',
    78: 'microwave',
    79: 'oven',
    80: 'toaster',
    81: 'sink',
    82: 'refrigerator',
    84: 'book',
    85: 'clock',
    86: 'vase',
    87: 'scissors',
    88: 'teddy bear',
    89: 'hair drier',
    90: 'toothbrush'
}  #todas las cosas que detecta el modelo
#FINITA la cantidad que detecta

# Leer imagen y convertir a tensor
image_path = "/Users/flor/Documents/Facultad/Progra_python/VSC/Clase 10/persona.jpg"
image = cv2.imread(image_path) #lee la imagen
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #la convierte en rbg
input_tensor = tf.convert_to_tensor(image_rgb) #convierte en tensor-> cada pixel en una matriz, cada pixel está compuesto de 3 números: las intensidades del RGB del pixel.
input_tensor = input_tensor[tf.newaxis, ...]

# Hacer predicción
result = detector(input_tensor)

boxes = result['detection_boxes'][0].numpy()
class_ids = result['detection_classes'][0].numpy().astype(np.int32)
scores = result['detection_scores'][0].numpy()

height, width, _ = image_rgb.shape

# Mostrar imagen con detecciones
plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.axis('off')
plt.show()