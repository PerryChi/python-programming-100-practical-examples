import dlib
from skimage import io
from pathlib import Path

# 本节编程实例的功能是在上一节检测出的人脸上画出眉毛 眼睛鼻子和嘴的轮廓
# 检测出人脸，绘制出人脸轮廓
def facelandmark():
    # 生成一个正面人脸检测器
    facedetector = dlib.get_frontal_face_detector()
    # 生成人脸特征预测器对象，进行人脸面部轮廓特征提取
    # 运用已训练好的模型数据进行特征训练
    # 下载地址： https://dlib.net/files/shape_predictor_68_facelandmarks.dat.bz2
    # 现在并解压到当前目录
    model_path = str(
        Path(__file__).parent
            / 'shape_predictor_68_face_landmarks.dat'
        )
    predictor = dlib.shape_predictor(model_path)
    # 调用skimage的io子模块读取图片文件
    img = io.imread(Path(__file__).parent / 'face_image.jpeg')
        # 生成图形显示窗口（Windows窗口形式）
    vwindow = dlib.image_window()
    # 把读入的图片显示到窗口
    vwindow.set_image(img)
    # 第二个参数 1 表示将图片放大一倍，便于检测到更多人脸
    dets = facedetector(img, 1)
    # 循环取得每张脸上轮廓特征，并在脸上绘出轮廓
    for k, d in enumerate(dets):
        # 获取每张脸上轮廓特征，每张脸提取68个点的数据，轮廓特征由这些数据生成
        shape = predictor(img, d)
        # 在人脸上绘制轮廓
        vwindow.add_overlay(shape)
    # 在人脸上绘制矩形
    vwindow.add_overlay(dets)
    dlib.hit_enter_to_continue()


# 调用人脸检测函数
facelandmark()