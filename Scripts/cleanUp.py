#!/usr/bin/env python3

from PIL import Image, ImageFilter
import statistics as st
import os
import argparse
import cv2


def processImage(image):
    image = image.filter(ImageFilter.SMOOTH_MORE)
    image = image.filter(ImageFilter.SMOOTH_MORE)
    if 'L' != image.mode:
        image = image.convert('L')

    """
    pixel_list=[]

    for column in range(image.size[0]):
        for line in range(image.size[1]):
            pixel_list.append(image.getpixel((column,line)))
            
    factor=round(sum(pixel_list)/len(pixel_list))
    factor=st.mode(pixel_list)
    print(factor)"""

    for column in range(image.size[0]):
        for line in range(image.size[1]):
            if image.getpixel((column,line)) < 200:
                value=0
            else:
                value=255
            image.putpixel((column, line), value)

    return image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', help='Path of source directory', type=str)
    parser.add_argument('--target', help='Path of target directory', type=str)
    args = parser.parse_args()

    if args.src is None:
        print("Please specify the source directory")
        exit(1)

    if args.target is None:
        print("Please specify the target directory")
        exit(1)
        
    for x in os.listdir(args.src):
        image=cv2.imread(os.path.join(args.src, x))
        #processed_image=processImage(image)
        processed_image=cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
        cv2.imwrite(os.path.join(args.target, x),processed_image)
        
if __name__ == '__main__':
    main()