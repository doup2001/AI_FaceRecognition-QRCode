import cv2
import numpy as np
from utils import detect
from utils import face
from utils import opens
from utils import mosaic

# qr코드 / 바코드 / 얼굴 인식이 가능한 프로그램.
# 얼굴 인식 후

clicked_coordinates = []

def mouse_callback(event, x, y, flags, param):
    # 왼쪽 마우스 클릭 이벤트 처리
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_coordinates.append((x, y))
        print(f"Clicked coordinates: {x}, {y}")
        # return x, y

if __name__ == "__main__":
    # 카메라 캡처 설정
    cap = cv2.VideoCapture(0)

    # 마우스 이벤트 콜백 함수 등록
    cv2.namedWindow("QR and Barcode Detection")
    cv2.setMouseCallback("QR and Barcode Detection", mouse_callback)

    while True:
        # 카메라에서 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            break

        # QR 코드 및 바코드 찾기
        frame_with_detection, decoded_objects = detect.detect_qr_and_barcode(frame)
        
        # 얼굴 찾기
        frame_with_faces, faces = face.detect_faces(frame.copy())
	
	# 얼굴에 모자이크 적용
	frame_with_faces_mosaic = mosaic_faces(frame_with_faces, faces)
        
        # 결과 화면에 표시
        cv2.imshow("QR and Barcode Detection", frame_with_detection)

        # 클릭한 좌표를 확인하고 해당하는 QR 코드의 URL을 열기
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif clicked_coordinates:
            x, y = clicked_coordinates.pop(0)
            for obj in decoded_objects:
                points = obj.polygon
                if len(points) == 4 and cv2.pointPolygonTest(np.array(points, dtype=np.int32), (x, y), False) == 1:
                    url = obj.data.decode('utf-8')
                    opens.open_browser(url)

    # 사용한 자원 해제
    cap.release()
    cv2.destroyAllWindows()
