import sip
import sys
import struct
import socket
import json
from func_json import *
from cls_loadModule import *
from PyQt5.QtCore import QThread
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from module.frm_display import *
from cls_thread import *

global server
global udpconn
global datapath
class cod_display(QWidget,Ui_Form):
	"""docstring for cod_display"""
	def __init__(self, arg,path):
		super(cod_display, self).__init__()
		self.setupUi(self)
		self.arg = arg
		self.ini_path = path 
		self.lbl_timer.setText("     ")
		self.tempform = QWidget
		self.load_config()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.fiveflag = True
		self.scrollflag = True
	def load_config(self):
		"""加载ini文件"""
		global udpconn
		global datapath

		try:
			ini_args = str_dict(read_file(self.ini_path))
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

			self.u_thread = UDPThread()#很简单的一个坑，把线程的声明放到类的初始化函数下就ok了。
			start_working(['datetime'],self.lbl_datetime)

			
		except:
			self.ini_path="./initialize/config.ini"
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
		"""启动线程监听udp指令"""
		global server

		try:
			server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#允许地址重用。
			# server.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1, 0))
			#如果要已经处于连接状态的soket在调用closesocket后强制关闭，不经TIME_WAIT的过程：

			# server.setblocking(0)#非阻塞模式

			# 绑定 客户端口和地址:
			server.bind(arg)

			self.u_thread.sinOut.connect(self.load_data)
			self.u_thread.start()
			
		except OSError as e:
			server.close()
			server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			# 绑定 客户端口和地址:
			server.bind(arg)	

		except RuntimeError as e:
			raise e
		finally:
			pass

	def stop_udp():
		"""udp指令线程停止"""
		global server
		global datapath
		self.u_thread.finished()
		server.shutdown(2)#关闭整个通道
		# server.close()

		
	def keyPressEvent(self,event):
		'''窗体快捷键'''
		global datapath
		try:
			if event.key() == Qt.Key_A:#Qt.Key_Escape
				self.stop_udp
				stop("datetime")
				stop("fivetime")
				self.hide()
				# sip.delete(self)#删除自身窗体
				# self.close()
				self.arg.show()

			elif event.key() == Qt.Key_Return:#5分钟正计时
				self.fivestart()

			elif event.key() == Qt.Key_Shift:#20秒倒计时
				self.twentystart()

			elif event.key() == Qt.Key_Space:

				self.load_data(read_file(datapath))#通过本地数据进行加载操作

		except :
			pass
		finally:
			self.key = ""

	def scrolling(self):
		"""翻屏显示启动"""
		if self.scrollflag == True and (isinstance(self.tempform,mod_resultlist) or isinstance(self.tempform,mod_startlist) 
		or isinstance(self.tempform,mod_ranklist) or isinstance(self.tempform,mod_medal)):
			self.scrollflag = False
			self.tempform.starttimer(self.scrolltime)

		elif self.scrollflag == False and (isinstance(self.tempform,mod_resultlist) or isinstance(self.tempform,mod_startlist) 
		or isinstance(self.tempform,mod_ranklist) or isinstance(self.tempform,mod_medal)):
			self.scrollflag = True
			self.tempform.endtimer()

	def fivestart(self):
		"""正计时5分钟启动"""
		if self.fiveflag == True:
			self.fiveflag = False
			start_working(['fivetime',self.timer if self.timer>0 else 300],self.lbl_timer)
		else :
			self.fiveflag = True
			stop('fivetime')
			self.lbl_timer.setText('     ')

	def twentystart(self):
		"""倒计时20秒启动"""
		if isinstance(self.tempform,mod_result):#判断是否是成绩处理模块
			self.tempform.starttimer(self.counttime)

	def load_data(self,sx):
		"""对UDP数据进行解析并控制屏幕操作，是本地数据操作和在线数据操作的统一入口"""
		try:		
			self.data_ini_args = json_dict(sx)

			a = self.data_ini_args.keys()
			a = list(a)[0]

			if (a == "C8kPeuWjMxOqm4Ca"):
				pass
			
			elif (a == "scrolling"):
				self.scrolling()

			elif (a == "twentystart"):
				self.twentystart()

			elif (a == "fivestart"):
				self.fivestart()

			else:

				# 从ly_center卸载widget
				if (self.ly_center.itemAt(0)): 
					for i in reversed(range(self.ly_center.count())): 
						self.ly_center.itemAt(i).widget().deleteLater()#两种方法都可以清除主窗体内的挂件
						# ly_center.itemAt(i).widget().setParent(None)

				if (a == "welcome"):
					self.tempform = mod_welcome(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)

				if (a == "step"):
					self.tempform = mod_step(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)

				elif (a == "result"):
					self.lbl_timer.setText('00:00')
					self.tempform = mod_result(self.data_ini_args,self.counttime)
					self.ly_center.addWidget(self.tempform)

				elif (a == "schedule"):
					self.tempform = mod_schedule(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)

				elif (a == "startlist"):
					self.tempform = mod_startlist(self.data_ini_args,self.scrolltime)
					self.ly_center.addWidget(self.tempform)

				elif (a == "r_list"):
					self.tempform = mod_resultlist(self.data_ini_args,self.scrolltime)
					self.ly_center.addWidget(self.tempform)
				elif (a == 'k_list'):
					self.tempform = mod_ranklist(self.data_ini_args,self.scrolltime)
					self.ly_center.addWidget(self.tempform)

				elif (a == "judge"):
					self.tempform = mod_judge(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)
				elif (a == "medal"):
					self.tempform = mod_medal(self.data_ini_args,self.scrolltime)
					self.ly_center.addWidget(self.tempform)
				elif (a == "celebrate"):
					self.tempform = mod_celebrate(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)
				
		except Exception as e:
			raise e
		finally:
			return

class UDPThread(QThread):
	"""线程类用于接收UDP（控制电脑的操作指令）"""
	sinOut = pyqtSignal(str)

	def __init__(self,parent=None):
		super(UDPThread, self).__init__(parent)
		self.udpflag = True
	
	def __del__(self):
		self.udpflag = False
		self.wait()

	def run(self): 
		global server
		global datapath
		global udpconn

		while self.udpflag == True:
			try:

				data, addr = server.recvfrom(10240) #1024是接收字节 # resultlist 是关键字出现就报错
				# data = server.recv(10024) #1024是接收字节
				sx = str(data.decode('utf-8'))
				# server.sendto("ok".encode('utf-8'), addr)
				# server.close()
			except Exception as e:

				sx = str(data.decode('utf-8'))
				write_file(datapath,sx) #先将数据存储到本地
				self.sinOut.emit(sx)#发送数据到处理程序
				server.shutdown(2)#关闭整个通道
				# server.close()
				server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#允许端口重用。
				# 绑定 客户端口和地址:
				server.bind(udpconn)
			finally:
				write_file(datapath,sx) #先将数据存储到本地
				self.sinOut.emit(sx)#发送数据到处理程序
				


if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = cod_display("hello","./initialize/config.ini")
	example.show()
	sys.exit(app.exec_())