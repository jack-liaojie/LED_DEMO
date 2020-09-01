import sys
import socket
import json
from func_json import *
from cls_loadModule import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from module.frm_display import *
from cls_thread import *

global server
global udpconn
global datapath
class cod_display(QWidget,Ui_Form):
	"""docstring for cod_display"""
	def __init__(self, arg):
		super(cod_display, self).__init__()
		self.ini_path = ''
		self.setupUi(self)
		self.arg = arg
		self.load_config()
		self.lbl_timer.setText("     ")
		self.tempform = QWidget
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.fiveflag = True
		self.countdownflag = True

	def load_config(self):
		global udpconn
		global datapath
		try:
			
			ini_path="./initialize/config.ini"
			ini_args = str_dict(read_file(ini_path))
			self.configpath = ini_args["center"]['modulepath']
			datapath = ini_args["center"]['datapath']
			self.x = int(ini_args["center"]['x'])
			self.y =  int(ini_args["center"]['y'])
			self.timer = int(ini_args["center"]['timer'])
			self.width =  int(ini_args["center"]['width'])
			self.height =  int(ini_args["center"]['height'])
			self.setStyleSheet(ini_args["center"]['stylesheet'])
			self.udp_ip = ini_args["center"]['udp_ip']
			self.udp_port = ini_args["center"]['udp_port']
			self.pic_path = ini_args["center"]['pic_path']
			self.scrolltime = int(ini_args["center"]['scrolltime']) if ini_args["center"]['scrolltime'].isnumeric() else 10000
			self.counttime = int(ini_args["center"]['counttime']) if ini_args["center"]['counttime'].isnumeric() else 20
			self.top_title = ini_args["top"]['title']
			udpconn = (self.udp_ip,int(self.udp_port))
			self.move(self.x,self.y)#窗体定位
			self.resize(self.width,self.height) 		
			'''设置窗体图片'''
			painter = QPainter(self)
			pixmap = QPixmap(self.pic_path)
			painter.drawPixmap(self.rect(),pixmap)
			# 加入页眉和页脚
			# start_working(['fivetime','5'],self.lbl_timer)
			start_working(['datetime'],self.lbl_datetime)
			
		except:
			ini_path="./initialize/config.ini"
			self.configpath = "./module/"
			datapath = "./initialize/data.ini"
			self.x = 0
			self.y =  0
			self.timer = 300
			self.width =  1920
			self.height =  1080
			self.setStyleSheet("font-size:40pt;background-color:rgb(26, 36,56);")
			self.udp_ip = "127.0.0.1"
			self.udp_port = "8080"
			self.pic_path = "./resource/"
			self.scrolltime = 10000
			self.counttime = 20
			udpconn = (self.udp_ip,int(self.udp_port))
			self.move(self.x,self.y)#窗体定位
			self.resize(self.width,self.height) 	
		finally:
			self.lbl_title.setText(self.top_title)

			#开启UDP监控线程
			self.start_udp((self.udp_ip,int(self.udp_port)),datapath)
			

	def start_udp(self,arg,path="./initialize/data.ini"):
		global server
		try:
			u_thread = UDPThread()
			server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			# 绑定 客户端口和地址:
			server.bind(arg)

			u_thread.sinOut.connect(self.load_data)
			u_thread.start()
			
		except IOError as identifier:
			u_thread.finished
		finally:
			self.udp_stop

	def udp_stop():
		global server
		global datapath
		u_thread.flag = False
		server.close()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		
	def keyPressEvent(self,event):
		'''退出窗体快捷键escape'''
		try:
			if event.key() == Qt.Key_Escape:
				self.close()
				self.arg.show()

			elif event.key() == Qt.Key_Return:#5分钟正计时
				if self.fiveflag == True:
					self.fiveflag = False
					start_working(['fivetime',self.timer if self.timer>0 else 300],self.lbl_timer)
				else :
					self.fiveflag = True
					stop('fivetime')
					self.lbl_timer.setText('00:00')

			elif event.key() == Qt.Key_Shift:#20秒倒计时
				if self.countdownflag == True:
					self.countdownflag = False
					self.tempform.starttimer(self.counttime)
				else :
					self.countdownflag = True
					self.tempform.endtimer()

			elif event.key() == Qt.Key_Space:
				self.load_data(datapath)

		except :
			return
		finally:
			self.key = ""

	def load_data(self,data_path):
		"""对UDP数据进行解析并控制屏幕操作"""
		try:		
			self.lbl_timer.setText("     ")
			self.data_ini_args = json_dict(read_file(data_path))
			a = self.data_ini_args.keys()
			a = list(a)[0]

			if (a == "C8kPeuWjMxOqm4Ca"):
				pass
			
			else:

				# 从ly_center卸载widget
				if (self.ly_center.itemAt(0)): 
					for i in reversed(range(self.ly_center.count())): 
						self.ly_center.itemAt(i).widget().deleteLater()
						# ly_center.itemAt(i).widget().setParent(None)

				if (a == "welcome"):
					self.tempform = mod_welcome(self.data_ini_args)
				if (a == "step"):
					self.tempform = mod_step(self.data_ini_args)
				elif (a == "result"):
					self.lbl_timer.setText('00:00')
					self.tempform = mod_result(self.data_ini_args,self.counttime)
				elif (a == "schedule"):
					self.tempform = mod_schedule(self.data_ini_args)
				elif (a == "startlist"):
					self.tempform = mod_startlist(self.data_ini_args,self.scrolltime)
				elif (a == "r_list"):
					self.tempform = mod_resultlist(self.data_ini_args,self.scrolltime)
				elif (a == 'k_list'):
					self.tempform = mod_ranklist(self.data_ini_args,self.scrolltime)
				elif (a == "judge"):
					self.tempform = mod_judge(self.data_ini_args)
				elif (a == "medal"):
					self.tempform = mod_medal(self.data_ini_args,self.scrolltime)
				elif (a == "celebrate"):
					self.tempform = mod_celebrate(self.data_ini_args)
					
				elif (a == "timerstart"):
					start_working(['fivetime',self.timer if self.timer>0 else 300],self.lbl_timer)
					
				self.ly_center.addWidget(self.tempform)

		except Exception as e:
			raise e
		finally:
			return

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
		global datapath
		global udpconn

		while self.flag == True:
			try:
				data, addr = server.recvfrom(10240) #1024是接收字节 # resultlist 是关键字出现就报错
				# data = server.recv(10024) #1024是接收字节
				sx = str(data.decode('utf-8'))
				server.sendto("ok".encode('utf-8'), addr)
				server.close()
			except WindowsError as identifier:
				sx = str(data.decode('utf-8'))#读出发送的json字符串数据
				server.close()
				server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				# 绑定 客户端口和地址:
				server.bind(udpconn)
			finally:
				write_file(datapath,sx)
				time.sleep(0.99)
				self.sinOut.emit(datapath)






if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = cod_display("hello")
	example.show()
	sys.exit(app.exec_())