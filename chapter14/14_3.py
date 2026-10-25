# 导入视觉库
import cv2
from pathlib import Path

# 车牌识别函数
def detect(img):
    # 设置分类器数据模型文件(已训练好的)
    cascade_path = 'cascade.xml'
    # 用数据模型生成分类器
    cascade = cv2.CascadeClassifier(cascade_path)
    # 设置图片要转换的高度，为改变图片大小做准备
    resize_h = 400
    # 图片在计算机中的存储形式是三维数据
    # img.shape[0]取得矩阵的第一维，第一维的度数(成员数量)决定图片高度，
    # 所以可以理解为获取图片高度
    hh = img.shape[0]
    # 取得图片宽度
    ww = img.shape[1]
    # 取得原始图片宽与高的比值
    ratio = float(ww) / float(hh)
    # 重置图片的大小
    img = cv2.resize(img, (int(ratio * resize_h), resize_h))
    # 转为灰度图，更便于识别
    image_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 车牌定位
    car_plates = cascade.detectMultiScale(image_gray, 1.1, 3, minSize=(20, 10), maxSize=(20*20, 10*40))
    print('检测到车牌数', len(car_plates))
    if len(car_plates) > 0:
        for car_plate in car_plates:
            x, y, width, height = car_plate
            cv2.rectangle(img, (x-8, y-8), x+width, y+height+8, (255, 0, 0), 2)
            img_befor = cv2.resize(img, (ww, hh))
            cv2.imshow('image', img_befor)


# 主函数
if __name__ == '__main__':
    image_path = Path(__file__).parent / 'car_plate.jpeg'
    image = cv2.imread(str(image_path))
    detect(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()