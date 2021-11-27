
# Task 3
- Pakistani id card image data extraction using easyocr and harrcascade-classifier

## EasyOcr Model
How to extract text from images using EasyOCR Python Library (Deep Learning) OCR 
provides us with different ways to see an image, find and recognize the text in it.
When we think about OCR, we inevitably think of lots of paperwork - bank cheques and legal
documents, text present in number plate and street signs. In our case, we will try to predict
the text of ID cards. EasyOCR is implemented using Python and the PyTorch library. If you have
a CUDA-capable GPU, the underlying PyTorch deep learning library can speed up your 
text detection and OCR speed tremendously. As of this writing, EasyOCR can OCR text in 58 languages,
including English, German, Hindi, Russian, and more!

- Use flask for web view. app.py is enterypoint, It contains all routes we use in this api.
- Run app.py file to start server.
  ```terminal
  python app.py
  ```
- When server started it shows http://127.0.0.1:5000/ this ip adderess. By clicking this, web page 
  will open as shown in screenshots page1.
- By clicking open camera button, It redirect to page 2 shown in screenshots. Here video will start
  recording. you have to show your id card infront of camera. after takes some clean frame you need
  to press close camera button.
- By pressing close button it redirect to page 3 as shown in screenshots. It take time to process
  extraction functionality. It's time taken is depend on 2 factors, 1st is length of video. It takes
  too much time if video is lengthy. 2nd factor is if it extract all data from your few frames.
  then it will show you quick result.
- video should be small enough with clean recording or using good quality camera for fast response.
## Installation
1. Install python 
2. Run this command in any terminal on 
your system to clone this repository. 

```terminal
  git clone https://github.com/saleemullah7654321/All_Working.git
  cd All_Working
  python -m pip install -r .\Task3\requirements.txt
```
    
## 🛠 Skills
python


## Screenshots

### Page 1
![page1](https://raw.githubusercontent.com/saleemullah7654321/All_Working/master/Task3/screenshots/page1.PNG)
### Page 2
![page1](https://raw.githubusercontent.com/saleemullah7654321/All_Working/master/Task3/screenshots/page2.PNG)
### Page 3
![page1](https://raw.githubusercontent.com/saleemullah7654321/All_Working/master/Task3/screenshots/page3.PNG)

