import json

def read_file(path):
	try:
		args={}
		f = open(path,"r",encoding="utf-8")
		data = f.read()
		args = json.loads(data)#将文件中的字符串转换为dict对象
		return args #返回dict对象
	except IOError as e:
		raise e
	finally:
		f.close()

def write_file(path,args):
	try:
		f = open(path,"w",encoding="utf-8")
		if type(args) == dict:
			data = json.dumps(args, sort_keys=True, indent=4, separators=(",", ":"))#dict对象转换成格式化字符串
		else:
			data = args.replace("\'","\"")
		f.write(data)#写入文件中

	except Exception as e:
		raise e
	finally:
		f.close()

def strtojs_format(args):
	data = json.dumps(args, sort_keys=True, indent=4, separators=(",", ":"))#dict对象转换成格式化字符串
	return data

def str_to_dict(args):
	data ={}
	data = eval(args)
	# args = json.loads(args)#将文件中的字符串转换为dict对象
	return data #返回字典类型

def dict_to_str(args):
	return str(args)


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
			    "modulepath": "./initialize/confige.ini",
			    "pic_path": "E:/2020EQ/CODE/LED/resource/sward.jpg",
			    "stylesheet": "font-size:24pt;background-color:rgb(255, 0,0);",
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

	path="./initialize/confige.ini"
	data = write_file(path,args)


	args =	{
		"welcome":{"title":"盛装舞步预赛"},
		"content":{"name":"welcome to Equestrain festivate"}
	}

	args =	{
		"schedule":{"title":"盛装舞步预赛"},
		"content":
			[
				{"time":"10:00","sport":"盛装舞步","event":"资格赛"},
				{"time":"11:00","sport":"盛装舞步","event":"资格赛"},
				{"time":"12:00","sport":"盛装舞步","event":"资格赛"}
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
		"result" :{"title":"盛装舞步预赛"},
		"data":
			[
				{"sport": "盛装舞步","event":"资格赛",
				 "order":"3","rank": "1","name":"廖杰","city":"山西","horse":"火龙驹","result":"343.33",
				 "E":"23","M":"123","C":"242","P":"234"}
			],
		"content":
			[	{"order":"1","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"2","name":"吉喆","result":"222","city":"山东"},
		 		{"order":"3","name":"吉喆","result":"222","city":"山东"}
		 	]
	}

	args =	{
		"startlist" :{"title":"盛装舞步预赛"},
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
		"resultlist" : {"title":"盛装舞步预赛"},
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
