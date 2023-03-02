from doubleimage import *
from edgedetection import *
from negative import *
from verticalflip import *

if __name__ == '__main__':
    castle = "castle.gif"

    makeDoubleImage(castle)

    makeEdgeDetection(castle)

    makeNegative(castle)

    verticalflip(castle)
