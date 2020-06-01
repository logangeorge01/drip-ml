from flask import Flask, request, render_template, url_for, flash, redirect
from predict import Predict
from werkzeug.utils import secure_filename
import os
import random

app = Flask(__name__)

p = Predict()

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
   return '.' in filename and \
      filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def render_html():
   inits = '0118,0134,0339,0645,0815,0215,1039,1053,0163,0761,0771,0791'.split(',')
   return render_template('init.html', images=inits)


@app.route('/', methods=['POST'])
def make_recs():
   # if 'img' not in request.files:
   #    flash('No file part')
   #    return redirect(request.url)
   # file = request.files['img']
   # if file.filename == '':
   #    flash('No selected file')
   #    return redirect(request.url)
   # if file and allowed_file(file.filename):
   #    img_path = secure_filename(file.filename)
   img_paths = request.form.getlist('imgs')
   print(img_paths)

   recs = []
   for n in img_paths:
      recs+=p.get_recs(f'static/{n}')[0]


   # recs = [p.get_recs(f'static/{n}' for n in img_paths)]
   print('=====')
   print(recs)
   print('=====')
   random.shuffle(recs)

   return render_template('recs.html', images=recs)