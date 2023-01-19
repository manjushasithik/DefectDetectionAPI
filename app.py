"""
Simple app to upload an image via a web form 
and view the inference results on the image in the browser.
"""
from subprocess import STDOUT, check_call , call

check_call(['apt-get', 'update'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
check_call(['apt-get', 'install', '-y', 'libgl1'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
check_call(['apt-get', 'install', '-y', 'libglib2.0-0'], stdout=open(os.devnull,'wb'), stderr=STDOUT)

check_call([ 'apt-get', 'update','-y'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
check_call([ 'apt-get', 'install' ,'-y','abiword'], stdout=open(os.devnull,'wb'), stderr=STDOUT)

import argparse
import io
import math
import os
from PIL import Image
from flask_cors import CORS
import numpy as np
from base64 import b64encode
#import pythoncom
import itertools

import base64
import torch
import logging
#import azure.functions as func
import tempfile
from os import listdir

import pandas as pd

import openpyxl
from flask import Flask, render_template, request, redirect,jsonify,send_file

#from w3lib.url import parse_data_uri

from app_func import *

import os
import json
#from docx2pdf import convert
from docx import Document # for pdf format
from docx.shared import Pt # for pdf format
from docx.shared import Inches
#from docx2pdf import convert # for pdf format
#from msoffice2pdf import convert #for pdf format
#import pythoncom # for pdf format
app = Flask(__name__)
CORS(app)
# check_call(['apt-get', 'update'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
# check_call(['apt-get', 'install', '-y', 'libgl1'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
# check_call(['apt-get', 'install', '-y', 'libglib2.0-0'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
# check_call([ 'apt-get', 'update','-y'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
# check_call([ 'apt-get', 'install' ,'-y','abiword'], stdout=open(os.devnull,'wb'), stderr=STDOUT)


@app.route("/", methods=["POST"])
def call_func():
    return predict()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=8000, type=int, help="port number")
    args = parser.parse_args()
    
   # detect.run(weights='yolov5s.pt', save_txt= True)
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat
