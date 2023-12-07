import numpy as np
import cv2
from pyzbar.pyzbar import decode

def detect_qr_and_barcode(frame):
    # 이미지 전처리를 위해 Gaussian 블러 적용
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # OpenCV를 사용하여 QR 코드 및 바코드 찾기
    decoded_objects = decode(blurred_frame)

    for obj in decoded_objects:
        barcode_data = obj.data.decode('utf-8')
        obj_type = obj.type
        points = obj.polygon

        # 바코드 또는 QR 코드 주변에 윤곽선 그리기
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = hull.astype(int)  # hull의 좌표를 정수로 변환
            cv2.polylines(frame, [hull], True, (0, 0, 255), 3)
        else:
            points = np.array(points, dtype=np.int32)  # points의 좌표를 정수로 변환
            for j in range(len(points)):
                cv2.line(frame, tuple(points[j]), tuple(points[(j+1) % len(points)]), (0, 0, 255), 3)

        # 화면에 바코드 또는 QR 코드 정보 출력
        cv2.putText(frame, f"{obj_type}: {barcode_data}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 4, cv2.LINE_AA)

    return frame, decoded_objects