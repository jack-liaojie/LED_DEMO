import json
import uuid
import re
import csv
from decimal import Decimal

class ImportCSV(object):
	"""docstring for ClassName"""

	def __init__(self, arg):
		super(ImportCSV, self).__init__()
		self.arg = arg
# 2

	def readcsvfile(filename):
		try:
			rows = []
			with open(filename, 'r', encoding='utf-8') as f:
				reader = csv.reader(f)
				# print(type(reader))
				for row in reader:
					rows.append(row)
			return rows
		except Exception as e:
			raise e
		finally:
			pass
		

	def writecsvfile(filename, params):
		with open(filename, 'w', encoding='utf-8',newline='') as f:
			csv_writer = csv.writer(f)
			for row in params:
				csv_writer.writerow(row)
		f.close()

def generateUUID():
	id = uuid.uuid1()	# 还有uuid2、uuid3、uuid4、uuid5等其他方法
	return id

def write_file(path,args):
	try:
		f = open(path,"w",encoding="utf-8")
		f.write(args)#写入文件中

	except Exception as e:
		raise e
	finally:
		f.close()

def read_file(path):
	try:
		f = open(path,"r",encoding="utf-8")
		data = f.read()
		return data
	except IOError as e:
		raise e
	finally:
		f.close()

def strregex(args):
	# 通过正则表达式将decimal类型转为字符
	# 例如：Decimal('65.262000000')转为'65.262'
	args = str(args)
	args = re.sub(r"Decimal\(\'(\S*)000000\'\)",r"'\g<1>'", args)
	args = args.replace("\'","\"")
	return args

def str_dict(args):#返回的是的dict类型
	data ={}
	data = eval(args)
	return data #返回字典类型

def dict_str(args):
	return str(args)

def dict_json(args):#返回的是字符串类型
	#(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
	data = json.dumps(args, indent=4, separators=(",", ":"), ensure_ascii=False)#dict对象转换成格式化字符串
	return data

def json_dict(args):
	try:
		data={}
		# (2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）
		data = json.loads(args)
		return data #返回dict对象
	except :
		pass
	finally:
		pass


if __name__ == "__main__":
	args = {
		"top":
				{
				"left_path":"./resource/sward.jpg",
				"right_path":"./resource/sward.jpg",
				"title":"盛装舞步预赛"
				},
		"center":
				{
				"height": "1080",
				"timer":300,
				"modulepath": "./initialize/confige.ini",
				"pic_path": "E:/2020EQ/CODE/LED/resource/sward.jpg",
				"stylesheet": "font-size:30pt;background-color:rgb(26, 36,56);",
				"udp_ip": "127.0.0.1",
				"udp_port": "8080",
				"width": "1920",
				"x": "0",
				"y": "0"
				},
		"bottom":
				{
				"left_path":"./resource/sward.jpg",
				"right_path":"./resource/sward.jpg",
				"title":"盛装舞步预赛"
				}
	}

	path="./initialize/config.ini"
	args = dict_json(args)
	data = write_file(path,args)


	args =	{
		"welcome":{"title":"盛装舞步预赛"},
		"content":{"name":"welcome to Equestrain festivate"}
	}

	args =	{
			"schedule":"盛装舞步个人赛资格赛",
			"content":[
				[
					"09:00",
					"盛装舞步个人赛-资格赛",
					"盛装舞步个人赛-资格赛"
				],
				[
					"09:00",
					"盛装舞步个人赛-预赛",
					"盛装舞步个人赛-预赛"
				],
				[
					"09:00",
					"盛装舞步个人赛-决赛",
					"盛装舞步个人赛-决赛"
				]
			]
		}

	args =	{
		"judge" :{"title":"盛装舞步预赛"},
		"content":
			[ 
				{"judge":"主裁判","name" : "吉喆","city":"山东"},
				{"judge":"裁判员","name":"廖杰","city":"北戴河"},
				{"judge":"裁判员","name":"廖杰","city":"北戴河"},
				{"judge":"E","name":"廖杰","city":"北戴河"},
				{"judge":"M","name":"廖杰","city":"北戴河"},
				{"judge":"C","name":"廖杰","city":"北戴河"}
			]
	}

	args =	{
	"result":"盛装舞步个人赛资格赛",
	"data":[
		[
			1,
			4958,
			"盛装舞步个人赛",
			"资格赛",
			"盛装舞步个人赛-资格赛",
			null,
			"浙江队",
			"1",
			"贾海涛",
			"Corrinne Solyst",
			"10",
			"10",
			"",
			"62.368",
			"0.000",
			"65.263",
			"60.263",
			"0.000",
			"(9)",
			"(1)",
			"(9)",
			"(12)",
			"(1)",
			"62.631",
			"9",
			"62.631",
			"9",
			"[Image]浙江队",
			"贾海涛 / Corrinne Solyst",
			"浙江队"
		]
	],
	"content":"[(19, \"刘丽娜\", \"Don Dinero\", \"新疆队\", \"17\", \"17\", \"1\", \"70.087\", 1, \"Q\", \"70.087\", None, \"[Image]新疆队\", \"[Image]IRM_Q\", \"新疆队\", \"刘丽娜 / Don Dinero\")]"
	}

	args =	{
		"startlist" :"盛装舞步预赛",
		"content":
			[
		 		{"order":"1","name":"吉喆","horse":"火龙驹","city":"山东"},
		 		{"order":"2","name":"廖杰","horse":"火龙驹","city":"山东"},
		 		{"order":"3","name":"杨港","horse":"火龙驹","city":"山东"},
		 		{"order":"4","name":"旃泰溢","horse":"火龙驹","city":"山东"},
		 		{"order":"5","name":"吉喆","horse":"火龙驹","city":"山东"},
		 		{"order":"6","name":"吉喆","horse":"火龙驹","city":"山东"},
		 		{"order":"7","name":"吉喆","horse":"火龙驹","city":"山东"},
		 		{"order":"8","name":"吉喆","horse":"火龙驹","city":"山东"},
		 		{"order":"9","name":"吉喆","horse":"火龙驹","city":"山东"}
			]
		
	}
	
	args =	{
		"ranklist" : {"title":"盛装舞步预赛"},
		"content":
			[
		 		{"order":"1","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"2","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"3","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"4","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"5","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"6","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"7","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"8","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"9","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"10","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"11","name":"吉喆","result":"222","city":"山东"}
			]
		
	}
	
	args =	{
		"r_list" : {"title":"盛装舞步预赛"},
		"content":
			[	{"order":"1","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"2","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"3","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"4","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"5","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"6","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"7","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"8","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"9","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"10","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"11","name":"吉喆","result":"222","city":"山东","sign":"Q"}
		 	]

	}

	args =	{
		"medal" : {"title":"盛装舞步个人赛"},
		"content":
			[	{"order":"1","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"2","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"3","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"4","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"5","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"6","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"7","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"8","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"9","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"10","name":"吉喆","result":"222","city":"山东","sign":"Q"},
		 		{"order":"11","name":"吉喆","result":"222","city":"山东","sign":"Q"}
		 	]

	}
	args =	{
		"teamresultlist": {"title":"盛装舞步预赛"},
		"content":
 		[
	 		{"order":"1","result":"222","city":"山东"},
	 		{"order":"2","result":"222","city":"山东"},
	 		{"order":"3","result":"222","city":"山东"},
	 		{"order":"4","result":"222","city":"山东"},
	 		{"order":"5","result":"222","city":"山东"},
	 		{"order":"6","result":"222","city":"山东"},
	 		{"order":"7","result":"222","city":"山东"},
	 		{"order":"8","result":"222","city":"山东"},
	 		{"order":"9","result":"222","city":"山东"},
	 		{"order":"10","result":"222","city":"山东"},
	 		{"order":"11","result":"222","city":"山东"}
		]
		
	}
	

	# print(data)
	# args = read_file(path)
	# print(args["1"])
	# "stylesheet": "QMainWindow{"position:absolute;top:1000px;left:1000px;width:1024px;height:768px;background-color:rgb(255, 0, 0);font-size:24pt;background-image: url(./resource/sward.jpg);"}"
