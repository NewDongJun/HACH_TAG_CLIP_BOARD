import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import search as sc

# 문자열 저장할 리스트
List_A = []
s_line = []

# 입력받은 문자를 리스트로 읽어들이는 함수
def M_List():
    global s_line
    global List_A
    s_line = []
    List_A = []
    f = open("data.txt", 'r')

    while True:
        line = f.readline()
        s_line.append(line)
        if '#' in line:
            List_A.append(s_line)
            s_line = []
        if not line: break
    f.close()

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("일단gui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)


        self.PlusBtn.clicked.connect(self.button1Function)

        #리스트 위젯
        M_List()
        L_Text = ""
        self.listView.clear()
        for i in List_A:
            for k in i:
                L_Text= L_Text + k
            self.listView.addItem(L_Text)
            L_Text = ""
        self.listView.itemClicked.connect(self.Texting)   

        #서치 기능

        self.finding.textChanged.connect(self.Search)





    #btn_1이 눌리면 작동할 함수
    #버튼을 누르면 글이 추가
    def button1Function(self):
        #txt저장소에 데이터를 저장하는 기능
        text = self.TextBox.toPlainText()
        f = open("data.txt", 'a')
        f.write(text)
        f.write("\n")
        f.close()
        self.TextBox.clear()

        #리스트 재생성
        M_List()
        L_Text = ""
        self.listView.clear()
        for i in List_A:
            for k in i:
                L_Text= L_Text + k
            self.listView.addItem(L_Text)
            L_Text = ""
        self.listView.itemClicked.connect(self.Texting)



    def Texting(self):
        self.OutText.clear()
        for i in List_A:
            if self.listView.currentRow() == List_A.index(i):
                for j in i:
                    self.OutText.append(j)



    """
    ##함수 사용법 나중에 키워드는 변수 처리해서 따로 입력 받으면 됨
    ans = sc.search("이거")
    print(ans)
    """
    def Search(self):
        L_Text = ""
        ans = sc.search(self.finding.text())
        self.listView.clear()
        for i in ans:
            for k in i:
                L_Text= L_Text + k
            self.listView.addItem(L_Text)
            L_Text = ""
        self.listView.itemClicked.connect(self.Texting)
        print(ans)






if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()



