# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Salman Ayaz
# Date: Nov. 24, 2021
# Description: A program to do advanced modifications to an image

import cmpt120imageProjHelper
import numpy

##############################################################
## Basic Mode Functions
##############################################################

def applyRedFilter(pixels): # apply red filter
    height = len(pixels)
    width = len(pixels[0])
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            pixels[colum][row][1] = 0
            pixels[colum][row][2] = 0
    return pixels

def applyGreenFilter(pixels): # apply green filter
    height = len(pixels)
    width = len(pixels[0])
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            pixels[colum][row][0] = 0
            pixels[colum][row][2] = 0
    return pixels

def applyBlueFilter(pixels): # apply blue filter
    height = len(pixels)
    width = len(pixels[0])
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            pixels[colum][row][0] = 0
            pixels[colum][row][1] = 0
    return pixels

def applySepiaFilter(pixels): # apply sepia filter
    height = len(pixels)
    width = len(pixels[0])
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            # obtain rgb values
            red = pixels[colum][row][0]
            green = pixels[colum][row][1]
            blue = pixels[colum][row][2]
            # calculate sepia values
            sepiaRed = (red * .393) + (green *.769) + (blue * .189)
            sepiaGreen = (red * .349) + (green *.686) + (blue * .168)
            sepiaBlue = (red * .272) + (green *.534) + (blue * .131)
            # keep sepia values only under 255
            sepiaRed = min(255, int(sepiaRed))
            sepiaGreen = min(255, int(sepiaGreen))
            sepiaBlue = min(255, int(sepiaBlue))
            # replace original pixels
            pixels[colum][row][0] = sepiaRed
            pixels[colum][row][1] = sepiaGreen
            pixels[colum][row][2] = sepiaBlue
    return pixels

def applyWarmFilter(pixels): # apply warm filter
    height = len(pixels)
    width = len(pixels[0])
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            # obtain r and b values
            red = pixels[colum][row][0]
            blue = pixels[colum][row][2]
            # scale up red
            if red < 64:
                red = red/64*80
            elif red > 64 and red < 128:
                red = (red-64)/(128-64) * (160-80) + 80
            else:
                red = (red-128)/(255-128) * (255-160) + 160
            # scale down blue
            if blue < 64:
                blue = blue/64*50
            elif blue > 64 and blue < 128:
                blue = (blue-64)/(128-64) * (100-50) + 50
            else:
                blue = (blue-128)/(255-128) * (255-100) + 100

            pixels[colum][row][0] = red
            pixels[colum][row][2] = blue
    return pixels

def applyColdFilter(pixels): # apply cold filter
    height = len(pixels)
    width = len(pixels[0])
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            # obtain r and b values
            red = pixels[colum][row][0]
            blue = pixels[colum][row][2]
            # scale up blue
            if blue < 64:
                blue = blue/64*80
            elif blue > 64 and blue < 128:
                blue = (blue-64)/(128-64) * (160-80) + 80
            else:
                blue = (blue-128)/(255-128) * (255-160) + 160
            # scale down red
            if red < 64:
                red = red/64*50
            elif red > 64 and red < 128:
                red = (red-64)/(128-64) * (100-50) + 50
            else:
                red = (red-128)/(255-128) * (255-100) + 100

            pixels[colum][row][0] = red
            pixels[colum][row][2] = blue
    return pixels
            
##############################################################
## Advanced Mode Functions
##############################################################

def rotateLeft(pixels): # rotate the image left
    # obtain dimensions of original img
    height = len(pixels)
    width = len(pixels[0])
    # get a blank img with width and height switched
    newImg = cmpt120imageProjHelper.getBlackImage(height, width)
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            # swap pixels
            newImg[width - row - 1][colum] = pixels[colum][row]    
    return newImg

def rotateRight(pixels): # rotate the image right
    # obtain dimensions of original img
    height = len(pixels)
    width = len(pixels[0])
    # get a blank img with width and height switched
    newImg = cmpt120imageProjHelper.getBlackImage(height, width)
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            newImg[row][height - colum - 1] = pixels[colum][row]  
    return newImg

def doubleSize(pixels):
    # obtain dimensions of original img
    height = len(pixels)
    width = len(pixels[0])
    # create a blank img that is double the size of the original
    newImg = cmpt120imageProjHelper.getBlackImage(2*width, 2*height)
    # sort through the colums
    for colum in range(height):
        # sort through the pixels
        for row in range(width):
            # place the original pixels onto the double sixed photo
            newImg[2*colum][2*row] = pixels[colum][row] # bottom right
            newImg[2*colum+1][2*row] = pixels[colum][row] # top right
            newImg[2*colum][2*row+1] = pixels[colum][row] # bottom left
            newImg[2*colum+1][2*row+1] = pixels[colum][row] # top left
    return newImg

def halfSize(pixels):
    # obtain dimensions of original img
    height = len(pixels)
    width = len(pixels[0])
    # create a blank img that is double the size of the original
    newImg = cmpt120imageProjHelper.getBlackImage(int(width/2)-1, int(height/2)-1) # <-- most likely the cause of the index issues
    newHeight = len(newImg)
    newWidth = len(newImg[0])
    # sort through the colums
    for colum in range(newHeight):
        # sort through the pixels
        for row in range(newWidth):
            # calculate the average values of each 2x2 pixel
            averageRed1 = pixels[colum*2][row*2][0] + pixels[colum*2+1][row*2][0]
            averageRed2 = pixels[colum*2][row*2+1][0] + pixels[colum*2+1][row*2+1][0]
            averageRed = (averageRed1 + averageRed2)/4
            averageGreen1 = pixels[colum*2][row*2][1] + pixels[colum*2+1][row*2][1]
            averageGreen2 = pixels[colum*2][row*2+1][1] + pixels[colum*2+1][row*2+1][1]
            averageGreen = (averageGreen1 + averageGreen2)/4
            averageBlue1 = pixels[colum*2][row*2][2] + pixels[colum*2+1][row*2][2]
            averageBlue2 = pixels[colum*2][row*2+1][2] + pixels[colum*2+1][row*2+1][2]
            averageBlue = (averageBlue1 + averageBlue2)/4
            # place the average values onto the image
            newImg[colum][row][0]= averageRed
            newImg[colum][row][1]= averageGreen
            newImg[colum][row][2]= averageBlue
    return newImg

def locateFish(pixels):
    height = len(pixels)
    width = len(pixels[0])
    # define the variables to store the dimensions of the detection box
    maxHeight = height # topmost pixel
    minHeight = 0 # bottommost pixel
    maxHorizontal = 0 # rightmost pixel
    minHorizontal = width # leftmost pixel
    # sort through pixels
    for colum in range(height):
        for row in range(width):
            # obtain rgb values
            red = pixels[colum][row][0]
            green = pixels[colum][row][1]
            blue = pixels[colum][row][2]
            # use rgb values to obtain hsv values
            HSVvalues = cmpt120imageProjHelper.rgb_to_hsv(red, green, blue)
            # detect yellow pixels using hsv
            if HSVvalues[0] > 50 and HSVvalues[1] > 45 and HSVvalues[2] > 95:
                # update min and max variables
                if colum < maxHeight:
                    maxHeight = colum
                if colum > minHeight:
                    minHeight = colum
                if row < minHorizontal:
                    minHorizontal = row
                if row > maxHorizontal:
                    maxHorizontal = row
        # draw the horizontal portions of the detection box
    for i in range(maxHorizontal - minHorizontal):
        pixels[maxHeight][minHorizontal + i] = [0, 255, 0]
        pixels[minHeight][minHorizontal + i] = [0, 255, 0]
    # draw the vertical portions of the detection box
    for i in range(minHeight - maxHeight):
        pixels[maxHeight + i][minHorizontal] = [0, 255, 0]
        pixels[maxHeight + i][maxHorizontal] = [0, 255, 0]
    return pixels

