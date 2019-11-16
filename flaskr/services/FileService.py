import os

from PIL import Image


class FileService:

    global dirPath

    def __init__(self, dirPath):
        self.dirPath = dirPath

    def getFiles(self):
        return [file for file in os.listdir(self.dirPath)]

    def saveImage(self, file):
        # TODO
        return "TODO"