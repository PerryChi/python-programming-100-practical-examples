import cv2
import dlib
from skimage import io
from pathlib import Path

# 检测出人脸并用矩形框标出来
def faceDetector():
    # 生成一个正面人脸检测器
    facedetector = dlib.get_frontal_face_detector()
    # 调用skimage的io子模块读取图片文件
    img = io.imread(Path(__file__).parent / 'face_image.jpeg')
    # 第二个参数 1 表示将图片放大一倍，便于检测到更多人脸
    dets = facedetector(img, 1)
    # 输出人脸数量和坐标
    print(f"共检测出人脸数: {len(dets)}张")
    # OpenCV 使用 BGR 图像格式
    display_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # 循环取得每张脸上的矩形框的坐标，提示: k从0开始计数
    for k, d in enumerate(dets):
        left, top = d.left(), d.top()
        right, bottom = d.right(), d.bottom()

        print(
            f"第{k + 1}张矩形框坐标: "
            f"左: {left} 上: {top} 右: {right} 下: {bottom}"
        )

        # 绘制人脸矩形框
        cv2.rectangle(
            display_img,
            (left, top),
            (right, bottom),
            (0, 0, 255),
            2
        )

    # 显示图像，按任意键退出
    cv2.imshow("Face Detection", display_img)
    try:
        cv2.waitKey(0)
    finally:
        cv2.destroyAllWindows()

# 调用人脸检测函数
faceDetector()