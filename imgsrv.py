import time 
import os 

image_service = "image-service.txt"

while True: 
    time.sleep(1) 
    with open(image_service, "r+", 4096) as imgs_pipe:
        content = imgs_pipe.readline().strip() 
        #print("Image Service Read:", content) #Debug print
        
    try:
        content_text = int(content)
        file_img = f'C:/Users/gulpe/OneDrive/Desktop/CS361/A1-MicroservicesWarm-Up/imgs/{content_text}.jpg'
        #print("File path:", file_img) #Debug print
    except ValueError:
        continue
    else:  
        with open(image_service, 'w+', 4096) as imgs_pipe:
            imgs_pipe.write(file_img)
        #print("Image Service Written: ", file_img) # Debug print

