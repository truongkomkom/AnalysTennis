import numpy as np
import cv2

# Tạo hình ảnh gốc (frame): Một đám mây trên nền bầu trời xanh
frame = np.zeros((200, 200, 3), dtype=np.uint8)
frame[:, :, 0] = 255  # B channel (màu xanh) là 255 (màu xanh)
frame[:, :, 1] = 204  # G channel (màu lục) là 204 (màu lục)
frame[:, :, 2] = 255  # R channel (màu đỏ) là 255 (màu đỏ)
cv2.imshow('frame', frame)
# Tạo hình ảnh shapes: Một hình chữ nhật bán trong suốt nằm ở trung tâm
shapes = np.zeros((200, 200, 3), dtype=np.uint8)
cv2.rectangle(shapes, (50, 50), (150, 150), (255, 255, 255), cv2.FILLED)
cv2.imshow('shapes', shapes)
# Thiết lập alpha (độ trong suốt của hình chữ nhật bán)
alpha = 0.5

# Tạo mặt nạ từ hình ảnh shapes
mask = shapes.astype(bool)
print(mask)
# Kết hợp hai hình ảnh lại với nhau và gán lại vào hình ảnh frame
out = frame.copy()
print(out[mask])
# out[mask] = cv2.addWeighted(frame, alpha, shapes, 1 - alpha, 0)[mask]

# Hiển thị hình ảnh kết quả
cv2.imshow('Result', out)
cv2.waitKey(0)
cv2.destroyAllWindows()