# Importing the Keras libraries and packages
from keras.models import Sequential, load_model
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image

def createKerasModel(pathTrainingset, pathTestset):
    # Initialising the CNN
    classifier = Sequential()
    # Step 1 - Convolution
    classifier.add(Conv2D(32, (3, 3), input_shape = (128, 128, 3), activation = 'relu'))
    classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    # Adding a second convolutional layer
    classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    # Step 3 - Flattening
    classifier.add(Flatten())
    # Step 4 - Full connection
    classifier.add(Dense(units = 128, activation = 'relu'))
    classifier.add(Dense(units = 12, activation = 'softmax'))
    # Compiling the CNN
    classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
    # Part 2 - Fitting the CNN to the images
    from keras.preprocessing.image import ImageDataGenerator
    train_datagen = ImageDataGenerator(rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True)
    test_datagen = ImageDataGenerator(rescale = 1./255)
    training_set = train_datagen.flow_from_directory(pathTestset,
    target_size = (128, 128),
    batch_size = 64,
    class_mode = 'binary')
    test_set = test_datagen.flow_from_directory(pathTrainingset,
    target_size = (128, 128),
    batch_size = 64,
    class_mode = 'binary')
    classifier.fit_generator(training_set,
    steps_per_epoch = 20,
    epochs = 1,
    validation_data = test_set,
    validation_steps = 10)
    # Part 3 - Making new predictions
    return classifier


def saveKerasModel(model, modelName):
    model.save(modelName + '.h5')

def loadKerasModel(modelName):
    return load_model(modelName + '.h5')

def checkImageInModel(model, imagePath):
    predictImage = image.load_img(imagePath, target_size = (64, 64))
    return model.predict(predictImage)