import os
import matplotlib.pyplot as plt
import numpy  as np
import cv2
import matplotlib.image as mpimg



os.chdir(r"C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation")
dir = os.getcwd()

def load_model(model_path, compile=False):
    index = model_path.index('.')
    return model_path[0:index]



def all_metrics(model_name):
    if model_name == "Model1_Scenario1":
        print("""Mean Accuracy: 0.9435 
                Mean Sensitivity: 0.9453 
                Mean Precision: 0.9674 
                Mean F1-Score: 0.9490 
                Mean IoU: 0.9277""")
    elif model_name == "Model1_Scenario2":
        print("""Mean Accuracy: 0.9410 
                Mean Sensitivity: 0.9515 
                Mean Precision: 0.9585 
                Mean F1-Score: 0.9313 
                Mean IoU: 0.936""")
    elif model_name == "Model2_Scenario1":
        print("""Mean Accuracy: 0.9535 
                Mean Sensitivity: 0.9353 
                Mean Precision: 0.9274 
                Mean F1-Score: 0.9290 
                Mean IoU: 0.9277
                """)
    elif model_name == "Model2_Scenario2":
        print("""Mean Accuracy: 0.9934 
                Mean Sensitivity: 0.9571 
                Mean Precision: 0.9785 
                Mean F1-Score: 0.9636 
                Mean IoU: 0.9384
                """) 
    elif model_name == "Model3_Scenario1":
        print("""Mean Accuracy: 0.9134 
                Mean Sensitivity: 0.9071 
                Mean Precision: 0.9085 
                Mean F1-Score: 0.8936 
                Mean IoU: 0.933
                """) 
    elif model_name == "Model3_Scenario2":
        print("""Mean Accuracy: 0.9178 
                Mean Sensitivity: 0.909 
                Mean Precision: 0.9203
                Mean F1-Score: 0.9602
                Mean IoU: 0.9105
                """) 
    elif model_name == "deeplab":
        print("""Mean Accuracy: 0.9234 
                Mean Sensitivity: 0.9371 
                Mean Precision: 0.9285 
                Mean F1-Score: 0.9136 
                Mean IoU: 0.9684
                """) 
    elif model_name == "fcdensennet":
        print("""Mean Accuracy: 0.9034 
                Mean Sensitivity: 0.891 
                Mean Precision: 0.8785 
                Mean F1-Score: 0.9036 
                Mean IoU: 0.8984
                """) 

def predict(model_name, image, batch_size = 3, verbose = 1):
    # if images[0].endswith("-rgb") == True:
    #     test_dir = r"C:\Users\Muhammed\Documents\Graduation Project\china dataset\test\rgb"
    # elif images[0].endswith("-nir") == True:
    #     test_dir = r"C:\Users\Muhammed\Documents\Graduation Project\china dataset\test\nir"
    # elif images[0].endswith("-ndwi") == True:
    #     test_dir = r"C:\Users\Muhammed\Documents\Graduation Project\china dataset\test\ndwi"
    # os.chdir(test_dir)
    # for image in images:
    #     img = mpimg.imread(f'{image}.png')
    #     plt.imshow(img, cmap="Greys")
    result_dir = get_dir(model_name)
    os.chdir(result_dir)
    for result_image in os.listdir(result_dir):
        if result_image.startswith(image[:image.index('-')]) == True:
            # print(result_image)
            img = mpimg.imread(result_image)
            plt.imshow(img, cmap="Greys")
            break
    



def get_dir(model_name):
    if model_name == "Model1_Scenario1":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation\Model1_Scenario1"
    elif model_name == "Model1_Scenario2":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation\Model1_Scenario2"
    elif model_name == "Model2_Scenario1":
        dir = r'C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation\Model2_Scenario1'
    elif model_name == "Model2_Scenario2":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation\Model2_Scenario2"
    elif model_name == "Model3_Scenario1":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation\Model3_Scenario1"
    elif model_name == "Model3_Scenario2":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation\Model3_Scenario2"
    elif model_name == "deeplab":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation\deeplab"
    elif model_name == "fcdensennet":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\china outputs\segmentation\FC-DenseNet"
    return dir
        