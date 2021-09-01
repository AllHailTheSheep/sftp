import os
import pathlib
from posixpath import join
import subprocess
import sys



def getImagesInFolder(dir):
    '''Gets list of paths to all images in a folder

    @type dir: str
    @param dir: The path to look for images in
    @rtype: list
    @returns: a list of image paths'''

    def getFilesInFolder(dir):
        '''Gets list of paths to all files in folder

        @type dir: str
        @param dir: The path to look for files in
        @rtype: list
        @returns: a list of file paths'''

        currentFiles = []
        for root, dirs, files in os.walk(dir, topdown=True):
            for name in files:
                currentFiles.append(os.path.join(root, name))
            for name in dirs:
                currentFiles.append(os.path.join(root, name))
        return currentFiles

    # now we get our current files
    currentFiles = getFilesInFolder(dir)
    # intialize our list
    images = []
    fileExtensions = ['.jpg', '.jpeg', '.png']
    for file in currentFiles:
        ext = pathlib.Path(file).suffix
        if ext in fileExtensions:
            # if our extension is one of the specified, add it to the images list
            images.append(file)
    return images

def openImage(path):
    ''' A platform specific funcition that opens an image in the users native environment with their default app
    @type path: str
    @param path: the path to the image to open'''

    ImageFromCMD = {'linux':'xdg-open',
                    'win32':'explorer',
                    'darwin':'open'}[sys.platform]
    subprocess.Popen([ImageFromCMD, path])