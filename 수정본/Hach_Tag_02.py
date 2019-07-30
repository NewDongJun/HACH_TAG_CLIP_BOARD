import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import search as sc

# 문자열 저장할 리스트
List_A = []
s_line = []
WW_List = []
WW_Line = ''

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

def delete_blank_tag(): #빈칸을 지우는 함수

    f = open("data.txt", 'r')
    list_data = f.readlines() # data 전체를 잠시 받는 리스트
    f.close()

    i = 0
    token = 0
    while(i < len(list_data)):
        if '#' in list_data[i]:
            token += 1
        else:
            token = 0

        if token is 2:
            del list_data[i]
            i -= 1
            token = 1
        i += 1

    f = open("data.txt", 'w')
    for i in range(0, len(list_data)):
        f.write(list_data[i])
    f.close()

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("일단gui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        delete_blank_tag()
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

        #편집기능
        self.listView.itemClicked.connect(self.I_Edit)





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
        self.listView.itemClicked.connect(self.SC_Texting)
        #print(ans)

    def SC_Texting(self):
        ans = sc.search(self.finding.text())
        self.OutText.clear()
        for i in ans:
            if self.listView.currentRow() == ans.index(i):
                for j in i:
                    self.OutText.append(j)

    def I_Edit(self):
        self.OutText.textChanged.connect(self.O_Edit)

    def O_Edit(self):
        global WW_List_A
        global WW_Line
        global List_A
        W_text = self.OutText.toPlainText()
        W_Line = W_text.split('#')
        #print(W_Line)
        for i in W_Line:
            if W_Line[0] == i:
                continue
            W_Line[W_Line.index(i)] = '#' + i

        if len(W_Line) > 2:
            for i in W_Line:
                if W_Line[0] == i or W_Line[1] == i:
                    continue
                W_Line[1] = W_Line[1] + i
                del(W_Line[W_Line.index(i)])
"""
        #print(W_Line)
        List_A[self.listView.currentRow()] = W_Line
        #print(List_A)

        WW_List_A = List_A
        #print(WW_List_A)
        WW_Line =''
        f = open("data.txt", 'w')
        for i in WW_List_A:
            for k in i:
                WW_Line += k
        f.write(WW_Line)
        f.write("\n")
        f.close()
        M_List()
"""















if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()



