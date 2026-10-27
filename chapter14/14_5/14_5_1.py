from skimage import io
import dlib
from pathlib import Path

# 这个源码是书籍原本代码，但例子已过时，dlib库有些API在新版中不存在了，所以运行会报错
# 请参考14_5_2.py的新实现

# 检测出人脸并用矩形框标出来
def faceDetector():
    # 生成一个正面人脸检测器
    facedetector = dlib.get_frontal_face_detector()
    # 调用skimage的io子模块读取图片文件
    img = io.imread(Path(__file__).parent / 'face_image.jpeg')
    # 生成图形显示窗口（Windows窗口形式）
    vwin = dlib.image_window()
    # 清除窗口中图片上面叠加的图片
    vwin.clear_overlay()
    # 把读入的图片显示到窗口
    vwin.set_image(img)
    # 第二个参数 1 表示将图片放大一倍，便于检测到更多人脸
    dets = facedetector(img, 1)
    # 在人脸上绘制矩阵
    vwin.add_overlay(dets)
    # 打印检测出的人脸信息
    print('共检测出人脸数: {}张'.format(len(dets)))
    # 循环取得每张脸上的矩形框的坐标，提示: k从0开始计数
    for k, d in enumerate(dets):
        print('第{}张矩形框坐标: 左: {} 上: {} 右: {} 下: {}'.format(
            k+1, d.left(), d.top(), d.right(), d.bottom()
        ))

    # 等待用户按回车键，退出函数
    dlib.hit_enter_to_continue()

# 调用人脸检测函数
faceDetector()