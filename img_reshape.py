import cv2
import os
import numpy as np

def reshape_and_write():
    directory = os.listdir('../../test')
    #print(directory)

    for file in directory: 
        img = cv2.imread("../../test/" + file, cv2.IMREAD_COLOR)

        old_image_height, old_image_width, channels = img.shape
        new_image_width = max(old_image_height, old_image_width)
        new_image_height = max(old_image_height, old_image_width)
        color = (0,0,0)

        result = cv2.resize(img, (new_image_width, new_image_height), interpolation = cv2.INTER_LINEAR)

        cv2.imwrite("../../test_reshaped/" + file, result)

def correct_labels():
    directory = os.listdir('./train_old_format')
    #print(directory)

    for file in directory: 
        open_file = open('./train_old_format/'+file,'r')

        output_final=''
        while True:
            next_line = open_file.readline()
            
            data=next_line.split(' ')
            #print(data)
            if len(data)>1:
                x_start=int(data[1])
                y_start=int(data[2])
                width=int(data[3])
                height=int(data[4])

                y_start=int(y_start*(480/360)) #THIS IS THE LINE THAT CHANGES
                height=int(height*(480/360)) #THIS IS THE LINE THAT CHANGES

                x_centre=x_start+width/2
                y_centre=y_start+height/2

                data[1]=str(round( x_centre/480 , 5) )
                data[2]=str(round( y_centre/480, 5) )
                data[3]=str(round(width/480,5) )
                data[4]=str(round(height/480,5) )
                output=''
                output=' '.join(data)
                output_final+=output
                #print(output)

            if not next_line:
                break
        
        open_file.close()
        write_file = open('../../train_YOLO_reshaped/'+file,'w')
        write_file.write(output_final)

def visualize_labels():
    img = cv2.imread("../../train_reshaped/0033.png", cv2.IMREAD_COLOR)
    print(img.shape)

    
    open_file = open('../../train_YOLO_reshaped/0033.txt','r')
   
    next_line = open_file.readline()
    data=next_line.split(' ')
    if len(data)>1:
        
        data[1]=int(float(data[1])*480)
        data[2]=int(float(data[2])*480)
        data[3]=int(float(data[3])*480)
        data[4]=int(float(data[4])*480)
        
        start_point=(int(data[1]-data[3]/2), int(data[2]-data[4]/2))
        end_point=(int(data[1]+data[3]/2), int(data[2]+data[4]/2))

        color = (255, 0, 0)  
        thickness = 2

        print(start_point, end_point)
        img = cv2.rectangle(img, start_point, end_point, color, thickness)


        cv2.imshow("Test img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#reshape_and_write()
#correct_labels()
visualize_labels()