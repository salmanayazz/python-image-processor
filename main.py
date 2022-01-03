# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Salman Ayaz
# Date: Nov. 21, 2021
# Description: A program to do advanced modifications to an image

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
# ***TO-DO: populate it to provide more functionalities***
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
# ***TO-DO: populate it to provide more functionalities***
basic = [
            "1: Apply Red Filter",
            "2: Apply Green Filter",
            "3: Apply Blue Filter",
            "4: Apply Sepia Filter",
            "5: Apply Warm Filter",
            "6: Apply Cold Filter",
            "7: Switch to Advanced Functions"

         ]

# list of advanced operation options
# ***TO-DO: populate it to provide more functionalities***
advanced =  [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Double Size",
                "4: Half Size",
                "5: Locate Fish",
                "6: Switch to Basic Functions"
            ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processor!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-7)")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        # ***TO-DO: add the rest to handle other system functionalities***
        elif userInput == "O": # if user picks to open a image
            print("Log: Opening Image")
            tkinter.Tk().withdraw() 
            openFileName = tkinter.filedialog.askopenfilename()
            img = cmpt120imageProjHelper.getImage(openFileName)
            state["lastOpenFilename"] = openFileName
            cmpt120imageProjHelper.showInterface(img, "Open image " + state["lastOpenFilename"], generateMenu(state))
        elif userInput == "S": # if the user wants to save the image
            print("Log: Saving Image")
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProjHelper.saveImage(img, saveFilename)
            state["lastSaveFilename"] = saveFilename
            cmpt120imageProjHelper.showInterface(img, state["lastOpenFilename"], generateMenu(state))
        elif userInput == "R": # to reload the original image
            print("Log: Reloading Image")
            img = cmpt120imageProjHelper.getImage(state["lastOpenFilename"])
            cmpt120imageProjHelper.showInterface(img, state["lastOpenFilename"], generateMenu(state))
        else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        # ***TO-DO: add the rest to handle other manipulation functionalities***

        if state["mode"] == "basic": # basic manipulations
            if userInput == "1": # apply red filter
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.applyRedFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply red filter " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "2": # apply green filter
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.applyGreenFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply green filter " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "3": # apply blue filter
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.applyBlueFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply blue filter " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "4": # apply sepia filter
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.applySepiaFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply sepia filter " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "5": # apply warm filter
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.applyWarmFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply warm filter " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "6": # apply cold filter
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.applyColdFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply cold filter " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "7": # switch to advanced mode
                print("Log: Performing " + basic[int(userInput)-1])
                state["mode"] = "advanced"
                cmpt120imageProjHelper.showInterface(img, "Advanced Mode " + state["lastOpenFilename"], generateMenu(state))
            else: # unrecognized user input
                print("Log: Unrecognized user input: " + userInput)

        elif state["mode"] == "advanced": # advanced manipulations
            if userInput == "1": # rotate image left
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.rotateLeft(img)
                cmpt120imageProjHelper.showInterface(img, "Rotate image left " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "2": # rotate image right
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.rotateRight(img)
                cmpt120imageProjHelper.showInterface(img, "Rotate image right " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "3": # double the sixe of the image
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.doubleSize(img)
                cmpt120imageProjHelper.showInterface(img, "Double image size " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "4": # half the size of the image
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.halfSize(img)
                cmpt120imageProjHelper.showInterface(img, "Half the image size " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "5": # find the fish in the image
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.locateFish(img)
                cmpt120imageProjHelper.showInterface(img, "Locate fish " + state["lastOpenFilename"], generateMenu(state))
            elif userInput == "6": # switch to basic mode
                print("Log: Performing " + advanced[int(userInput)-1])
                state["mode"] = "basic"
                cmpt120imageProjHelper.showInterface(img, "Basic Mode " + state["lastOpenFilename"], generateMenu(state))
            else: # unrecognized user input
                print("Log: Unrecognized user input: " + userInput)

                # ***TO-DO: use this format when you add the manipulation functionalities***
                # ***instead of setting the value of state["mode"]***
                # ***it is ok to go a bit beyond 100 characters when calling the showUserInterface***
                #img = cmpt120imageManip.applyRedFilter(img)
                #cmpt120imageProjHelper.showUserInterface(img, "Apply Red Filter ", generateMenu(state))

    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return img

# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")