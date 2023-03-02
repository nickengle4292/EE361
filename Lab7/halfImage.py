from cImage import *


def halfImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW // 2, oldH // 2)

    for row in range(0, oldH, 2):
        for col in range(0, oldW, 2):
            oldPixel = oldImage.getPixel(col, row)

            newIm.setPixel(col // 2, row // 2, oldPixel)

    return newIm


def makeHalfImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Half Image", width * 2, height)
    oldImage.draw(myWin)

    newImage = halfImage(oldImage)
    newImage.setPosition(width + 1, 0)
    newImage.draw(myWin)

    myWin.exitOnClick()


if __name__ == '__main__':
    makeHalfImage('castle.gif')
