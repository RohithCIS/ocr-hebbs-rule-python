# OCR using Hebb's Learning Rule
## Differentiates only between 'X' and 'O'


Dependencies
    
    python3
    pip3
    numpy
    opencv
    pickle

Setup

    ## If you are using Anaconda you can skip these steps

    #On Linux - Debian
    sudo apt-get install python3 python3-pip
    pip3 install numpy opencv-python

    #On Linux - Arch
    sudo pacman -Sy python python-pip
    pip install numpy opencv-python

    #On Mac
    sudo brew install python3 python3-pip
    pip3 install numpy opencv-python

    #On Windows
    #Download and Install python3 bundle
    # https://www.python.org/downloads/windows/
    pip3 install numpy opencv-python

Usage

    #Put the images for training in the ./train folder as x.jpg and o.jpg
    python3 train.py

    #Test images need to be place in ./test folder
    python3 test.py test/filename.ext

Author

    Rohith Balaji
    
    b.rohith2015@vit.ac.in
    me@therohith.com

    https://therohith.com