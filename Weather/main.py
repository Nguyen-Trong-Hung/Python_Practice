import requests
import json
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6 import QtWidgets, uic

API_KEY = '22c9e1c1151e4f61962115258240108'

url = 'http://api.weatherapi.com/v1/current.json?key=' + API_KEY + '&q=Hanoi'

response = requests.get(url)
data = response.json()

with open("data_weather.json","w", encoding="utf-8") as Datafile:
    json.dump(data, Datafile)

print("Đã lấy được dữ liệu")

class giaoDienChinh(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainUI.ui", self)

        self.updateGiaoDien()

        self.comboBoxDiaDiem.currentIndexChanged.connect(self.chuyenDiaDiem)

    def updateGiaoDien(self):
        with open("data_weather.json", "r", encoding="utf-8") as Datafile:
            dulieuDictionary = json.load(Datafile)

        self.lineEditDiaDiem.setText(dulieuDictionary['location']['name'])
        self.lineEditQuocGia.setText(dulieuDictionary['location']['country'])
        self.lineEditToaDo.setText(str(dulieuDictionary['location']['lat']) + ', ' + str(dulieuDictionary['location']['lon']))

        self.labelThoiGian.setText(dulieuDictionary['location']['localtime'])

        self.lineEditNhietDo.setText(str(dulieuDictionary['current']['temp_c']))
        self.lineEditNhietDoTB.setText(str(dulieuDictionary['current']['heatindex_c']))
        self.lineEditSucGio.setText(str(dulieuDictionary['current']['wind_kph']))
        self.lineEditHuongGio.setText(str(dulieuDictionary['current']['wind_dir']))
        self.lineEditApSuatKQ.setText(str(dulieuDictionary['current']['pressure_mb']))
        self.lineEditDoAm.setText(str(dulieuDictionary['current']['humidity']))
        self.lineEditTLMay.setText(str(dulieuDictionary['current']['cloud']))
        self.lineEditTamNhin.setText(str(dulieuDictionary['current']['vis_km']))
    
    def chuyenDiaDiem(self):
        diaDiem = self.comboBoxDiaDiem.currentText()
        url = 'http://api.weatherapi.com/v1/current.json?key=' + API_KEY + '&q=' + diaDiem

        response = requests.get(url)
        data = response.json()

        with open("data_weather.json","w", encoding="utf-8") as Datafile:
            json.dump(data, Datafile)

        print("Đã lấy được dữ liệu")
        self.updateGiaoDien()
khoiChayHeThong = QApplication(sys.argv)
phanMem = giaoDienChinh()
phanMem.show()
chayPhanMem = khoiChayHeThong.exec()
sys.exit(chayPhanMem)