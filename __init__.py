import sys
import os

# This is a trick that allows for all the submodules in yolov5 to find each other
sys.path.append(os.getcwd() + "/" + __name__)
