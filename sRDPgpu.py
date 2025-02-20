# -*- coding: utf-8 -*-

import sys
import os
import base64
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import subprocess

class RDPConnector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('RDP Connector')

        layout = QVBoxLayout()

        self.label_workstation = QLabel('Имя станции:')
        self.edit_workstation = QLineEdit()
        layout.addWidget(self.label_workstation)
        layout.addWidget(self.edit_workstation)

        self.label_login = QLabel('Логин:')
        self.edit_login = QLineEdit()
        layout.addWidget(self.label_login)
        layout.addWidget(self.edit_login)

        self.label_password = QLabel('Пароль:')
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)

        self.button_connect = QPushButton('Подключиться')
        # self.button_connect.clicked.connect(self.connect_to_rdp)
        layout.addWidget(self.button_connect)

        self.setLayout(layout)

    def connect_to_rdp(self):
        workstation = self.edit_workstation.text()
        login = self.edit_login.text()
        password = self.edit_password.text()

        if not login or not password:
            QMessageBox.warning(self, 'Ошибка', 'Логин и пароль обязательны!')
            return

        # Формируем команду для подключения по RDP
        rdp_file = f"""
        full address:s:192.168.1.100
        username:s:{login}
        password:s:{password}
        """

        # Сохраняем настройки в .rdp файл
        with open('connection.rdp', 'w') as f:
            f.write(rdp_file)

        # Запускаем mstsc с созданным .rdp файлом
        try:
            subprocess.run(['mstsc', 'connection.rdp'], check=True)
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, 'Ошибка', f'Не удалось подключиться: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    rdp_connector = RDPConnector()
    rdp_connector.show()
    sys.exit(app.exec())