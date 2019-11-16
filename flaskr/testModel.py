from services.kerasModelService import loadKerasModel, checkImagePath

model = loadKerasModel('fruitModel')
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8198.JPG'))
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8215.JPG'))
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8215.JPG'))
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8209.JPG'))
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8162.JPG'))