from flask import Flask, request
from services.kerasModelService import createKerasModel, saveKerasModel, loadKerasModel, checkImageInModel
import json

from services.FileService import FileService
app = Flask(__name__)
fileService = FileService('temp')

@app.route('/', methods=['GET'])
def getFiles():
    return json.dumps(fileService.getFiles())

@app.route('/', methods=['POST'])
def saveFile():
    f = request.files['file']
    return f

print("test")
model = loadKerasModel('regalArticleModel')
result = checkImageInModel(model, '/Users/jan/Documents/repos/unnamedFruitScanProject/flaskr/dataset/Codecamp_Regal/Testset/1_Haribo_Goldbaer/IMG_1119.jpg')
print(result)

if __name__ == "__main__":
    app.run()