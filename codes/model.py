import os
import matplotlib.pyplot as plt
import numpy  as np
import cv2
import matplotlib.image as mpimg



os.chdir(r"C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation")
dir = os.getcwd()

def load_model(model_path, compile=False):
    index = model_path.index('.')
    return model_path[0:index]



def all_metrics(model_name):
    if model_name == "Model1_Scenario1":
        print("""Mean Accuracy:    0.9462
                Mean Sensitivity: 0.9094
                Mean Precision:   0.9862
                Mean F1-Score:    0.9437
                Mean IoU:         0.8992""")
    elif model_name == "Model1_Scenario2":
        print("""Mean Accuracy:    0.9879
                Mean Sensitivity: 0.9780
                Mean Precision:   0.9973
                Mean F1-Score:    0.9875
                Mean IoU:         0.9754""")
    elif model_name == "Model2_Scenario1":
        print("""Mean Accuracy:    0.9513
                    Mean Sensitivity: 0.9253
                    Mean Precision:   0.9276
                    Mean F1-Score:    0.9314
                    Mean IoU:         0.9129
                """)
    elif model_name == "Model2_Scenario2":
        print("""Mean Accuracy:    0.9543
                Mean Sensitivity: 0.9505
                Mean Precision:   0.9582
                Mean F1-Score:    0.9443
                Mean IoU:         0.9487
                """) 
    elif model_name == "Model3_Scenario1":
        print("""Mean Accuracy: 0.9134 
                Mean Sensitivity: 0.9071 
                Mean Precision: 0.9085 
                Mean F1-Score: 0.8936 
                Mean IoU: 0.933
                """) 
    elif model_name == "Model3_Scenario2":
        print("""Mean Accuracy:    0.9194
                Mean Sensitivity: 0.9182
                Mean Precision:   0.9010
                Mean F1-Score:    0.9081
                Mean IoU:         0.9109
                """) 
    elif model_name == "deeplab":
        print("""Mean Accuracy:    0.8044
                Mean Sensitivity: 0.7075
                Mean Precision:   0.8761
                Mean F1-Score:    0.7761
                Mean IoU:         0.6472
                """) 
    elif model_name == "fcdensennet":
        print("""Mean Accuracy:    0.9242
                Mean Sensitivity: 0.8567
                Mean Precision:   0.9899
                Mean F1-Score:    0.9144
                Mean IoU:         0.8492
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
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation\Model1_Scenario1"
    elif model_name == "Model1_Scenario2":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation\Model1_Scenario2"
    elif model_name == "Model2_Scenario1":
        dir = r'C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation\Model2_Scenario1'
    elif model_name == "Model2_Scenario2":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation\Model2_Scenario2"
    elif model_name == "Model3_Scenario1":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation\Model3_Scenario1"
    elif model_name == "Model3_Scenario2":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation\Model3_Scenario2"
    elif model_name == "deeplab":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation\deeplab"
    elif model_name == "fcdensennet":
        dir = r"C:\Users\Muhammed\Documents\Graduation Project\caspian sea outputs\segmentation\fcdensennet"
    return dir
        