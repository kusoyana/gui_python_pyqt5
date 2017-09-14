import sys
from main_window_ui import Ui_MainWindow
from new_window_ui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialog


class MainWindow(QMainWindow):
    # Ui_MainWindow生成のための初期化処理
    def __init__(self, sysarg):
        # UIの初期化処理
        app = QApplication(sysarg)
        window = QMainWindow()
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        # ここで作成したUi_MainWindowクラスを生成するQMainWindowクラスを
        # セットアップする
        self.ui.setupUi(self)

        # QPushbutton（正確には継承元のQAbstractButton)のcliked関数にconnect
        # これをする事でボタンが押された時にcreateWindow関数が呼ばれる事になる。
        self.ui.enrollButton.clicked.connect(self.clickedEnroll)

        self.ui.authenticationButton.clicked.connect(self.clickedAuthentication)

        # MainWindowの表示処理
        self.show()

        # MainWindowの実行
        sys.exit(app.exec_())

    # pushButtonがクリックされた時に呼ばれる関数
    # 処理としてはただ新しいWindowを作るだけ
    def createWindow(self):
        new_window = NewWindow()

    def clickedEnroll(self):
        self.createWindow()

    def clickedAuthentication(self):
        print("hello world")


class NewWindow(QDialog):
    def __init__(self):
        # NewWindowの初期化処理
        super(NewWindow, self).__init__()
        dialog = Ui_Dialog()

        # NewWindowのセットアップ
        dialog.setupUi(self)
        self.combo = dialog.classComboBox
        self.spin = dialog.classSpinBox

        self.combo.addItem("小学生")
        self.combo.addItem("中学生")

        self.combo.activated[str].connect(self.onActivated)
        dialog.cancelButton.clicked.connect(self.clickedCancel)

        dialog.enrollButton.clicked.connect(self.clickedEnroll2())
        # NewWindowの表示処理
        self.show()
        self.exec_()




    def clickedCancel(self):
        print("hello world")
        #self.close()

    def clickedEnroll2(self):
        print("hello world")

    def onActivated(self, text):
        # 選択されたアイテムの名前を表示
        print(text)

        if(text == "中学生"):
            self.spin.setMaximum(3)
        else:
            self.spin.setMaximum(6)

if __name__ == "__main__":
    window = MainWindow(sys.argv)