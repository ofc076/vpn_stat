# -*- coding: utf-8 -*-

from flask import Flask
from flask import request, render_template, url_for
from flask import Response, redirect, abort

import os
import subprocess
import time
from vpn_settings import *


app = Flask(__name__)
app.secret_key = 'ofc076_flask_secret_key'


# def readHtmlFromFile():
#     with open(os.path.join(workDir, outputFile), 'r', encoding="utf8") as myfile:
#         data = myfile.read()
#     return data


def getContent():
    x = []
    with open(STATUS_FILE_PATH,'r') as f:
        for line in f:
            x.append(line)
    print(' res = {}'.format(x))
    res = []
    for line in x:
        if '---------' in line:
            continue
        res.append(line)
    return res

def createReport():
    _ = subprocess.Popen([STATUS_CMD], shell=True).pid
    return

@app.route('/')
def hello_world():
#    print(db.session)
#    print(app.config)
    createReport()
    time.sleep(2)
    draft_content = getContent()
    table_head = draft_content[0].replace('\n','')
    content = []
    for line in draft_content[1:]:
        line_dict = {}
        parsed_line = line.split('|')
        line_dict['as_name'] = parsed_line[0].strip()
        line_dict['vpn_name'] = parsed_line[1].strip()
        line_dict['vpn_ip'] = parsed_line[2].strip()
        line_dict['last_upd'] = parsed_line[3].strip()
        if line_dict['vpn_name'][:2] in GET_SOUND:
            line_dict['link'] = '/dload/list_to_rec.py'
        else:
            line_dict['link'] = ''
        content.append(line_dict)

    return render_template('base.html', content_arr=content, table_head=table_head), 200, add_headers_http(REFRESH_TIME, request, redirect='')


@app.errorhandler(404)
def page_not_found(e):
    newUrl = request.url_root + url_for('hello_world')[1:]
    if DEV:
        print(newUrl)
    return render_template('base.html', content_arr='page not found :(('), 404, add_headers_http(REFRESH_TIME, request, redirect=newUrl)

#@app.errorhandler(500)
#def page_not_found(e):
#    newUrl = request.url_root + url_for('hello_world')[1:]
#    if DEV:
#        print(newUrl)
#    return render_template('base.html', content_arr='error 500 :(('), 5000, add_headers_http(REFRESH_TIME, request, redirect=newUrl)


def add_headers_http(refresh, request, redirect=''):
    if redirect == '':
        redirect = request.url
    if DEV:
        print(request.url)
    return {'Content-type':'text/html; charset=utf-8', 'Refresh':'{}; url={}'.format(refresh, redirect)}


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
