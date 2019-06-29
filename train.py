import numpy as np
import cv2
import pickle

class Weights(object):
    def __init__(self, array):
        self.weights = array

def train():
    print("IN MAIN")
    init_w = np.zeros(250000, dtype="uint8")
    init_del_w1 = []
    init_del_w2 = []
    im_x = cv2.imread('train/x.jpg', cv2.IMREAD_GRAYSCALE)
    im_o = cv2.imread('train/o.jpg', cv2.IMREAD_GRAYSCALE)

    # CALCULATE DEL W
    for i in im_x:
        for j in i:
            if j>128:
                init_del_w1.append(-1)
            else:
                init_del_w1.append(1)

    # UPDATE WEIGHTS
    print("Updating Weights for X")
    for index, w in enumerate(init_del_w1):
        init_w[index] += w

    # CALCULATE DEL W
    for i in im_o:
        for j in i:
            if j>128:
                init_del_w2.append(1)
            else:
                init_del_w2.append(-1)

    # UPDATE WEIGHTS
    print("Updating Weights for O")
    for index, w in enumerate(init_del_w2):
        init_w[index] += w


    with open('weights/x_o.pkl', 'wb') as output:
        weights = Weights(init_w)
        print("Writing weights to Pickle file")
        pickle.dump(weights, output, pickle.HIGHEST_PROTOCOL)

    print("DONE")
                

if __name__ == '__main__':
    train()