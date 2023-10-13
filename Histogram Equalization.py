import cv2
import numpy as np

# 讀取圖片
image = cv2.imread('圖片名稱.jpg')

# 轉換為灰度圖
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用閾值處理找到非黑色區域
_, thresholded = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)

# 找到非黑色區域的輪廓
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 創建一個與原圖相同大小的黑色圖像
result = np.zeros_like(image)

# 對每個非黑色區域，將其填充到結果圖像中
for contour in contours:
    cv2.drawContours(result, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

# 將結果圖像轉為灰度
result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

# 對結果圖像進行直方圖均衡化
result_equalized = cv2.equalizeHist(result_gray)

# 顯示結果-這邊可有可無，我只想看看
cv2.imshow('Processed Image', result_equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存結果
cv2.imwrite('output_image.jpg', result_equalized)

