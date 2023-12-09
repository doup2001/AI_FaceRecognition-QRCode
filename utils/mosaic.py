import cv2

# 얼굴 부분을 모자이크 처리하는 함수
def mosaic_faces(frame, faces):
    for (x, y, w, h) in faces:

        face_roi = frame[y:y+h, x:x+w]

        face_roi = cv2.resize(face_roi, (w//10, h//10))

        face_roi = cv2.resize(face_roi, (w, h), interpolation=cv2.INTER_AREA)

        # 모자이크 처리된 얼굴을 원본 프레임에 적용
        frame[y:y+h, x:x+w] = face_roi

    return frame


    # 얼굴 감지
    faces = detect_faces(frame)

    # 얼굴 부분 모자이크 처리
    frame = mosaic_faces(frame, faces)