import os
import random

class Wallpapers:
	# Поддерживаемые расширения
	IMGS_EXTENSION = ['png', 'jpeg', 'jpg']
	# Папка с изображениями
	IMGS_PATH = './images'

	# Список фоновых изображений
	images = list()

	def __init__(self, timest):
		# Объект для работы с датой и временем
		self.timest = timest

	def __getWallpapers(self):
		# Загрузка всех картинок
		for img in os.listdir(self.IMGS_PATH):
			# Расширение картинки
			ext = img.split('.')[len(img.split('.')) - 1]
			# Если подходит, добавить в список
			if(ext in self.IMGS_EXTENSION):
				self.images.append(img)

	def uploadWallpaper(self):
		# Загрузка всех картинок
		self.__getWallpapers()

		data = list()
		curr_s = str(self.timest.getCurrentSeason())
		curr_t = self.timest.getCurrentTimeOfDay()

		# Фильтрация имеющихся картинок, соответствующих сезону и времени суток
		# img[0] означает первая буква в названии картинки, т.е номер сезона
		# img[2] - время суток
		for img in self.images:
			if(img[0] == curr_s and img[2] == curr_t):
				data.append(img)

		# Рандомный выбор
		choice = random.randint(0, len(data) - 1)

		# Предзагруженное фоновое изображение
		self.image = data[choice]

	def getWallpaper(self): 
		return self.IMGS_PATH + '/' + self.image