
# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import time
import socket
from func_json import *
from cls_loadModule import *

# class UDPThread(QThread):
# 	"""docstring for TimerThread"""

# 	def __init__(self):
# 		super(UDPThread, self).__init__()
# 		self.flag = True
	
# 	def __del__(self):
# 		self.flag = False
# 		self.wait()

# 	def run(self): 
# 		while self.flag == True:
# 			udp_listening()
# 			time.sleep(0.99)

# global u_obj
# global u_thread
# global u_path
# global s
# def udp_working(arg,path,obj):
# 	global u_thread
# 	global u_obj
# 	global u_path
# 	global s
# 	u_obj = obj
# 	u_path = path
# 	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 	# 绑定 客户端口和地址:
# 	s.bind(arg)

# 	u_thread = UDPThread()
# 	u_thread.start()

# def udp_listening():
# 	global s
# 	# global u_path
# 	data, addr = s.recvfrom(1024) #1024是接收字节
# 	# data = s.recv(1024) #1024是接收字节
# 	# print ('Received from %s:%s.' % addr)
# 	sx = str(data.decode('utf-8'))
# 	print(sx)
# 	# s.sendto("sx".encode('utf-8'), addr)
# 	write_file(u_path,sx)
# 	load_data(u_obj)

# def udp_stop():
# 	global u_thread
# 	global s
# 	u_thread.flag = False
# 	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


class TimerThread(QThread):
	"""docstring for TimerThread"""
	trigger = pyqtSignal()

	def __init__(self):
		super(TimerThread, self).__init__()
		self.flag = True
	
	def __del__(self):
		self.flag = False
		self.wait()

	def run(self): 
		while self.flag == True:
			self.trigger.emit()
			time.sleep(0.99)
global f_thread
global d_thread
global f_lbltime
global d_lbltime
def start_working(arg,lblobject):
	"""lblobject需要传入QLabel对象"""
	global sec
	if (arg[0] == 'fivetime'):
		global f_lbltime
		global f_thread
		f_thread = TimerThread()
		f_lbltime = lblobject
		sec = int(arg[1]) if arg[1].isnumeric() else 300
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
	d = QDateTime.currentDateTime().toString("hh:mm:ss dddd")
	# d = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss dddd")
	d_lbltime.setText(d)
	# print(d)

def five_working():
	global sec
	sec -= 1
	if (sec == -1): 
		stop("fivetime")
	else :
		f_lbltime.setText(intotime(sec)) #在lbl对象上显示数字
		# print(intotime(sec))

def stop(arg):
	if (arg == 'datetime'):
		global d_thread
		d_thread.flag = False
	elif (arg == 'fivetime'):
		global f_thread
		f_thread.flag = False
		global sec
		sec = 300
	
def intotime(sec):
	m, s = divmod(sec, 60)
	h, m = divmod(m, 60)
	return ("%02d:%02d:%02d" % (h, m, s))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	start_working(['fivetime','530'],QLabel())
	start_working(['datetime'],QLabel())
	udp_working(("127.0.0.1",8080),"./initialize/data.ini",QLabel)

	sys.exit(app.exec_())
