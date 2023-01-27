import math
import random


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2

    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2

    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


def leibniz(terms):
    acc = 0
    num = 4    #numerator is constant
    den = 1     #denominator starts at 1

    for aTerm in range(terms):
        nextTerm = num / den
        if (aTerm%2==1):
             nextTerm = nextTerm * (-1)
        acc = acc + nextTerm    #add term to accumulator
        den = den + 2                  #prepare for next term
    return acc


def wallis(pairs):
    acc = 1
    num = 2  # numerator starts at 2
    for aPair in range(pairs):
        leftTerm = num / (num - 1)  # denominator is numerator - 1
        rightTerm = num / (num + 1)  # denominator is numerator + 1

        acc = acc * leftTerm * rightTerm  # compute running product

        num = num + 2  # prepare for next term

    pi = acc * 2
    return pi


def montePi(numDarts):
    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = rendom.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts *4
    return pi