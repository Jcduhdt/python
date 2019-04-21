# # cmd  .\.venvs\lpthw\Scripts\activate 转到虚拟空间
# cmd cd 到存放文件目录
# python easy_hello.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
