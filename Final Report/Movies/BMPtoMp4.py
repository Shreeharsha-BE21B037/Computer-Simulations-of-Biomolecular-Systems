#!/usr/bin/env python
# coding: utf-8

# In[19]:


get_ipython().system('pip install opencv-python')


# In[18]:


import cv2
import os

# Set the directory containing your BMP image files
image_folder = 'C:\\Users\\shree\\OneDrive\\Desktop\\ACADS\\Bio Simulations\\Final Report\\movies\\Chmx_S631N_1ns_MD\\NC_Ele'

# Get the list of BMP image files in the specified directory
images = [img for img in os.listdir(image_folder) if img.endswith(".bmp")]
frame = cv2.imread(os.path.join(image_folder, images[0]))

# Set the output video file name and codec
output_file = 'Chmx_S631N_Ele.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as needed

# Set the frame size to match the dimensions of the BMP images
height, width, layers = frame.shape
frame_size = (width, height)

# Create the video writer object
out = cv2.VideoWriter(output_file, fourcc, 10, frame_size)  # Adjust the frame rate as needed 

# Loop through the BMP images and add them to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    out.write(frame)

# Release the video writer object
out.release()

print(f"Video '{output_file}' created successfully!")

