import numpy as np
import cv2
import pickle
import sys

class Weights(object):
    def __init__(self, array):
        self.weights = array

def test():
    filename = sys.argv[1]
    print("Filename : ", filename)

    with open('weights/x_o.pkl', 'rb') as input:
        dump = pickle.load(input)
        print("Loading Weight Files")
        weights = dump.weights

    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (500, 500))
    
    print('Putting Image through the net')

    img_w = []

    for i in img:
        for j in i:
            if j>128:
                img_w.append(-1)
            else:
                img_w.append(1)

    f_y = 0

    for index, w in enumerate(weights):
        f_y += w * img_w[index]

    if f_y >= 0:
        print("The image given is O")
    else:
        print("The image given is X")


if __name__ == '__main__':
    test()