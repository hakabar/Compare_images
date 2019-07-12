# Compare_images
Code to compare almost identical images in the same directory against one of them to detect changes in the image by subtracting the mean px values from the images. 

This code has been build to detect in which image/frame insect appears (from a group of images). The background in all the images stay the same.  

User settings must be filled in file configuration_file.py that you will find in this folder

This project will contains 2 python scripts:
  - compare_images_nonCuda.py --> Uses Numpy and CPU to perform the actions.
  - compare_imgaaes_cuda.py --> Uses Numpy and Numba to perform the actions via the GPU. (Script to be added in the future)
