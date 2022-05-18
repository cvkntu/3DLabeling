import cv2 as cv
import numpy as np
import glob
import os
import tools

def test_dataset(calib_dir, image_dir, label_dir):
    "testing the data set, display each image and draw 3D bounding boxes"

    names = [s[:6] for s in os.listdir(calib_dir)]
    names.sort()

    for name in names:
        calib_file = os.path.join(calib_dir, f'{name}.txt')
        image_file = os.path.join(image_dir, f'{name}.png')
        label_file = os.path.join(label_dir, f'{name}.txt')


        I = cv.imread(image_file)


        calib_data = tools.read_calib_file(calib_file)
        label_data = tools.read_3d_label_file(label_file)


        tools.draw_3d_labels(I, calib_data, label_data)
        

        cv.imshow('3D Labels', I)
        if (cv.waitKey() & 0xFF == ord('q')):
            exit()

        

        
        
if __name__ == '__main__':
    calib_dir = 'data_object_calib/training/calib'
    image_dir = 'data_object_image_2/training/image_2'
    label_dir = 'data_object_label_2/training/label_2'

    # calib_dir = 'sample_calib'
    # image_dir = 'sample_image_2'
    # label_dir = 'sample_label_2'

    test_dataset(calib_dir, image_dir, label_dir)

    

    
