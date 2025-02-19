# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('RDP Connector')

        layout = QVBoxLayout()

        self.label_login = QLabel('Логин:')
        self.edit_login = QLineEdit()
        layout.addWidget(self.label_login)
        layout.addWidget(self.edit_login)

        self.label_password = QLabel('Password:')
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)

        self.button_connect = QPushButton('Connect')
        # self.button_connect.clicked.connect(self.connect_to_rdp)
        layout.addWidget(self.button_connect)

        self.setLayout(layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    rdp_connector = Test()
    rdp_connector.show()
    sys.exit(app.exec())