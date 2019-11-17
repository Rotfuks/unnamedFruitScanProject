from flask import Flask, request
import os
from services.kerasModelService import loadKerasModel, checkImageFile
from configurations.environmentConfigurations import LocalEnvironment, ProdEnvironment
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = loadKerasModel('fruitModel')

@app.route('/', methods=['GET'])
def healthResponse():
    return "I am alive", 200

@app.route('/', methods=['POST'])
def getResult():
    if 'file' not in request.files:
        print('No file part')
    f = request.files['file']
    result = checkImageFile(model, f)
    print(result)
    return result, 200

if os.environ['ENV'] == 'prod':
    config = ProdEnvironment()
else:
    config = LocalEnvironment()

if __name__ == "__main__":
    app.run(host=config.HOST)