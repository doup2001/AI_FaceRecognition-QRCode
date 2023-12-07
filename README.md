Gachon University OpenSource Term Project

이도연 202033454 / 김진호 201735941 / 이한별 202036175 / 이서연 202334507

프로젝트개요
- QR코드와 바코드를 인식하는 프로그램을 개발했습니다.
- QR코드와 바코드를 스캔하는 프로그램이기에 얼굴을 인식했을 때, 
  모자이크로 얼굴을 가려줄 수 있도록 기능을 추가하였습니다. 

데모나예시를보여주는이미지/영상
- 유튜브 링크 참조 : 

사용한패키지와그version(install이필요할경우안내)
- numpy==1.26.2
- opencv-python==4.8.1.78
- pyzbar==0.1.9

실행방법
- program.py를 실행하여 웹캠으로 바코드나, QR코드를 보여주게 된다면 좌측 상단 위에 해당 정보가 출력됩니다.
  QR코드의 경우에는 해당 화면을 누를 시, 사이트로 이동합니다.

참고자료(참고한자료,영상,블로그,소스코드등이있을경우반드시표기)
- pyzbar 설치 관련 참고 블로그 : https://jeongjaeyoung0.github.io/python/2021/09/09/PS-zbar/
- qr코드 스캔 블로그 : https://www.delftstack.com/ko/howto/python/opencv-qr-code/
- 바코드 스캔 블로그 : https://jeongjaeyoung0.github.io/python/2021/09/08/PV-barcodeRecognition/