import cv2
from utils import detect

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
    cap = cv2.VideoCapture(1)

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
        
        # 결과 화면에 표시
        cv2.imshow("QR and Barcode Detection", frame_with_detection)

        # 키 입력 대기
        key = cv2.waitKey(1)
        if key in (27, ord('q')):  # ESC 키 또는 'q' 키를 누르면 종료
            break

    # 사용한 자원 해제
    cap.release()
    cv2.destroyAllWindows()
