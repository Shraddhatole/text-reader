from PIL import Image
import pytesseract as pt
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def main():
    # path for the folder for getting the raw images
    path = "D:/images4"
    # path for the folder for getting the output
    tempPath = "D:/images4/textFiles"
    # iterating the images inside the folder
    for imageName in os.listdir(path):
        print("-----------------------------")

        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)

        # applying ocr using pytesseract for python
        text = pt.image_to_string(img, lang="jpn")

        # for removing the .jpg from the imagePath
        imageName = imageName[0:-4]

        fullTempPath = os.path.join(tempPath, imageName + ".txt")
        print(text)

        # saving the  text for every image in a separate .txt file
        file1 = open(fullTempPath, "w", encoding='utf-8')
        file1.write(text)
        file1.close()


if __name__ == '__main__':
    main()