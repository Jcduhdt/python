# 我只有.py才能实现
# 用.ipynb它不会显示时间，也不能中断，还是要学习啊
import time

print("按下回车开始计时，按下Ctrl+C 停止计时")
while True:
    try:
        input()
        starttime = time.time()
        print("开始")
        while True:
            print("计时：",round(time.time() - starttime,0),'秒',end = '\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总时间：', round(endtime - starttime,2), 'secs')
        break
