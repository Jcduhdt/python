# cmd  .\.venvs\lpthw\Scripts\activate 转到虚拟空间
# cmd cd 到存放文件目录
# python hello_name.py
# 浏览器打开 http://127.0.0.1:5000/hello
# 把Zhang改成任意就可以看见对你的输入进行hello
# 打开http://127.0.0.1:5000/hello?name=Zhang
from flask import Flask
from flask import render_template
from flask import request
# 这个函数知道如何去template/目录加载模板.html文件，这是flask的默认设置
# render 渲染
app = Flask(__name__)

# python中的装饰器 以 @ 开头
# 装饰器只是一种接受函数的函数，并返回一个新函数
@app.route('/hello')# 匹配路径
def index():
    # request.args.get()从浏览器获取数据 键=值
    # Nobody时默认值，不修改url就会显示这个
    name = request.args.get('name','Nobody')

    if name:
        # f"Hello,{name}"似乎不行了 我用了会报错
        greeting = "Hello, {}".format(name)
    else:
        greeting = "Hello World!"
    # 向模板(template)提供参数 html中出项greeting的位置都是传递给模板的变量
    return render_template("index.html",greeting = greeting)

if __name__ == "__main__":
    app.run()
