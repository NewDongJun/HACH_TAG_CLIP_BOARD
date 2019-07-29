import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 문자열 저장할 리스트
List_A = []
s_line = []

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("일단gui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #문자열 리스트화
        global s_line
        global List_A
        f = open("hihi.txt", 'r')

        while True:
            line = f.readline()
            s_line.append(line)
            if '#' in line:
                List_A.append(s_line)
                s_line = []
            if not line: break
        f.close()

        #리스트에 표시




        self.PlusBtn.clicked.connect(self.button1Function)

        

    #btn_1이 눌리면 작동할 함수
    def button1Function(self):
        text = self.TextBox.toPlainText()
        f = open("hihi.txt", 'a')
        f.write(text)
        f.close()



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()



