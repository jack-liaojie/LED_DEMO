
# -*- coding:UTF-8 -*-

import xml.etree.ElementTree as ET

def write_xml(in_path,args):
	'''模拟写入配置信息到xml文件中，tag标签命名遵循css格式
		in_path:xml文件路径及名称
		args：字典数据
	'''
	root = ET.Element("configuration")
	y = ET.SubElement(root,'language')
	y.attrib ={"name": args['language']}
	y = ET.SubElement(root,'directory')
	y.attrib ={"name": args['directory']}

	y = ET.SubElement(root,'udp')
	y.attrib ={"ip": args['udp']['ip'],
			   "port":args['udp']['port']
				}

	y = ET.SubElement(root,'database')
	y.attrib ={"ip": args['database']['ip'],
			   "useer":args['database']['useer'],
			   "password":args['database']['password'],
			   "db":args['database']['db'],
			   }

	y = ET.SubElement(root,'display')
	y.attrib = {
			   'x':args['display']['x'],
			   'y':args['display']['y'],
			   'width':args['display']['width'],
			   'height':args['display']['height'],
			   'color':args['display']['backgroundcolor']
				}

	y = ET.SubElement(root,'top')
	y.attrib = {
			   'text':args['top']['text'],
			   'x':args['top']['x'],
			   'y':args['top']['y'],
			   'width':args['top']['width'],
			   'height':args['top']['height'],
			   'color':args['top']['color'],
			   'font':args['top']['font'],
			   'size':args['top']['size']
				}
	y = ET.SubElement(root,'footer')
	y.attrib = {
			   'text':args['footer']['text'],
			   'x':args['footer']['x'],
			   'y':args['footer']['y'],
			   'width':args['footer']['width'],
			   'height':args['footer']['height'],
			   'color':args['footer']['color'],
			   'font':args['footer']['font'],
			   'size':args['footer']['size']
				}
	y = ET.SubElement(root,'eq')
	y.attrib = {
			   'modul_name':args['eq']['modul_name'],
			   'grid':args['eq']['grid'],
			   'font':args['eq']['font'],
			   'size':args['footer']['size']
				}

	x = ET.SubElement(y,'text')
	x.attrib = {
			   'name':args['text']['name'],
			   'x':args['text']['x'],
			   'y':args['text']['y'],
			   'width':args['text']['width'],
			   'height':args['text']['height'],
			   'color':args['text']['color'],
			   'font':args['text']['font'],
			   'alignment':args['text']['alignment'],
			   'backgroundcolor':args['text']['backgroundcolor'],
			   'datafield':args['text']['datafield'],
			   'size':args['text']['size']
				}

	x = ET.SubElement(y,'image')
	x.attrib = {
			   'name':args['image']['name'],
			   'x':args['image']['x'],
			   'y':args['image']['y'],
			   'width':args['image']['width'],
			   'height':args['image']['height'],
			   'file':args['image']['file'],
			   'h_alignment':args['image']['h_alignment'],
			   'v_alignment':args['image']['v_alignment'],
			   'size':args['image']['size']
				}
	
	x = ET.SubElement(y,'grid')
	x.attrib = {
			   'name':args['grid']['name'],
			   'x':args['grid']['x'],
			   'y':args['grid']['y'],
			   'width':args['grid']['width'],
			   'height':args['grid']['height'],
			   'rows':args['grid']['rows'],
			   'cols':args['grid']['cols'],
			   'color':args['grid']['color'],
			   'size':args['grid']['size']
				}
	x = ET.SubElement(y,'shape')
	x.attrib = {
			   'name':args['shape']['name'],
			   'x':args['shape']['x'],
			   'y':args['shape']['y'],
			   'width':args['shape']['width'],
			   'height':args['shape']['height'],
			   'shape':args['shape']['shape'],
			   'border_width':args['shape']['border_width'],
			   'color':args['shape']['color'],
			   'visable':args['shape']['visable']
				}

	tree = ET.ElementTree(root)
	tree.write_xml(in_path, encoding="utf-8", xml_declaration=True)

def read_xml_iterator(args,element):
	'''将遍历xml子节点，并读出数据写入字典args中
	args：字典
	element：sub_root节点
	'''
	args={**args,**{element.tag:element.attrib}}#合并两个字典
	sub_element = list(element)
	if len(sub_element) == 0:
		return args
	else:
		for e in sub_element:#遍历子节点
			args = read_xml_iterator(args,e)
		return args #返回字典类型

def read_xml(path):
	'''读取xml文件'''
	args={}
	tree = ET.parse(path)
	root = tree.getroot()
	sub_root= list(root)
	for element in sub_root:#遍历子节点
		args = read_xml_iterator(args,element)
	return args#返回字典


def get_config(path):
	'''读出xml文件内容并转换为字典'''
	args = read_xml(path)
	print(args)

def set_config():
	'''模拟字典数据'''
	args={"language":"chn"}
	args['directory']="d:/workstudio/"
	args['udp']={'port':"8080",'ip':"127.0.0.1"}
	args['database']={'ip':".",'useer':"sa",'password':"111",'db':"eq"}
	args['display']={'x':"6",'y':"8",'width':"68",'height':"768",'backgroundcolor':"red"}
	args['top']={'text':"equestrain champion",'x':"6",'y':"8",'width':"68",'height':"768",'color':"768",'font':"微软雅黑",'size':"24"}
	args['eq']={'modul_name':"ranking",'grid':"6",'font':"微软雅黑",'size':"24"}
	args['footer']={'text':"equestrain champion",'x':"6",'y':"8",'width':"68",'height':"768",'color':"768",'font':"微软雅黑",'size':"24"}
	args['text']={'name':"column_1",'x':"6",'y':"8",'width':"68",'height':"768",'color':"768",'font-family':"微软雅黑",'font-size':"24",'alignment':'left','font-weight':'bold','backgroundcolor':'black','datafield':'txt_title'}
	args['image']={'name':"image_1",'x':"6",'y':"8",'width':"68",'height':"768",'file':"c:/x.bmp",'size':"24",'h_alignment':'left','v_alignment':'top'}
	args['grid']={'name':"rank_grid",'x':"6",'y':"8",'width':"68",'height':"768",'rows':"6",'cols':'left','color':'red','size':"24"}
	args['shape']={'name':"shape",'x':"6",'y':"8",'width':"68",'height':"768",'shape':"6",'border_width':'left','color':'red','visable':"false"}
	return args



if __name__ == '__main__':
	path="./initialize/confige.xml"
	get_config(path)
	# print(set_config())
	# write_xml(path,set_config())

