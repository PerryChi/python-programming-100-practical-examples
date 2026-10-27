import cv2
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
    # 现在并解压到当前目录
    predictor = dlib.shape_predictor(model_path)
    # 调用skimage的io子模块读取图片文件
    img = io.imread(Path(__file__).parent / 'face_image.jpeg')
    # 第二个参数 1 表示将图片放大一倍，便于检测到更多人脸
    dets = facedetector(img, 1)
    # OpenCV 使用 BGR 图像格式
    display_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # 循环取得每张脸上轮廓特征，并在脸上绘出轮廓
    for k, d in enumerate(dets):
        # 绘制人脸矩形框
        cv2.rectangle(
            display_img,
            (d.left(), d.top()),
            (d.right(), d.bottom()),
            (0, 255, 0),
            2
        )
        # 预测人脸的 68 个关键点
        shape = predictor(img, d)
        # 绘制关键点
        for i in range(shape.num_parts):
            x = shape.part(i).x
            y = shape.part(i).y
            cv2.circle(display_img, (x, y), 2, (0, 0, 255), -1)


    # 显示图像，按任意键退出
    cv2.imshow("Face Detection", display_img)
    try:
        cv2.waitKey(0)
    finally:
        cv2.destroyAllWindows()

# 调用人脸检测函数
facelandmark()