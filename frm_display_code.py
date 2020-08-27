import sys
import socket
import json
from func_json import *
from cls_loadModule import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from frm_top_code import cod_top
from frm_bottom_code import cod_bottom
from module.frm_display import *
from cls_thread import *

global server

class cod_display(QWidget,Ui_Form):
	"""docstring for cod_display"""
	def __init__(self, arg):
		super(cod_display, self).__init__()
		self.ini_path = ''
		self.arg = arg
		self.setupUi(self)
		self.load_config()
		self.tempform = QWidget
		self.setWindowFlags(Qt.FramelessWindowHint)

	def load_config(self):
		ini_path="./initialize/confige.ini"
		ini_args = read_file(ini_path)
		self.configpath = ini_args["center"]['configpath']
		self.datapath = ini_args["center"]['datapath']
		self.x = int(ini_args["center"]['x'])
		self.y =  int(ini_args["center"]['y'])
		self.width =  int(ini_args["center"]['width'])
		self.height =  int(ini_args["center"]['height'])
		self.setStyleSheet(ini_args["center"]['stylesheet'])
		self.udp_ip = ini_args["center"]['udp_ip']
		self.udp_port = ini_args["center"]['udp_port']
		self.pic_path = ini_args["center"]['pic_path']

		self.move(self.x,self.y)#窗体定位
		self.resize(self.width,self.height) 		
		'''设置窗体图片'''
		painter = QPainter(self)
		pixmap = QPixmap(self.pic_path)
		painter.drawPixmap(self.rect(),pixmap)	
		# 加入页眉和页脚
		self.ly_top.addWidget(cod_top(""))
		self.ly_bottom.addWidget(cod_bottom(""))

		#开启UDP监控线程
		self.start_udp((self.udp_ip,int(self.udp_port)),self.datapath)
	
	def start_udp(self,arg,path="./initialize/data.ini"):
		global server
		try:
			u_thread = UDPThread()
			server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			# 绑定 客户端口和地址:
			server.bind(arg)

			u_thread.sinOut.connect(self.load_data)
			u_thread.start()
			
		except expression as identifier:
			u_thread.finished()
		finally:
			self.udp_stop

	def udp_stop():
		global server
		u_thread.flag = False
		server.close()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		
	def keyPressEvent(self,event):
		'''退出窗体快捷键escape'''
		self.key = ""

		if event.key() == Qt.Key_Escape:
			try:
				self.close()
				self.arg.show()
			except Exception as e:
				return

		elif event.key() == Qt.Key_Shift:
			load_data(self)

	def load_data(self,args):
		try:
			print(args)
			self.data_ini_args = json.loads(args.replace("\'","\""))
			a = self.data_ini_args.keys()
			a = list(a)[0]
			if (a == "C8kPeuWjMxOqm4Ca"):
				pass
			
			else:
				write_file(self.datapath,args)

				# 从ly_center卸载widget
				if (self.ly_center.itemAt(0)): 
					for i in reversed(range(self.ly_center.count())): 
						self.ly_center.itemAt(i).widget().deleteLater()
						# ly_center.itemAt(i).widget().setParent(None)

				if (a == "welcome"):
					self.tempform = mod_welcome(self.data_ini_args)
				elif (a == "result"):
					self.tempform = mod_result(self.data_ini_args)
				elif (a == "schedule"):
					self.tempform = mod_schedule(self.data_ini_args)
				elif (a == "startlist"):
					self.tempform = mod_startlist(self.data_ini_args)
				elif (a == "resultlist"):
					self.tempform = mod_resultlist(self.data_ini_args)
				elif (a == "ranklist"):
					self.tempform = mod_ranklist(self.data_ini_args)
				elif (a == "judge"):
					self.tempform = mod_judge(self.data_ini_args)
					
				self.ly_center.addWidget(self.tempform)

		except Exception as e:
			raise e
		finally:
			pass

class UDPThread(QThread):
	sinOut = pyqtSignal(str)

	def __init__(self):
		super(UDPThread, self).__init__()
		self.flag = True
	
	def __del__(self):
		self.flag = False
		self.wait()

	def run(self): 
		global server
		while self.flag == True:
			data, addr = server.recvfrom(1024) #1024是接收字节
			# data = server.recv(1024) #1024是接收字节
			sx = str(data.decode('utf-8'))
			server.sendto("ok".encode('utf-8'), addr)
			self.sinOut.emit(sx)
			# time.sleep(0.99)






if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = cod_display("hello")
	example.show()
	sys.exit(app.exec_())