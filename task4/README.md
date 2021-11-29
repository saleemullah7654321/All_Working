
# Task 4
- In this task we have to write parser for via annotator json file to convert  this json data for 
  yolo formate like text file for each image and for unet masked images for training model on our custom
  data using these created masked images. which we create from our via json file using our parser. this
  json is suitable for mrcnn model training. so we write parser for yolo and unet.

# YOLO PARSER
yolo takes text formate as labels. In this text file it takes 5 values:
  - class
  - x position
  - y position
  - width of rectangle
  - height of rectangle
   ```
    def normalize_for_yolo(xmin,ymin,w,h,w_img,h_img):
        xcenter = (xmin + w/2) / w_img
        ycenter = (ymin + h/2) / h_img
        w = w / w_img
        h = h / h_img
        return xcenter,ycenter,w,h
 ```
 this function use for normalize json data values for yolo formate.

 

# UNET PARSER
unet takes masked images as label for image which want to use in training.
all images size should be multiple of 32. I use 512x512, because we use two classes for this task 
- cat
- dog
so during masking the area we need to select different color value for diffect classes. like, [1,1,1]
for cat and [2,2,2] for dog and [0,0,0] for background. Because model detect using these different
color values to distiguish between different classes.
## Installation
1. Install python 
2. Run this command in any terminal on 
your system to clone this repository. 

```terminal
  git clone https://github.com/saleemullah7654321/All_Working.git
  cd All_Working
  python -m pip install -r .\Task2\requirements.txt
```
    
## 🛠 Skills
- Python
- Knowledge of how train custom dataset using any model.

