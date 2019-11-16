from services.kerasModelService import createKerasModel, saveKerasModel

model = createKerasModel('../data/ML_TRAINING', '../data/ML_TEST')
saveKerasModel(model, 'fruitModel')