from src.services.kerasModelService import loadKerasModel, checkImageFile

model = loadKerasModel('fruitModel')

print('PFLAUME: ', checkImageFile(model, '../data/ML_TEST/1_PFLAUME/IMG_8331.JPG'))
print('PFLAUME: ', checkImageFile(model, '../data/ML_TEST/1_PFLAUME/IMG_8315.JPG'))
print('PFLAUME: ', checkImageFile(model, '../data/ML_TEST/1_PFLAUME/IMG_8306.JPG'))
print('PFLAUME: ', checkImageFile(model, '../data/ML_TEST/1_PFLAUME/IMG_8294.JPG'))
print('PFLAUME: ', checkImageFile(model, '../data/ML_TEST/1_PFLAUME/IMG_8291.JPG'))

print('BANANE: ', checkImageFile(model, '../data/ML_TEST/2_BANANE/IMG_8846.JPG'))
print('BANANE: ', checkImageFile(model, '../data/ML_TEST/2_BANANE/IMG_8835.JPG'))
print('BANANE: ', checkImageFile(model, '../data/ML_TEST/2_BANANE/IMG_8826.JPG'))
print('BANANE: ', checkImageFile(model, '../data/ML_TEST/2_BANANE/IMG_8816.JPG'))
print('BANANE: ', checkImageFile(model, '../data/ML_TEST/2_BANANE/IMG_8772.JPG'))

print('APFEL: ', checkImageFile(model, '../data/ML_TEST/3_Apfel/IMG_8198.JPG'))
print('APFEL: ', checkImageFile(model, '../data/ML_TEST/3_Apfel/IMG_8215.JPG'))
print('APFEL: ', checkImageFile(model, '../data/ML_TEST/3_Apfel/IMG_8215.JPG'))
print('APFEL: ', checkImageFile(model, '../data/ML_TEST/3_Apfel/IMG_8209.JPG'))
print('APFEL: ', checkImageFile(model, '../data/ML_TEST/3_Apfel/IMG_8162.JPG'))

print('ANANAS: ', checkImageFile(model, '../data/ML_TEST/4_Ananas/IMG_8512.JPG'))
print('ANANAS: ', checkImageFile(model, '../data/ML_TEST/4_Ananas/IMG_8523.JPG'))
print('ANANAS: ', checkImageFile(model, '../data/ML_TEST/4_Ananas/IMG_8560.JPG'))
print('ANANAS: ', checkImageFile(model, '../data/ML_TEST/4_Ananas/IMG_8440.JPG'))
print('ANANAS: ', checkImageFile(model, '../data/ML_TEST/4_Ananas/IMG_8367.JPG'))