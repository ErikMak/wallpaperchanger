import ctypes
import platform
import design
import os
from timestamp import Timestamp
from wallpapers import Wallpapers
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		# Объекты классов Timestamp и Wallpapers
		self.timest = Timestamp()
		self.wallpapers = Wallpapers(self.timest)

		self.setupUi(self)

		# Загрузка обоев
		self.loadWallpaper()
		# Событие на кнопку смены обоев запускает метод смены системных обоев
		self.btnChange.clicked.connect(self.changeWallpaper)
		# Событие на вторую кнопку еще раз загружает обои (обновляет)
		self.btnReload.clicked.connect(self.loadWallpaper)

		# Таймер
		timer = QtCore.QTimer(self)
		# Отрисовка часов по таймеру
		timer.timeout.connect(self.printLabel)

		# Запуск таймера с периодом 1сек
		timer.start(1000)

	def printInfo(self):
		# Текущий сезон - массив, нулевой элемент название, первый элемент иконка
		season = self.timest.getCurrentSeasonLabel()
		# Путь к картинке
		img = self.wallpapers.getWallpaper()

		text = '<p>&#128293; Добро пожаловать в WallpaperChanger! \
		<br>Текущий сезон: <b>{} {}</b> \
		<br>Предварительный просмотр:</p> \
		<div><img width="450" src="{}"></div>'.format(season[1], season[0], img)

		# Вставка подготовленного текста
		self.textEdit.setHtml(text)

	def printError(self, msg):
		# Сообщение об ошибке
		text = '<p>&#128293; Добро пожаловать в WallpaperChanger! \
		<br>&#9940; {}</p>'.format(msg)

		# Вставка подготовленного текста
		self.textEdit.setHtml(text)

	def printLabel(self):
		# Получить текущее время, модуль от Qt
		time = QtCore.QTime.currentTime()
		# Текстовый формат
		label_time = time.toString('hh:mm:ss')

		self.timerLabel.setText(label_time)

	def loadWallpaper(self): 
		try:
			# Предварительно загрузить обои
			self.wallpapers.uploadWallpaper()
			# Вывести текст с информацией и картинкой
			self.printInfo()
		except Exception as err:
			self.printError(err)

	def changeWallpaper(self):
		try:
			# Путь к картинке
			wallpaper_path = self.wallpapers.getWallpaper()
			SPI_SETDESKWALLPAPER = 20

			# Абсолютный путь к картинке
			abs_path = os.path.abspath(wallpaper_path)

			# В зависимости от ОС сменить обои
			if(platform.system() == 'Windows'):
				ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
			elif(platform.system() == 'Linux'): 	
				os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri "file:///{}"'.format(abs_path))
		except Exception as err:
			self.printError(err)