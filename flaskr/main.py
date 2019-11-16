from flask import Flask, request
from services.kerasModelService import loadKerasModel, checkImageFile

app = Flask(__name__)
model = loadKerasModel('fruitModel')

@app.route('/', methods=['POST'])
def getResult():
    if 'file' not in request.files:
        print('No file part')
    f = request.files['file']
    result = checkImageFile(model, f)
    print(result)
    return result

if __name__ == "__main__":
    app.run()