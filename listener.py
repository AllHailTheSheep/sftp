import time
from uttils import getImagesInFolder, openImage

folderToListen = input("Input path to folder to listen in: ")
# we run this once to get the images that are already in the target folder
seenImages = getImagesInFolder(folderToListen, recursive=True)

while True:
    time.sleep(1)
    # get the current list of images in folder
    currentImages = getImagesInFolder(folderToListen, recursive=True)
    for image in currentImages:
        # if we have an image in the current images that appeared since the last check, we open it
        if image not in seenImages:
            openImage(image)
            seenImages.append(image)
    # if the user takes an image out of the folder, we want it to be shown when it appears
    for image in seenImages:
        if image not in currentImages:
            seenImages.remove(image)