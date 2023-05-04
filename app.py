import subprocess
import sys

from flask import Flask,render_template,request
import pickle
import numpy as np
import shutil
from PIL import Image
import os
import psutil

#path for English
# src0_path = r"D:/captured/saved_img.jpg"
# dst0_path = r"D:/images5/saved_img.jpg"

#path for English
src1_path = r"F:/APP FOR BOOK READER_Final/Eng.png"
dst1_path = r"D:/images2/Eng.png"

#path for Hindi
src2_path = r"F:/APP FOR BOOK READER_Final/Hin.png"
dst2_path = r"D:/images/Hin.png"

#path for Japanese
src3_path = r"F:/APP FOR BOOK READER_Final/Jap.png"
dst3_path = r"D:/images4/Jap.png"

#path for Russian
src4_path = r"F:/APP FOR BOOK READER_Final/Rus.png"
dst4_path = r"D:/images3/Rus.png"

app = Flask('__name__')
model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')



def robot():
    return render_template('robot.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        shutil.move(src1_path, dst1_path)
        return render_template('index.html')

@app.route('/success2', methods=['POST'])
def success2():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        shutil.move(src2_path, dst2_path)
        return render_template('index.html')

@app.route('/success3', methods=['POST'])
def success3():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        shutil.move(src3_path, dst3_path)
        return render_template('index.html')

@app.route('/success4', methods=['POST'])
def success4():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        shutil.move(src4_path, dst4_path)
        return render_template('index.html')

# video capture

@app.route('/predict_video',methods=["POST"])
def predict_video():
    with open("video capture.py") as f:
        exec(f.read())
    os.system("video_ocr.py 1")
    # with open("model5.py") as f:
    #     exec(f.read())
    # feature=[int(x) for x in request.form.values()]
    # feature_final=np.array(feature).reshape(-1,1)
    # prediction=model.predict(feature_final)
    # return render_template('index.html',prediction_text='Price of House will be Rs. {}'.format(int(prediction)))
    return render_template('index.html', prediction_text0='Video captured')

@app.route('/read_video',methods=["POST"])
def read_video():

    with open("model5.py") as f:
        exec(f.read())
    feature=[int(x) for x in request.form.values()]
    # feature_final=np.array(feature).reshape(-1,1)
    # prediction=model.predict(feature_final)
    # return render_template('index.html',prediction_text='Price of House will be Rs. {}'.format(int(prediction)))
    return render_template('index.html')




#English

@app.route('/predict',methods=["POST"])
def predict():
    os.system("ocr_english.py 1")
    with open("model2.py") as f:
        exec(f.read())
    # feature=[int(x) for x in request.form.values()]
    # feature_final=np.array(feature).reshape(-1,1)
    # prediction=model.predict(feature_final)
    # return render_template('index.html',prediction_text='Price of House will be Rs. {}'.format(int(prediction)))
    # return render_template('index.html', prediction_text='English text reading')
    return render_template('index.html')

#Hindi
@app.route('/predict2',methods=["POST"])
def predict2():
    os.system("ocr_hindi.py 1")
    with open("model.py") as f:
        exec(f.read())
    return render_template('index.html')

# japanese
@app.route('/predict3',methods=["POST"])
def predict3():
    os.system("ocr_japan.py 1")
    with open("model4.py") as f:
        exec(f.read())
    # feature=[int(x) for x in request.form.values()]
    # feature_final=np.array(feature).reshape(-1,1)
    # prediction=model.predict(feature_final)
    # return render_template('index.html',prediction_text='Price of House will be Rs. {}'.format(int(prediction)))
    return render_template('index.html')

# russian

@app.route('/predict4',methods=["POST"])
def predict4():
    os.system("ocr_russia.py 1")
    with open("model3.py") as f:
        exec(f.read())
    # feature=[int(x) for x in request.form.values()]
    # feature_final=np.array(feature).reshape(-1,1)
    # prediction=model.predict(feature_final)
    # return render_template('index.html',prediction_text='Price of House will be Rs. {}'.format(int(prediction)))
    return render_template('index.html')

if(__name__=='__main__'):
    app.run(debug=True)

