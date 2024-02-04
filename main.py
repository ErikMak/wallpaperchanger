import sys
from PyQt5 import QtWidgets
from app import App

def main():
	qt_app = QtWidgets.QApplication(sys.argv)
	window = App()
	window.show()
	qt_app.exit(qt_app.exec_())

if __name__ == '__main__':
	main()