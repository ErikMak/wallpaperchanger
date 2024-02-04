import datetime

class Timestamp:
	def __init__(self):
		# Текущее время 
		self.date = datetime.datetime.now() 

	def getCurrentSeason(self):
		# Текущий сезон (1 - зима, 2 - весна, 3- лето, 4-осень)
		x = self.date.month % 12 // 3 + 1
		return x

	def getCurrentSeasonLabel(self):
		x = self.getCurrentSeason()

		if(x == 1):
		 	return ['Зима', '&#10052;']
		if(x == 2):
		    return ['Весна', '&#127802;']
		if(x == 3):
			return ['Лето', '&#127958;']
		if(x == 4):
			return ['Осень', '&#127809;']

	def getCurrentTimeOfDay(self):
		hour = self.date.hour

		# Текущее время суток (n-ночь, m-утро, d-день, e-вечер)
		if hour >= 0 and hour <= 6:
			return 'n'
		if hour > 6 and hour <= 12:
			return 'm'
		if hour > 12 and hour <= 18:
			return 'd'
		if hour > 18 and hour < 24:
			return 'e'