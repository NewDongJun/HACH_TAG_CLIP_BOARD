import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("일단gui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        f = open("hihi.txt", 'r')
        while True:
            line = f.readline()
            if not line: break
            self.TextBox.append(line)
        f.close()

        self.PlusBtn.clicked.connect(self.button1Function)
        self.TextBox.textChanged.connect(self.TextSave)




    #btn_1이 눌리면 작동할 함수
    def button1Function(self):
        print("btn_1 Clicked")

    def TextSave(self):
        print("text save")
        text = self.TextBox.toPlainText()
        print(text)

        f = open("hihi.txt", 'w')
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



