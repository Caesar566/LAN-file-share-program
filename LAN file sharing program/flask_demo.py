from flask import Flask, request, render_template, send_file, url_for
from werkzeug.utils import secure_filename
import os
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
 
@app.route('/upload/',methods=['GET', 'POST'])#装饰器
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('py\\data', filename))
        return '上传成功'
    return render_template('upload.html')

@app.route('/download/',methods=['GET', 'POST'])
def download():
    url_str = ''
    for file in file_read():
        url_str += '<h1>文件列表<h1><li><a href="' + file + '">' + file + '</a></li>\n'
        url_for('file_download', file_name = 'file')
    url_str += '<p><a href="remove">删除</a></p>'
    return url_str

@app.route('/download/remove')
def remove():
        url_str = ''
        for file in file_read():
            url_str += '<h1>点击删除文件<h1><li><a href="remove/' + file + '">' + file + '</a></li>\n'
            url_for('file_remove', file_name = 'file')
        return url_str

@app.route('/download/remove/<file_name>')
def file_remove(file_name):
    shutil.move('py//data//' + file_name,'py//trash')
    return '删除成功'

@app.route('/download/<file_name>')
def file_download(file_name):
    return send_file('data\\'+file_name, as_attachment=True, attachment_filename=file_name)

def file_read():
    file_list = []
    dir = 'py\\data'
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_list.append(os.path.join(file))
    print(file_list)
    return file_list

if __name__ == '__main__':
    app.run(host='192.168.0.106', port=1234)

