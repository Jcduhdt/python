from PIL import Image

'''
@Time 2020-1-2
@author zhangxiong
@software pycharm
将图片用字符画显示

核心： 字符和像素点的灰度值建立映射
为啥我的字符图看起来不行啊
'''

# image_file = Image.open(r'E:/picture/1.jpg')
# w, h = image_file.size
# # 缩放
# image_file.thumbnail((w//2, h//2))
# image_file1 = image_file.convert('L')  # 黑白
# image_file1.show()
# image_file1.save('E:/picture/2.jpg')

codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}【】?-_+~<>i!lI;:,"^`'. '''
count = len(codeLib)


def transform(image_file):
    image_file = image_file.convert('L')  # 转成黑白
    codePic = ''
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            # 灰度
            gray = image_file.getpixel((w, h))
            codePic = codePic + codeLib[int((count * gray) / 256)]  # 找到每个像素点对应的字符集的位置，并对嘴硬字符串进行拼接
        codePic = codePic + '\r\n'  # 加上回车换行 两个不一样
    print(codePic)
    return codePic


if __name__ == "__main__":
    # 打开图像
    # fp = open(r'E:/picture/0.jpg')
    image_file = Image.open('E:/picture/2.jpg')
    image_file.show()
    # 调整图片大小
    image_file = image_file.resize((int(image_file.size[0] * 0.5), int(image_file.size[1] * 0.25)))
    # 打开文本文件
    tmp = open('E:/picture/demo.txt', 'w')
    tmp.write(transform(image_file))
    tmp.close()
