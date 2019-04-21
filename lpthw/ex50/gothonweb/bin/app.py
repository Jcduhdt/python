# cmd  .\.venvs\lpthw\Scripts\activate 转到虚拟空间
# cmd cd 到存放文件目录
# python app.py
# html 居然没注释成功！！
from flask import Flask
from flask import render_template
# 这个函数知道如何去template/目录加载模板.html文件，这是flask的默认设置
# render 渲染
app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello World!"
    # 向模板(template)提供参数 html中出项greeting的位置都是传递给模板的变量
    return render_template("index.html",greeting = greeting)

if __name__ == "__main__":
    app.run()
