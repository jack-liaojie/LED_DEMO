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

#主窗体类
class cod_display(QWidget,Ui_Form):
	def __init__(self, arg,path):
		super(cod_display, self).__init__()
		self.setupUi(self)
		self.arg = arg
		self.ini_path = path
		self.tempform = QWidget
		self.fivetime = 300#设置默认计时时间
		self.fiveflag = True
		self.twentyflag = True
		self.twentypauseflag = False
		self.fivepauseflag = False
		self.twentytime = 20#设置默认计时时间
		self.load_config()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.twentytimer = QTimer()
		self.twentytimer.timeout.connect(self.ReverseTime)
	#清屏
	def clear_led(self):
		self.lbl_title.setText("")
		self.lbl_title_2.setText("")
		self.lbl_fivetimer.setText("")
		self.lbl_twentytimer.setText("")
		self.lbl_datetime.setText("")
		self.lbl_ico.setText("")

	"""加载ini文件"""
	def load_config(self):
		global udpconn
		global datapath

		try:
			ini_args = str_dict(read_file(self.ini_path))
			datapath = ini_args["center"]['datapath']
			self.setStyleSheet(ini_args["center"]['stylesheet'])
			self.udp_ip = ini_args["center"]['udp_ip']
			self.udp_port = ini_args["center"]['udp_port']
			udpconn = (self.udp_ip,int(self.udp_port))
			self.u_thread = UDPThread()#很简单的一个坑，把线程的声明放到类的初始化函数下就ok了。
			start_working(['datetime'],self.lbl_datetime)
		except:
			pass
		finally:
			#开启UDP监控线程
			self.start_udp((self.udp_ip,int(self.udp_port)))
			self.showMaximized()

	"""启动线程监听udp指令"""
	def start_udp(self,arg):
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

	"""udp指令线程停止"""
	def stop_udp(self):
		global server
		global datapath
		self.u_thread.finished()
		server.shutdown(2)#关闭整个通道
		sip.delete(self)#删除自身窗体


	def keyPressEvent(self,event):
		'''窗体快捷键'''
		global datapath
		try:
			if event.key() == Qt.Key_A:#Qt.Key_Escape
				self.stop_udp
				stop_working("datetime")
				stop_working("fivetime")
				self.close()

			elif event.key() == Qt.Key_Return:#5分钟正计时
				if self.fiveflag:
					self.fiveflag = False
					self.fivestart(self.fivetime,'1')
				else:
					self.fiveflag = True
					self.fivestart(self.fivetime,'0')

			elif event.key() == Qt.Key_Shift:#20秒倒计时
				if self.twentyflag:
					self.twentyflag = False
					self.twentystart(self.twentytime,'1')
				else:
					self.twentyflag = True
					self.twentystart(self.twentytime,'0')

			elif event.key() == Qt.Key_Space:

				self.load_data(read_file(datapath))#通过本地数据进行加载操作~

		except :
			pass
		finally:
			self.key = ""

	def scrollingstart(self, timenum, scrollflag):
		"""翻屏显示启动"""
		if scrollflag == "1" and (isinstance(self.tempform,mod_resultlist) or isinstance(self.tempform,mod_startlist)
								  or isinstance(self.tempform,mod_ranklist)):
			self.tempform.starttimer(timenum*1000)

		elif scrollflag == "0" and (isinstance(self.tempform,mod_resultlist) or isinstance(self.tempform,mod_startlist)
									or isinstance(self.tempform,mod_ranklist) ):
			self.tempform.endtimer()

	def fivestart(self,timenum,fiveflag):
		"""正计时5分钟启动"""
		self.fivetime = timenum
		if fiveflag == '1' and self.fivepauseflag == False:#开始
			start_working(['fivetime',timenum],self.lbl_fivetimer)
		elif  fiveflag == '1' and self.fivepauseflag == True:#开始
			start_working(['fivetime',"True"],self.lbl_fivetimer)
		elif fiveflag == '0':#暂停
			self.fivepauseflag = True
			stop_working('fivetime')
		elif fiveflag == '2':#复位
			stop_working('fivetime')
			self.lbl_fivetimer.setText("00:00")
			self.fivepauseflag = False
		elif fiveflag == '3':#清屏
			stop_working('fivetime')
			self.lbl_fivetimer.setText("")
			self.fivepauseflag = False

	def twentystart(self,timenum,twentyflag):
		"""倒计时20秒启动"""
		if twentyflag == '1' and self.twentypauseflag == False:#开始
			self.scrolltime = timenum
			self.twentytimer.start(1000)
			return
		elif  twentyflag == '1' and self.twentypauseflag == True:#开始
			self.twentytimer.start(1000)

			return
		elif twentyflag == '0' :#暂停
			self.twentypauseflag = True
			self.twentytimer.stop()

			return
		elif twentyflag == '2' :
			self.twentytimer.stop()#复位
			self.lbl_twentytimer.setText(str(timenum))

			self.twentypauseflag = False
			return
		elif twentyflag == '3' :
			self.twentytimer.stop()#清屏
			self.lbl_twentytimer.setText("")
			self.twentypauseflag = False

			return

		#倒计时钟显示
	def ReverseTime(self):
		self.lbl_twentytimer.setText('{:0>2s}'.format(str(self.scrolltime)))
		self.scrolltime -= 1

	"""对UDP数据进行解析并控制屏幕操作，是本地数据操作和在线数据操作的统一入口"""
	def load_data(self,sx):
		try:
			self.data_ini_args = json_dict(sx)

			a = self.data_ini_args.keys()
			a = list(a)[0]

			if (a == "C8kPeuWjMxOqm4Ca"):
				pass

			elif (a == "scrollingstart"):
				self.scrollingstart(int(self.data_ini_args['time']), self.data_ini_args['status'])

			elif (a == "twentystart"):
				self.twentystart(int(self.data_ini_args['time']),self.data_ini_args['status'])

			elif (a == "fivestart"):
				self.fivestart(int(self.data_ini_args['time']),self.data_ini_args['status'])

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
					self.lbl_fivetimer.setText('00:00')
					self.lbl_title_2.setText(self.data_ini_args['result'])
					self.tempform = mod_result(self.data_ini_args,self.counttime)
					self.ly_center.addWidget(self.tempform)

				elif (a == "schedule"):
					self.lbl_title_2.setText(args['schedule'])
					self.tempform = mod_schedule(self.data_ini_args,self.scrolltime)
					self.ly_center.addWidget(self.tempform)

				elif (a == "startlist"):
					self.lbl_title_2.setText(args['startlist']+ "秩序单")
					self.tempform = mod_startlist(self.data_ini_args,self.scrolltime)
					self.ly_center.addWidget(self.tempform)

				elif (a == "r_list"):
					self.tempform = mod_resultlist(self.data_ini_args,self.scrolltime)
					self.ly_center.addWidget(self.tempform)
					self.lbl_title_2.setText(args['r_list'] + "成绩公告")

				elif (a == 'k_list'):
					self.tempform = mod_ranklist(self.data_ini_args,self.scrolltime)
					self.ly_center.addWidget(self.tempform)
					self.lbl_title_2.setText(args['k_list'] + "名次公告")

				elif (a == "judge"):
					self.tempform = mod_judge(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)
					self.lbl_title_2.setText(args['judge'])

				elif (a == "medal"):
					self.tempform = mod_medal(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)
					self.lbl_title_2.setText(args['medal']+ "奖牌榜")

				elif (a == "celebrate"):
					self.tempform = mod_celebrate(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)

		except Exception as e:
			raise e
		finally:
			return

#线程类用于接收UDP（控制电脑的操作指令）
class UDPThread(QThread):
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