import sys
from algorithm import playfair, Vigenere, Rotor, DES_a, AES128
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QRadioButton)
from config import *
import chardet

class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.set_layout()
        self.initUI()
        self.init_choose_UI()
        self.key = None

    def set_layout(self):
        self.grid = QGridLayout() #栅栏布局
        self.grid.setSpacing(10)
        self.setLayout(self.grid)
        self.setGeometry(300, 300, 1200, 450)
        self.setWindowTitle('加密解密系统')
        self.show()

    def initUI(self):
        '''初始化并添加共有的控件: 标题、明文、加密、解密标签及文本框'''
        self.title = QLabel('加密解密系统')
        self.title.setFont(QFont("等线", 15, QFont.Bold))

        self.keyEdit = QLineEdit()
        self.key_text = QLabel('密钥')

        plain_text = QLabel('明文')
        cipher_text = QLabel('密文')
        plain_text2 = QLabel('解密结果')

        encryp_button = QPushButton('加密')
        decryp_button = QPushButton('解密')
        encryp_button.clicked.connect(self.encrypt)
        decryp_button.clicked.connect(self.decrypt)

        self.plain_text_edit = QTextEdit()
        self.cipher_text_edit = QTextEdit()
        self.plain_text2_edit = QTextEdit()
        self.plain_text_edit.setText('Please input string to encrpyt')

        for each in [plain_text, cipher_text, plain_text2, encryp_button, decryp_button,
                     self.plain_text_edit, self.cipher_text_edit, self.plain_text2_edit,
                     self.key_text, self.keyEdit]:
            each.setFont(QFont("等线", 13, QFont.Bold))

        for each in [plain_text, cipher_text, plain_text2, self.title]:
            each.setAlignment(Qt.AlignCenter)

        self.key_text.setAlignment(Qt.AlignRight)
        #添加各个控件
        self.grid.addWidget(self.title, 0, 3)

        self.grid.addWidget(self.key_text, 1, 1)
        self.grid.addWidget(self.keyEdit, 1, 2, 1, 3)

        self.grid.addWidget(plain_text, 2, 1)
        self.grid.addWidget(self.plain_text_edit, 3, 1, 5, 1)
        self.grid.addWidget(encryp_button, 6, 2)

        self.grid.addWidget(cipher_text, 2, 3)
        self.grid.addWidget(self.cipher_text_edit, 3, 3, 5, 1)
        self.grid.addWidget(decryp_button, 6, 4)

        self.grid.addWidget(plain_text2, 2, 5)
        self.grid.addWidget(self.plain_text2_edit, 3, 5, 5, 1)

    def init_choose_UI(self):
        '''初始化选择哪种加密算法的控件'''
        ag1 = QRadioButton(PLAY_FAIR)
        ag2 = QRadioButton(VIGENERE)
        ag3 = QRadioButton(ROTOR)
        ag4 = QRadioButton(DES)
        ag5 = QRadioButton(AES_128)
        self.ags = [ag1, ag2, ag3, ag4, ag5]
        for each in self.ags:
            each.setFont(QFont("等线", 13, QFont.Bold))
            each.toggled.connect(self.switch_UI)
        self.grid.addWidget(ag1, 1, 0)
        self.grid.addWidget(ag2, 2, 0)
        self.grid.addWidget(ag3, 3, 0)
        self.grid.addWidget(ag4, 4, 0)
        self.grid.addWidget(ag5, 5, 0)

    def switch_UI(self):
        agbutton = self.sender()
        if agbutton.isChecked():
            name = agbutton.text()
            self.title.setText(name)
            if name != ROTOR:
                self.keyEdit.setEnabled(True)
                self.keyEdit.setText(name_key_dict[name])

            else:
                self.keyEdit.setText('只使用默认密钥')
                self.keyEdit.setEnabled(False)
            self.plain_text_edit.setText('Please input string to encrpyt')
            self.cipher_text_edit.setText('')
            self.plain_text2_edit.setText('')

    def encrypt(self):
        pt = self.plain_text_edit.toPlainText()
        if len(pt) == 0: return
        name = self.title.text()
        self.key = self.keyEdit.text()
        if name != ROTOR and len(self.key) == 0: return
        if name == PLAY_FAIR: ct = playfair.crypt_sentence(pt, self.key)
        if name == VIGENERE: ct = Vigenere.cryp_decryp_Vigenere_sentence(pt, self.key, 1)
        if name == ROTOR: ct = Rotor.crypt_decrypt_rotor_sentence(pt, Rotor.ls1, Rotor.ls2, 1)
        if name == DES:
            ct = DES_a.DES_encryp_decryp_sentence(pt, self.key, 1)
            self.ct_DES = ct
        if name == AES_128:
            ct = AES128.AES_encryp_decryp_sentence(pt, self.key, 1)
            self.ct_AES = ct
        self.cipher_text_edit.setText(ct)
        self.plain_text2_edit.setText('')

    def decrypt(self):
        ct = self.cipher_text_edit.toPlainText()
        if len(ct) == 0: return
        name = self.title.text()
        self.key = self.keyEdit.text()
        if name != ROTOR and len(self.key) == 0: return
        if name == PLAY_FAIR: pt2 = playfair.decrypt_sentence(ct, self.key)
        if name == VIGENERE: pt2 = Vigenere.cryp_decryp_Vigenere_sentence(ct, self.key, -1)
        if name == ROTOR: pt2 = Rotor.crypt_decrypt_rotor_sentence(ct, Rotor.ls1, Rotor.ls2, -1)
        if name == DES: pt2 = DES_a.DES_encryp_decryp_sentence(self.ct_DES, self.key, -1) #字符转换问题
        if name == AES_128: pt2 = AES128.AES_encryp_decryp_sentence(self.ct_AES, self.key, -1)
        self.plain_text2_edit.setText(pt2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())