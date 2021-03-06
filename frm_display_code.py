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
		self.fivetime = 0#设置默认计时时间
		self.fiveflag = True
		self.twentyflag = True
		self.twentypauseflag = False
		self.fivepauseflag = False
		self.twentytime = 20#设置默认计时时间
		self.listtime = 10000#设置默认列表滚屏时间
		self.load_config()
		self.clear_led()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.lbl_date.setText(QDate.currentDate().toString("yyyy-MM-dd dddd"))
		self.fivetimer = QTimer()
		self.fivetimer.setInterval(1000)
		self.fivetimer.timeout.connect(self.goTime)
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
			self.data_ini_args  = {
					"twentystart": "twentystart",
					"time": "",
					"mobile": ("127.0.0.1",4000),
					"status": "4"
				}#通过键盘操作时钟时，给一个初始化参数
			self.u_thread = UDPThread()#很简单的一个坑，把线程的声明放到类的初始化函数下就ok了。
			start_working(self.lbl_datetime)
		except:
			pass
		finally:
			#开启UDP监控线程
			self.start_udp(("",int(self.udp_port)))
			# self.start_udp((self.udp_ip,int(self.udp_port)))
			self.showMaximized()

	"""启动线程监听udp指令"""
	def start_udp(self,arg):
		global server

		try:
			server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#允许地址重用。
			server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

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
					self.fivestart(self.fivetime,'1',self.data_ini_args['mobile'])
				else:
					self.fiveflag = True
					self.fivestart(self.fivetime,'0')

			elif event.key() == Qt.Key_Shift:#20秒倒计时
				if self.twentyflag:
					self.twentyflag = False
					self.twentystart(self.twentytime,'1',self.data_ini_args['mobile'])
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


	#UDP控制系统
	def generateUUID(self):
		id = uuid.uuid1()  # 还有uuid2、uuid3、uuid4、uuid5等其他方法
		return id

	def sendmessage_tomobile(self,args,addr):
		# if isinstance(addr,list):addr = tuple(addr)
		re = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		re.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # 广播式发送数据设置

		addr = ('255.255.255.255', addr[1])
		re.sendto(args.encode('utf-8'), addr)
		re.close()

	def fivestart(self,timenum,fiveflag,addr=("127.0.0.1",4000)):
		"""正计时5分钟启动"""
		timenum = self.format_time(self.fivetime)
		self.datetime = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz")
		MessageID = str(self.generateUUID())

		if fiveflag == '1' and self.fivepauseflag == False:  # 开始
			if self.fivetimer.isActive():return#如果正在运行时钟，则返回防止归零
			self.fivetime = 0
			self.fivetimer.start()

			args =f"""
					{{
					  "Data": {{
						"CurrentTime": "{timenum}",
						"TimerNumber": 1,
						"IsIncrease": true,
						"IsRunning": true,
						"IsDisplay": true,
						"TotalTime": "23:00"
					  }},
					  "MessageType": "TimerStartForApp",
					  "MessageID": "{MessageID}",
					  "Timestamp": "{self.datetime}"
					}}
				"""
			self.sendmessage_tomobile(args,addr)
			return

		elif  fiveflag == '1' and self.fivepauseflag == True:#开始

			self.fivetimer.start()
			args = f"""
					{{
					  "Data": {{
						"CurrentTime": "{timenum}",
						"TimerNumber": 1,
						"IsIncrease": true,
						"IsRunning": true,
						"IsDisplay": true,
						"TotalTime": "23:00"
					  }},
					  "MessageType": "TimerStartForApp",
					  "MessageID": "{MessageID}",
					  "Timestamp": "{self.datetime}"
					}}
				"""

			self.sendmessage_tomobile(args, addr)
			return
		elif fiveflag == '0':#暂停
			self.fivepauseflag = True
			self.fivetimer.stop()
			args = f"""
					{{
					  "Data": {{
						"CurrentTime": "{timenum}",
						"TimerNumber": 1
					  }},
					"MessageType": "TimerPauseForApp",
					"MessageID": "{MessageID}",
					"Timestamp": "{self.datetime}"
					}}
					"""

			self.sendmessage_tomobile(args, addr)

			return
		elif fiveflag == '2':#复位
			self.lbl_fivetimer.setText("00:00")
			self.fivetimer.stop()
			self.fivetime = 0

			args =f"""
					{{
					  "Data": {{
						"CurrentTime": "00:00",
						"TimerNumber": 1
					  }},
					  "MessageType": "TimerResetForApp",
					  "MessageID": "{MessageID}",
					  "Timestamp": "{self.datetime}"
					}}
				"""

			self.sendmessage_tomobile(args,addr)

			self.fivepauseflag = False
			return
		elif fiveflag == '3':#清屏
			self.lbl_fivetimer.setText("")
			self.fivetimer.stop()
			self.fivetime = 0
			args = f"""
					{{
					  "Data": {{
						"CurrentTime": "00:00",
						"TimerNumber": 1
					  }},
					  "MessageType": "TimerResetForApp",
					  "MessageID": "{MessageID}",
					  "Timestamp": "{self.datetime}"
					}}
					"""

			self.sendmessage_tomobile(args, addr)

			self.fivepauseflag = False
			return
		elif fiveflag == '4':#显示
			if self.fivetimer.isActive():return
			self.lbl_fivetimer.setText("00:00")
			self.fivetimer.stop()
			self.fivetime = 0
			self.fivepauseflag = False
			return

	def twentystart(self,timenum,twentyflag,addr=("127.0.0.1",4000)):
		"""倒计时20秒启动"""
		self.datetime = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz")
		MessageID = str(self.generateUUID())

		if twentyflag == '1' and self.twentypauseflag == False:#开始
			if self.twentytimer.isActive():return
			self.twentytime = timenum

			timenum = self.format_time(timenum+1)
			self.twentytimer.start(1000)

			args =f"""
					{{
					  "Data": {{
						"CurrentTime":"{timenum}",
						"TimerNumber": 2,
						"IsIncrease": false,
						"IsRunning": true,
						"IsDisplay": true,
						"TotalTime": "00:00"
					  }},
					  "MessageType": "TimerStartForApp",
					  "MessageID": "{MessageID}",
					  "Timestamp": "{self.datetime}"
					}}
				"""

			self.sendmessage_tomobile(args,addr)
			return

		elif  twentyflag == '1' and self.twentypauseflag == True:#继续
			timenum = self.format_time(self.twentytime)

			self.twentytimer.start(1000)
			args =f"""
					{{
					  "Data": {{
						"CurrentTime": "{timenum}",
						"TimerNumber": 2,
						"IsIncrease": false,
						"IsRunning": true,
						"IsDisplay": true,
						"TotalTime": "00:00"
					  }},
					  "MessageType": "TimerStartForApp",
					  "MessageID": "{MessageID}",
					  "Timestamp": "{self.datetime}"
					}}
				"""

			self.sendmessage_tomobile(args,addr)
			return
		elif twentyflag == '0' :#暂停
			self.twentypauseflag = True
			self.twentytimer.stop()
			print(self.twentytime)
			timenum = self.format_time(self.twentytime)
			print(timenum)
			args = f"""
					{{
					  "Data": {{
						"CurrentTime": "{timenum}",
						"TimerNumber": 2
					  }},
					"MessageType": "TimerPauseForApp",
					"MessageID": "{MessageID}",
					"Timestamp": "{self.datetime}"
					}}
					"""
			self.sendmessage_tomobile(args, addr)

			return
		elif twentyflag == '2' :
			self.twentytimer.stop()#复位
			self.twentytime = timenum
			self.lbl_twentytimer.setText(str(timenum))

			timenum = self.format_time(self.twentytime)

			args =f"""
					{{
					  "Data": {{
						"CurrentTime": "{timenum}",
						"TimerNumber": 2
					  }},
					  "MessageType": "TimerResetForApp",
					  "MessageID": "{MessageID}",
					  "Timestamp": "{self.datetime}"
					}}
				"""
			self.sendmessage_tomobile(args,addr)

			self.twentypauseflag = False
			return
		elif twentyflag == '3' :
			self.twentytimer.stop()#清屏
			self.lbl_twentytimer.setText("")
			self.twentytime = timenum
			timenum = self.format_time(self.twentytime)
			self.twentypauseflag = False
			args =f"""
					{{
					  "Data": {{
						"CurrentTime":"{timenum}",
						"TimerNumber": 2
					  }},
					  "MessageType": "TimerResetForApp",
					  "MessageID": "{MessageID}",
					  "Timestamp": "{self.datetime}"
					}}
				"""
			self.sendmessage_tomobile(args,addr)

			return
		elif twentyflag == '4' :
			if self.twentytimer.isActive(): return
			self.twentytimer.stop()#显示
			self.lbl_twentytimer.setText(str(timenum))

			timenum = self.format_time(timenum)

			args = f"""
								{{
								  "Data": {{
									"CurrentTime": "{timenum}",
									"TimerNumber": 2
								  }},
								  "MessageType": "TimerResetForApp",
								  "MessageID": "{MessageID}",
								  "Timestamp": "{self.datetime}"
								}}
							"""
			self.sendmessage_tomobile(args, addr)

			return

	# def format_time(self, timenum):
	# 	m, s = divmod(timenum, 60)
	# 	h, m = divmod(m, 60)
	# 	timenum = "00:%02d:%02d.000" % (m, s)
	# 	return timenum

	def format_time(self,timenum):
		if timenum < 0:
			timenum = abs(timenum)
			m, s = divmod(timenum, 60)
			h, m = divmod(m, 60)
			timenum = "-00:%02d:%02d.000" % (m, s)
		else:
			m, s = divmod(timenum, 60)
			h, m = divmod(m, 60)
			timenum = "00:%02d:%02d.000" % (m, s)
		return timenum

	#倒计时钟显示
	def ReverseTime(self):
		self.twentytime -= 1
		self.lbl_twentytimer.setText('{:0>2s}'.format(str(self.twentytime)))

	def goTime(self):
		self.fivetime += 1
		m, s = divmod(self.fivetime, 60)
		h, m = divmod(m, 60)
		self.lbl_fivetimer.setText("%02d:%02d" % (m, s))

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
				self.twentystart(int(self.data_ini_args['time']),self.data_ini_args['status'],self.data_ini_args['mobile'])

			elif (a == "fivestart"):
				self.fivestart(int(self.data_ini_args['time']),self.data_ini_args['status'],self.data_ini_args['mobile'])

			else:

				# 从ly_center卸载widget
				if (self.ly_center.itemAt(0)):
					for i in reversed(range(self.ly_center.count())):
						self.ly_center.itemAt(i).widget().deleteLater()#两种方法都可以清除主窗体内的挂件
				# ly_center.itemAt(i).widget().setParent(None)

				if (a == "welcome"):
					self.lbl_title.setText(self.data_ini_args['welcome'])
					self.lbl_title_2.setText(self.data_ini_args['content'])
					self.tempform = mod_welcome(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)

				if (a == "step"):
					self.tempform = mod_step(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)

				elif (a == "result"):
					self.lbl_title_2.setText(self.data_ini_args['result'])
					self.tempform = mod_result(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)

				elif (a == "schedule"):
					self.lbl_title_2.setText(self.data_ini_args['schedule'])
					self.tempform = mod_schedule(self.data_ini_args,self.listtime)
					self.ly_center.addWidget(self.tempform)

				elif (a == "startlist"):
					self.lbl_title_2.setText(self.data_ini_args['startlist']+ "秩序单")
					self.tempform = mod_startlist(self.data_ini_args,self.listtime)
					self.ly_center.addWidget(self.tempform)

				elif (a == "r_list"):
					self.tempform = mod_resultlist(self.data_ini_args,self.listtime)
					self.ly_center.addWidget(self.tempform)
					self.lbl_title_2.setText(self.data_ini_args['r_list'] + "成绩公告")

				elif (a == 'k_list'):
					self.tempform = mod_ranklist(self.data_ini_args,self.listtime)
					self.ly_center.addWidget(self.tempform)
					self.lbl_title_2.setText(self.data_ini_args['k_list'] + "名次公告")

				elif (a == "judge"):
					self.lbl_title_2.setText(self.data_ini_args['judge'])
					self.tempform = mod_judge(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)

				elif (a == "medal"):
					self.tempform = mod_medal(self.data_ini_args)
					self.ly_center.addWidget(self.tempform)
					self.lbl_title_2.setText(self.data_ini_args['medal']+ "奖牌榜")

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