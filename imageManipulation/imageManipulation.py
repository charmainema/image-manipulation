# import modules
from PIL import Image, ImageFilter, ImageOps
import os
import time

# initialize variables
filler = None

# list of edits 
taskList = {
    "extension": "to change the file extension \n(all new png images will be saved to a new \"png\" folder, and all new jpg images will be saved to a new \"jpg\" folder)",
    "size": "to change the size",
    "thumbnail": "to save a new thumbnail of selected image",
    "rotate": "to rotate the image",
    "black-white": "to convert to black and white",
    "blur": "to blur the image",
    "invert": "to invert the image's colors",
    "delete": "to delete an image"
}

# check whether the user's selection is valid
def checkValidSelection(selection, dictionary):
    for i in dictionary:
        if selection == i:
            return False
    return True

# print list of tasks
def printTasks(taskList):
    number = 1
    tasks = ""
    for i in taskList:
        tasks += f"\n{number}. \"{i}\" {taskList[i]},"
        number += 1
    return tasks

# print list of images
def printImages():
    printImages = ""
    for i in os.listdir(f"{os.getcwd()}\\images"):
        printImages += f"\n- \"{i}\""
    return printImages

# print list of folders
def printFolders(dir):
    printFolders = ""
    if dir == None:
        for i in os.listdir(os.getcwd()):
            if i == "imageManipulation.py":
                continue
            printFolders += f"\n- \"{i}\""
    else:
        for i in os.listdir(f"{os.getcwd()}\\{dir}"):
            printFolders += f"\n- \"{i}\""
    return printFolders

# print list of folders
def printFoldersDelete(dir):
    printFolders = ""
    if dir == None:
        for i in os.listdir(os.getcwd()):
            if i == "images" or i == "imageManipulation.py":
                continue
            printFolders += f"\n- \"{i}\""
        if printFolders == "":
            print("\n~~~~~~~~~~~~~~~~")
            print("It appears you have no files to delete. (You cannot delete the pictures in the \"images\" file)")
            proceed = input("(Press enter to continue) ")
            return True
        else:
            print("\n~~~~~~~~~~~~~~~~")
            filePath = input(f"In which file would you like to delete your image?{printFolders}\n: ")
            while checkValidSelection(filePath, os.listdir(os.getcwd())):
                print("\n~~~~~~~~~~~~~~~~")
                print("Invalid selection. Please re-enter selection.")
                filePath = input(f"In which file would you like to delete your image?{printFolders}\n: ")
            return filePath
    
# delete image
def Delete(dir):
    printFolders = ""
    for i in os.listdir(f"{os.getcwd()}\\{dir}"):
        printFolders += f"\n- \"{i}\""
    if printFolders == "":
        print("\n~~~~~~~~~~~~~~~~")
        print("It appears this file is empty.")
        proceed = input("(Press enter to continue) ")
        return True
    else:
        print("\n~~~~~~~~~~~~~~~~")
        image = input(f"Select the image you would like to delete from the following:{printFolders}\n: ")
        while checkValidSelection(image, os.listdir(f"{os.getcwd()}\\{dir}")):
            print("\n~~~~~~~~~~~~~~~~")
            print("Invalid selection. Please re-enter selection.")
            image = input(f"Select the image you would like to delete from the following:{printFolders}\n: ")
        return image

# select extension
def selectExtension():
    extension = input("Which extension would you like to change your image to? Type \"png\" to change to png. Type \"jpg\" to change to JPEG: ")
    # check if valid selection
    while extension != "jpg" and extension != "png":
        print("\n~~~~~~~~~~~~~~~~")
        print("Invalid selection. Please re-enter selection.")
        extension = input("Which extension would you like to change your image to? Type \"png\" to change to png. Type \"jpg\" to change to JPEG: ")
    extension = "." + extension
    return extension

# change extension
def changeExtension(img, singleEditTrue):
    folder = ""
    print("\n~~~~~~~~~~~~~~~~")
    selection = selectExtension()
    # check if image already has selected extension
    while os.path.splitext(img)[1] == selection:
        print("\n~~~~~~~~~~~~~~~~")
        print(f"Your image already has the selected selection: \"{selection}\". Please select a different extension.")
        selection = selectExtension()
    # select folder or create new folder if it doesn't already exist
    if singleEditTrue:
        if selection == ".jpg":
            if os.path.exists(f"{os.getcwd()}\\jpg") == False:
                os.mkdir(f"{os.getcwd()}\\jpg")
            folder = f"{os.getcwd()}\\jpg"
        if selection == ".png":
            if os.path.exists(f"{os.getcwd()}\\png") == False:
                os.mkdir(f"{os.getcwd()}\\png")
            folder = f"{os.getcwd()}\\png"
    time.sleep(1)
    print(f"Your image has been converted to {selection}!")
    newExtension = os.path.splitext(img)[0] + selection
    newExtension = newExtension.split("\\")[-1]
    savePath = f"{folder}\\{newExtension}"
    return savePath

# change width
def size(img, dimension):
    # input width
    print("\n~~~~~~~~~~~~~~~~")
    selectSize = input(f"Enter the {dimension} you would like your image to be (pixels), or enter \"same\" to keep the original {dimension}: ")
    # if width is not an integer
    while selectSize.isnumeric() == False and selectSize != "same":
        print("\n~~~~~~~~~~~~~~~~")
        print("Your entry is not a number. Please enter a numeric size.")
        selectSize = input(f"Enter the {dimension} you would like your image to be (pixels), or enter \"same\" to keep the original {dimension}: ")
    if selectSize == "same":
        selectSize = Image.open(img).size[0]
    else:
        selectSize = int(selectSize)
    return selectSize

# create thumbnail
def thumbnail(img):
    # user selects thumbnail size
    print("\n~~~~~~~~~~~~~~~~")
    thumbnailSize = input("What size would you like your thumbnail to be? (Enter \"200\", \"400\", or \"600\"): ")
    # check if thumbnailSize is valid
    while thumbnailSize != "200" and thumbnailSize != "400" and thumbnailSize != "600":
        print("\n~~~~~~~~~~~~~~~~")
        print("Invalid selection. Please re-enter selection.")
        thumbnailSize = input("What size would you like your thumbnail to be? (Enter \"200\", \"400\", or \"600\"): ")
    thumbnailSize = (int(thumbnailSize), int(thumbnailSize))
    image = Image.open(img)
    image.thumbnail(thumbnailSize)
    fileName = img.split("\\")[-1]
    # create thumbnails folder if not already existing and save thumbnail
    if thumbnailSize == (200, 200):
        if os.path.exists(f"{os.getcwd()}\\thumbnails-200") == False:
            os.mkdir(f"{os.getcwd()}\\thumbnails-200")
        image.save(f"{os.getcwd()}\\thumbnails-200\\{fileName}")
    elif thumbnailSize == (400, 400):
        if os.path.exists(f"{os.getcwd()}\\thumbnails-400") == False:
            os.mkdir(f"{os.getcwd()}\\thumbnails-400")
        image.save(f"{os.getcwd()}\\thumbnails-400\\{fileName}")
    elif thumbnailSize == (600, 600):
        if os.path.exists(f"{os.getcwd()}\\thumbnails-600") == False:
            os.mkdir(f"{os.getcwd()}\\thumbnails-600")
        image.save(f"{os.getcwd()}\\thumbnails-600\\{fileName}")

# rotate image
def rotateImg():
    # input degree of rotation
    print("\n~~~~~~~~~~~~~~~~")
    degree = input("Enter to what degree you would like to rotate your image to: ")
    # check whether entry is valid
    while degree.isnumeric() == False:
        print("\n~~~~~~~~~~~~~~~~")
        print("The value you entered is not a number. Please enter a number.")
        degree = input("Enter to what degree you would like to rotate your image to: ")
    return int(degree)

# convert to black and white
def convertBlackWhite():
    time.sleep(1)
    print("\n~~~~~~~~~~~~~~~~")
    print("Your image has been converted!")
    time.sleep(0.5)
    return "L"

# blur image 
def blurRadius():
    print("\n~~~~~~~~~~~~~~~~")
    radius = input("Enter the blur radius of your choice: ")
    while radius.isnumeric() == False:
        print("\n~~~~~~~~~~~~~~~~")
        print("The value you entered is not a number. Please enter a number.")
        radius = input("Enter the blur radius of your choice: ")
    return int(radius)

# invert colors
def invert(img):
    return ImageOps.invert(img)

# view image
def viewImage():
    complete = True
    while complete == True:
        # select folder to view from
        print("\n~~~~~~~~~~~~~~~~")
        filePath = input(f"Select the desired folder you would like to view your image from, from either of:{printFolders(filler)}\n or enter \"done\" to quit: ")
        if filePath == "done":
            complete = False
            continue
        # check if selection is valid
        while os.path.exists(f"{os.getcwd()}\\{filePath}") == False and filePath != "done":
            print("\n~~~~~~~~~~~~~~~~")
            print("Invalid selection. Please re-enter selection.")
            filePath = input(f"Select the desired folder you would like to view your image from, from either of:{printFolders(filler)}\n: ")
        # select image to view within selected folder
        print("\n~~~~~~~~~~~~~~~~")
        selectImage = input(f"Enter the image you would like to view within the selected folder:{printFolders(filePath)}\n: ")
        while os.path.exists(f"{os.getcwd()}\\{filePath}\\{selectImage}") == False and selectImage != "done":
            print("\n~~~~~~~~~~~~~~~~")
            print(f"The selected image does not exist in the current folder: \"{filePath}\".\nPlease re-enter selection, or change selected folder by entering, \"change\".")
            selectImage = input(f"Enter the image you would like to view within the selected folder:{printFolders(filePath)}\n: ")
            if selectImage == "change":
                break
        if selectImage == "change":
            continue
        else:
            Image.open(f"{os.getcwd()}\\{filePath}\\{selectImage}").show()

def saveProcedure():
    time.sleep(1)
    print("\n~~~~~~~~~~~~~~~~")
    print("Your image has been saved!")
    proceed = input("(Press enter to continue) ")
    return True

# save image
def saveImage(filename, savePath, saveImg, mode, imgSize, degree, radius):
    if os.path.exists(f"{os.getcwd()}\\{filename}") == False:
        os.mkdir(f"{os.getcwd()}\\{filename}")
    saveImg.convert(mode).resize(imgSize).rotate(degree).filter(ImageFilter.GaussianBlur(radius)).save(f"{os.getcwd()}\\{filename}\\{savePath}")


def selectTask(taskList):
    # select which task to run
    print("\n~~~~~~~~~~~~~~~~")
    task = input(f"What would you like to do with your image? Type... {printTasks(taskList)} \nand type \"done\" to save changes: ")
    # check if selection is valid
    while checkValidSelection(task, taskList) and task != "done":
        print("\n~~~~~~~~~~~~~~~~")
        print("Invalid selection. Please re-enter selection.")
        task = input(f"What would you like to do with your image? Type...{printTasks(taskList)} \nand type \"done\" to save changes: ")
    return task

complete = False

# initialize image manipulation
selection = input("Would you like to edit or view your image? Type \"yes\" to edit an image. Type \"view\" to view an image. Type \"no\" to quit: ")
while selection != "yes" and selection != "no" and selection != "view":
    print("\n~~~~~~~~~~~~~~~~")
    print("Invalid selection. Please re-enter selection.")
    selection = input("Would you like to edit or view your image? Type \"yes\" to edit an image. Type \"view\" to view an image. Type \"no\" to quit: ")

while selection != "no":
    if selection == "view":
        viewImage()
    elif selection == "yes":
        complete = False
        selected = False
        while selected == False:
            # select image
            print("\n~~~~~~~~~~~~~~~~")
            edit = input(f"Which image would you like to edit? Select from the following images by typing:{printImages()} \nTo add new images, move the desired image to the \"images\" folder, and press \"r\" to refresh the list of files to select your image: ")
            # check if selection is valid
            while os.path.exists(f"{os.getcwd()}\\images\\{edit}") == False and edit != "r":
                    print("\n~~~~~~~~~~~~~~~~")
                    print("Image does not exist. Please re-enter selection.")
                    edit = input(f"Which image would you like to edit? Select from the following images by typing:{printImages()} \nTo add new images, move the desired image to the \"images\" folder, and press \"r\" to refresh the list of files: ")
            # check if selection is included in default images
            if edit == "r":
                continue
            else:
                saveImg = Image.open(f"{os.getcwd()}\\images\\{edit}")
                img = f"{os.getcwd()}\\images\\{edit}"
                imgSize = Image.open(img).size
                degree = 0
                mode = "RGB"
                radius = 0
                savePath = edit
                selected = True
            # ask user whether multiple changes would like to be made
            print("\n~~~~~~~~~~~~~~~~")
            multipleChanges = input("Would you like to make multiple changes to this image? (Enter \"yes\", or \"no\"): ")
            while multipleChanges != "yes" and multipleChanges != "no":
                print("\n~~~~~~~~~~~~~~~~")
                print("Invalid selection. Please re-enter selection.")
                multipleChanges = input("Would you like to make multiple changes to this image? (Enter \"yes\", or \"no\"): ")
        # make multiple changes to image
        if multipleChanges == "yes":
            editCount = 0
            # edit image (multiple changes)
            while complete == False:
                task = selectTask(taskList)
                # change extension
                if task == "extension":
                    savePath = changeExtension(img, False).split("\\")[-1]
                    print(savePath)
                    editCount += 1
                # change size
                elif task == "size":
                    width = size(img, "width")
                    height = size(img, "height")
                    imgSize = (width, height)
                    editCount += 1
                # create thumbnail
                elif task == "thumbnail":
                    thumbnail(img)
                # rotate image
                elif task == "rotate":
                    degree = rotateImg()
                    editCount += 1
                # convert to black and white
                elif task == "black-white":
                    mode = convertBlackWhite()
                    editCount += 1
                # blur the image
                elif task == "blur":
                    radius = blurRadius()
                    editCount += 1
                # invert the image
                elif task == "invert":
                    saveImg = ImageOps.invert(saveImg.convert("RGB"))
                    editCount += 1
                # delete an image
                elif task == "delete":
                    print("\n~~~~~~~~~~~~~~~~")
                    option = input("Do you really want to delete an image? (Note: you will not be allowed to delete images in the \"images\" folder.) Type \"yes\" to select and delete an image. Type \"no\" to return: ")
                    while option != "yes" and option != "no":
                        print("Invalid selection. Please re-enter selection.")
                        print("\n~~~~~~~~~~~~~~~~")
                        option = input("Do you really want to delete an image? (Note: you will not be allowed to delete images in the \"images\" folder.) Type \"yes\" to select and delete an image. Type \"no\" to return: ")
                    if option == "yes":
                        file = printFoldersDelete(filler)
                        if file == True:
                            complete = True
                        else:
                            image = Delete(file)
                            if image == True:
                                continue
                            else:
                                os.remove(f"{os.getcwd()}\\{file}\\{image}")
                                time.sleep(1)
                                print("\n~~~~~~~~~~~~~~~~")
                                print("Your image has been deleted!")
                                time.sleep(0.5)
                # if edits are complete
                elif task == "done":
                    if editCount > 0:
                        saveImage("multiple-edits", savePath, saveImg, mode, imgSize, degree, radius)
                    complete = saveProcedure()
        # make single edits to image 
        else:
            task = selectTask(taskList)
            # change extension
            if task == "extension":
                savePath = changeExtension(img, True)
                saveImg.convert("RGB").save(savePath)
                complete = saveProcedure()
            # change size
            elif task == "size":
                width = size(img, "width")
                height = size(img, "height")
                imgSize = (width, height)
                saveImage(f"{width}-width", f"{width}-width_" + savePath , saveImg, mode, imgSize, degree, radius)
                complete = saveProcedure()
            # create thumbnail
            elif task == "thumbnail":
                thumbnail(img)
                complete = saveProcedure()
            # rotate image
            elif task == "rotate":
                degree = rotateImg()
                complete = saveProcedure()
                saveImage("rotated-images", f"{degree}degree_" + savePath, saveImg, mode, imgSize, degree, radius)
            # convert to black and white
            elif task == "black-white":
                mode = convertBlackWhite()
                saveImage("black-and-white", "bw_" + savePath, saveImg, mode, imgSize, degree, radius)
                complete = saveProcedure()
            # blur the image
            elif task == "blur":
                radius = blurRadius()
                saveImage("blur", "blur_" + savePath, saveImg, mode, imgSize, degree, radius)
                complete = saveProcedure()
            # invert the image
            elif task == "invert":
                saveImg = ImageOps.invert(saveImg)
                saveImage("invert", "inverted_" + savePath, saveImg, mode, imgSize, degree, radius)
            # delete an image
            elif task == "delete":
                print("\n~~~~~~~~~~~~~~~~")
                option = input("Do you really want to delete an image? (Note: you will not be allowed to delete images in the \"images\" folder.) Type \"yes\" to select and delete an image. Type \"no\" to return: ")
                while option != "yes" and option != "no":
                    print("Invalid selection. Please re-enter selection.")
                    print("\n~~~~~~~~~~~~~~~~")
                    option = input("Do you really want to delete an image? (Note: you will not be allowed to delete images in the \"images\" folder.) Type \"yes\" to select and delete an image. Type \"no\" to return: ")
                if option == "yes":
                    file = printFoldersDelete(filler)
                    if file == True:
                        complete = True
                    else:
                        image = Delete(file)
                        if image == True:
                            complete = True
                        else:
                            os.remove(f"{os.getcwd()}\\{file}\\{image}")
                            time.sleep(1)
                            print("\n~~~~~~~~~~~~~~~~")
                            print("Your image has been deleted!")
                            time.sleep(0.5)

    # re-loop through selections unless user quits
    print("\n~~~~~~~~~~~~~~~~")
    selection = input("Would you like to edit or view your image? Type \"yes\" to edit an image. Type \"view\" to view an image. Type \"no\" to quit: ")
    while selection != "yes" and selection != "no" and selection != "view":
        print("\n~~~~~~~~~~~~~~~~")
        print("Invalid selection. Please re-enter selection.")
        selection = input("Would you like to edit or view your image? Type \"yes\" to edit an image. Type \"view\" to view an image. Type \"no\" to quit: ")

