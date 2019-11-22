#!/usr/bin/env python3

import os
import random
import argparse
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', help='Path of source directory', type=str)
    args = parser.parse_args()

    if args.src is None:
        print("Please specify the source directory and file name")
        exit(1)

    count=0
    success=0
    fin = open(args.src)
    for line in fin:
        line=line.strip()
        if line[0:line.find(".")] == line[line.find(",")+2:len(line)]:
            success+=1
        else:
            print("Mismatch: "+line)
        count+=1;
    fin.close()
    
    print("Accuracy : "+str((float(success)/float(count))*100.00)+"%")
    
    
if __name__ == '__main__':
    main()