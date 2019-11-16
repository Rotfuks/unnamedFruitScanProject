from services.kerasModelService import loadKerasModel, checkImagePath

model = loadKerasModel('fruitModel')
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8198.JPG'))
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8215.JPG'))
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8215.JPG'))
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8209.JPG'))
print('APFEL: ', checkImagePath(model, '../data/ML_TEST/3_Apfel/IMG_8162.JPG'))

print('PFLAUME: ', checkImagePath(model, '../data/ML_TEST/1_PFLAUME/IMG_8331.JPG'))
print('PFLAUME: ', checkImagePath(model, '../data/ML_TEST/1_PFLAUME/IMG_8315.JPG'))
print('PFLAUME: ', checkImagePath(model, '../data/ML_TEST/1_PFLAUME/IMG_8306.JPG'))
print('PFLAUME: ', checkImagePath(model, '../data/ML_TEST/1_PFLAUME/IMG_8294.JPG'))
print('PFLAUME: ', checkImagePath(model, '../data/ML_TEST/1_PFLAUME/IMG_8291.JPG'))

print('BANANE: ', checkImagePath(model, '../data/ML_TEST/2_BANANE/IMG_8846.JPG'))
print('BANANE: ', checkImagePath(model, '../data/ML_TEST/2_BANANE/IMG_8835.JPG'))
print('BANANE: ', checkImagePath(model, '../data/ML_TEST/2_BANANE/IMG_8826.JPG'))
print('BANANE: ', checkImagePath(model, '../data/ML_TEST/2_BANANE/IMG_8816.JPG'))
print('BANANE: ', checkImagePath(model, '../data/ML_TEST/2_BANANE/IMG_8772.JPG'))