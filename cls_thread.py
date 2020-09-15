
# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import time
import socket
from func_json import *
from cls_loadModule import *

class TimerThread(QThread):
	"""docstring for TimerThread"""
	trigger = pyqtSignal()

	def __init__(self):
		super(TimerThread, self).__init__()
		self.flag = True
	
	def __del__(self):
		self.quit()
		self.wait()

	def run(self): 
		while self.flag == True:
			self.trigger.emit()
			time.sleep(1)
global d_thread
global d_lbltime
global i
global sec
def start_working(lblobject):
	"""lblobject需要传入QLabel对象"""
	global sec
	global i
	global d_lbltime
	global d_thread
	d_thread = TimerThread()
	d_lbltime = lblobject

	d_thread.trigger.connect(curr_working)

	d_thread.start()

def curr_working():
	global d_lbltime
	d = QDateTime.currentDateTime().toString("hh:mm:ss")
	d_lbltime.setText(d)


def stop_working(arg):
	try:

		global d_thread
		global sec

		d_thread.flag = False
		d_thread.terminate()
		d_thread.wait()

	except Exception as e:
		pass
	finally:
		return

def intotime(sec):
	m, s = divmod(sec, 60)
	h, m = divmod(m, 60)
	return ("%02d:%02d" % (m, s))
	# return ("%02d:%02d:%02d" % (h, m, s))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	start_working(['datetime'],QLabel())

	sys.exit(app.exec_())
