import time
import webbrowser 

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def main(): 
    prng_file = "prng-service.txt"
    image_service = "image-service.txt"

    while True: 
        user_input = input('Enter 1 to generate a new image or 2 to exit: ')

        if user_input == "1":
            with open(prng_file,'w+', 4096) as prng_pipe:
                prng_pipe.write('run')
            time.sleep(5) 
             
            with open(prng_file, "r", 4096) as prng_pipe:
                prng_ln = prng_pipe.readline().strip()
                #print("PRNG Output:", prng_ln) #debug output

            with open(image_service, 'w+', 4096) as imgs_pipe:                
                imgs_pipe.write(prng_ln)            
            time.sleep(5)

            with open(image_service, 'r', 4096) as imgs_pipe:
                imgs_ln = imgs_pipe.readline().strip()
                #print("Image Path:", imgs_ln) #debug print

            #webbrowser.open(imgs_ln)
            webbrowser.get('chrome').open(f'file:///{imgs_ln}')
                    
        elif user_input == "2":
            return 
        else: 
            print('Unknown option! ') 
            
if __name__ == "__main__": 
    main()

