from flask import Flask, request
from keras_preprocessing.image import load_img
from services.kerasModelService import loadKerasModel, checkImageFile
import json



app = Flask(__name__)
model = loadKerasModel('fruitModel')

@app.route('/', methods=['GET'])
def getFiles():
    return json.dumps(fileService.getFiles())

@app.route('/', methods=['POST'])
def getResult():
    if 'file' not in request.files:
        print('No file part')
    f = request.files['file']
    result = checkImageFile(model, load_img(f, target_size = (128, 128)))
    print(result)
    return result

if __name__ == "__main__":
    app.run()