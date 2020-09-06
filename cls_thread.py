
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
global f_thread
global d_thread
global f_lbltime
global d_lbltime
global i
def start_working(arg,lblobject):
	"""lblobject需要传入QLabel对象"""
	global sec
	global i
	if (arg[0] == 'fivetime'):
		global f_lbltime
		global f_thread
		f_thread = TimerThread()
		f_lbltime = lblobject
		sec = arg[1] if type(arg) == int else 300
		i = 0
		f_thread.trigger.connect(five_working)
		f_thread.start()

	elif (arg[0] == 'datetime'):
		global d_lbltime
		global d_thread
		d_thread = TimerThread()
		d_lbltime = lblobject
		
		d_thread.trigger.connect(curr_working)

		d_thread.start()

def curr_working():
	global d_lbltime
	d = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss dddd")
	d_lbltime.setText(d)

def five_working():
	global sec
	global i
	i += 1
	if (i == sec + 1): 
		i = 0
		stop("fivetime")
	else :
		f_lbltime.setText(intotime(i)) #在lbl对象上显示数字

def stop(arg):
	try:

		if (arg == 'datetime'):
			global d_thread
			d_thread.flag = False
			# d_thread.quit()
			d_thread.terminate()
			d_thread.wait()
		elif (arg == 'fivetime'):
			global f_thread
			f_thread.flag = False
			# f_thread.quit()
			f_thread.terminate()
			f_thread.wait()
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
	start_working(['fivetime','530'],QLabel())
	start_working(['datetime'],QLabel())
	udp_working(("127.0.0.1",8080),"./initialize/data.ini",QLabel)

	sys.exit(app.exec_())
